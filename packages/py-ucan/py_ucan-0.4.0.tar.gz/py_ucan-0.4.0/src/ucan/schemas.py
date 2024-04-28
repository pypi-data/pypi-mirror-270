import typing as t

import pydantic as pyd

from ucan.utils import validate_is_did


# typing
T_BaseModel = t.TypeVar("T_BaseModel", bound=pyd.BaseModel)


# Global Utils
validate_call = pyd.validate_call(
    config=pyd.ConfigDict(arbitrary_types_allowed=True),
    validate_return=True,
)


# base model
class BaseModel(pyd.BaseModel):
    """base pydantic model class."""

    model_config = pyd.ConfigDict(
        strict=False,
        frozen=True,
        arbitrary_types_allowed=True,
        validate_assignment=True,
        extra="forbid",
        revalidate_instances="always",
        validate_default=True,
        validate_return=True,
        from_attributes=False,
        populate_by_name=True,
        coerce_numbers_to_str=False,
    )


# Custom Pydantic Fields

DidString = t.Annotated[str, pyd.AfterValidator(validate_is_did)]
