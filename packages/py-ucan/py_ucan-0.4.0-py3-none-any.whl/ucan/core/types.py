from __future__ import annotations

import abc
import typing as t
import typing_extensions as te

import pydantic as pyd

from ucan.core.semver import SemVer
from ucan.schemas import BaseModel


# Function types


@te.runtime_checkable
class IsRevokedFunc(te.Protocol):
    async def __call__(self, ucan: Ucan) -> bool: ...


# SCHEMAS


class ResourcePointer(BaseModel):
    scheme: str
    hier_part: str = pyd.Field(alias="hierPart")

    SEPARATOR: t.ClassVar[str] = ":"

    @pyd.model_serializer
    def ser_model(self) -> dict[str, t.Any]:
        # https://github.com/pydantic/pydantic/issues/8379
        # for now, hard code the serializer
        return {"scheme": self.scheme, "hierPart": self.hier_part}

    @classmethod
    def from_string(cls, data: str) -> te.Self:
        """Load ResourcePointer from string.

        `data` must be in the format: {scheme}{SEPARATOR}{hier_part}.

        Args:
            data (str): string representation of ResourcePointer.

        Raises:
            TypeError: Expected {separater} in the value.

        Returns:
            te.Self: ResourcePointer object.
        """
        parts = data.split(cls.SEPARATOR)
        if len(parts) < 2:  # noqa: PLR2004
            msg = f"Expected '{cls.SEPARATOR}' in the value"
            raise TypeError(msg)

        return cls(scheme=parts[0], hier_part=cls.SEPARATOR.join(parts[1:]))

    def encode(self) -> str:
        """Returns a string representation of the ResourcePointer.

        The returned value is in the format: {scheme}{SEPARATOR}{hier_part}.

        Returns:
            str: String represenation of ResourcePointer.
        """
        return f"{self.scheme}{self.__class__.SEPARATOR}{self.hier_part}"


class Ability(BaseModel):
    namespace: str
    segments: list[str]

    SEPARATOR: t.ClassVar[str] = "/"

    @classmethod
    def from_string(cls, data: str) -> te.Self:
        parts = data.split(cls.SEPARATOR)
        if len(parts) < 2:  # noqa: PLR2004
            msg = f"Expected '{cls.SEPARATOR}' in the value"
            raise TypeError(msg)

        return cls(namespace=parts[0], segments=parts[1:])

    def encode(self) -> str:
        return self.__class__.SEPARATOR.join([self.namespace, *self.segments])


class Capability(BaseModel):
    with_: ResourcePointer = pyd.Field(alias="with")
    can: Ability

    @pyd.field_validator("with_", mode="before")
    def validate_with(cls, data: str | t.Any) -> ResourcePointer | t.Any:
        if isinstance(data, str):
            return ResourcePointer.from_string(data)

        return data

    @pyd.field_validator("can", mode="before")
    def validate_can(cls, data: str | t.Any) -> Ability | t.Any:
        if isinstance(data, str):
            return Ability.from_string(data)

        return data

    @pyd.model_serializer
    def ser_model(self) -> dict[str, t.Any]:
        # https://github.com/pydantic/pydantic/issues/8379
        # for now, hard code the serializer
        return {"with": self.with_, "can": self.can}


class UcanHeader(BaseModel):
    alg: str
    typ: str
    ucv: SemVer

    @pyd.field_validator("ucv", mode="before")
    def validate_ucv(cls, data: str | t.Any) -> SemVer | t.Any:
        if isinstance(data, str):
            return SemVer.from_string(data)

        return data


class UcanPayload(BaseModel):
    iss: str
    aud: str
    exp: int
    nbf: int | None = None
    nnc: str | None = None
    att: list[Capability]
    fct: list[t.Any] | None = None
    prf: list[str]


class UcanParts(BaseModel):
    header: UcanHeader
    payload: UcanPayload


class Ucan(UcanParts):
    # We need to keep the encoded version around to preserve the signature
    signed_data: str = pyd.Field(alias="signedData")
    signature: str

    @pyd.model_serializer
    def ser_model(self) -> dict[str, t.Any]:
        # https://github.com/pydantic/pydantic/issues/8379
        # for now, hard code the serializer
        return {
            "header": self.header,
            "payload": self.payload,
            "signedData": self.signed_data,
            "signature": self.signature,
        }
