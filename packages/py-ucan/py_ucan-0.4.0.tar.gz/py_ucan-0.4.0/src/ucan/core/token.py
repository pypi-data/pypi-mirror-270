"""ucan.core.token module."""

from __future__ import annotations

import math
import typing as t
import typing_extensions as te

import jwt
from jwt.api_jwt import decode_complete

from ucan.core.plugins import Plugins
from ucan.core.types import Ucan, UcanHeader, UcanParts, UcanPayload
from ucan.schemas import validate_call
from ucan.utils import aware_utcfromtimestamp, aware_utcnow


class ProofError(Exception):
    pass


@te.runtime_checkable
class TokenParseFunc(te.Protocol):
    async def __call__(self, encoded_ucan: str) -> UcanParts: ...


@te.runtime_checkable
class TokenValidateFunc(te.Protocol):
    async def __call__(
        self,
        encoded_ucan: str,
        *,
        check_issuer: bool = True,
        check_signature: bool = True,
        check_is_expired: bool = True,
        check_is_too_early: bool = True,
    ) -> Ucan: ...


@te.runtime_checkable
class ValidateProofFunc(te.Protocol):
    def __call__(
        self,
        ucan: Ucan,
        *,
        check_addressing: bool = True,
        check_time_bounds_subset: bool = True,
        check_version_monotonic: bool = True,
        check_issuer: bool = True,
        check_signature: bool = True,
        check_is_expired: bool = True,
        check_is_too_early: bool = True,
    ) -> t.AsyncIterator[Ucan | Exception]: ...


def is_expired(ucan: Ucan) -> bool:
    """Check if a UCAN is expired."""
    return aware_utcfromtimestamp(ucan.payload.exp) <= aware_utcnow()


def is_too_early(ucan: Ucan) -> bool:
    """Check if a UCAN is not active yet."""
    if ucan.payload.nbf is None:
        return False
    return ucan.payload.nbf > math.floor(aware_utcnow().timestamp())


@validate_call
def parse(plugins: Plugins) -> TokenParseFunc:
    @validate_call
    async def _parse_inner(encoded_ucan: str) -> UcanParts:
        try:
            decoded_token = decode_complete(
                encoded_ucan, options={"verify_signature": False}
            )

            raw_header = decoded_token["header"]
            token_header = UcanHeader.model_validate(raw_header, strict=False)

            raw_payload = decoded_token["payload"]
            token_payload = UcanPayload.model_validate(raw_payload, strict=False)

            return UcanParts(header=token_header, payload=token_payload)

        except ValueError as err:
            msg = (
                f"Can't parse UCAN: {encoded_ucan}: Expected JWT format: "
                "3 dot-separated base64url-encoded values."
            )
            raise ValueError(msg) from err

    return _parse_inner


@validate_call
def validate(plugins: Plugins) -> TokenValidateFunc:
    @validate_call
    async def _validate_inner(
        encoded_ucan: str,
        *,
        check_issuer: bool = True,
        check_signature: bool = True,
        check_is_expired: bool = True,
        check_is_too_early: bool = True,
    ) -> Ucan:
        """Parse & Validate **one layer** of a UCAN."""
        parsed = await parse(plugins)(encoded_ucan)
        encoded_header, encoded_payload, encoded_signature = encoded_ucan.split(".")
        signed_data = f"{encoded_header}.{encoded_payload}"
        signed_data_bytes = signed_data.encode("utf8")
        signature_bytes = jwt.utils.base64url_decode(encoded_signature)

        if check_issuer and not await plugins.verify_issuer_alg(
            parsed.payload.iss, parsed.header.alg
        ):
            msg = (
                f"Invalid UCAN: {encoded_ucan}: Issuer key type does not "
                "match UCAN's `alg` property."
            )
            raise ValueError(msg)

        if check_signature:
            await plugins.verify_signature(
                parsed.payload.iss, signed_data_bytes, signature_bytes
            )

        ucan = Ucan(
            header=parsed.header,
            payload=parsed.payload,
            signed_data=signed_data,
            signature=encoded_signature,
        )

        if check_is_expired and is_expired(ucan):
            msg = f"Invalid UCAN: {encoded_ucan}: Expired."
            raise ValueError(msg)

        if check_is_too_early and is_too_early(ucan):
            msg = f"Invalid UCAN: {encoded_ucan}: Not active yet (too early)."
            raise ValueError(msg)

        return ucan

    return _validate_inner


@validate_call
def validate_proofs(plugins: Plugins) -> ValidateProofFunc:
    @validate_call
    async def _validate_proofs_inner(
        ucan: Ucan,
        *,
        check_addressing: bool = True,
        check_time_bounds_subset: bool = True,
        check_version_monotonic: bool = True,
        check_issuer: bool = True,
        check_signature: bool = True,
        check_is_expired: bool = True,
        check_is_too_early: bool = True,
    ) -> t.AsyncIterator[Ucan | Exception]:
        for prf in ucan.payload.prf:
            try:
                proof = await validate(plugins)(
                    prf,
                    check_issuer=check_issuer,
                    check_signature=check_signature,
                    check_is_expired=check_is_expired,
                    check_is_too_early=check_is_too_early,
                )
                if check_addressing and ucan.payload.iss != proof.payload.aud:
                    yield ProofError(
                        f"Invalid Proof: Issuer {ucan.payload.iss} doesn't match parent's audience {proof.payload.aud}"
                    )
                if (
                    check_time_bounds_subset
                    and proof.payload.nbf is not None
                    and ucan.payload.exp > proof.payload.nbf
                ):
                    yield ProofError(
                        f"Invalid Proof: 'Not before' ({proof.payload.nbf}) is after parent's expiration ({ucan.payload.exp})"
                    )

                if (
                    check_time_bounds_subset
                    and ucan.payload.nbf is not None
                    and ucan.payload.nbf > proof.payload.exp
                ):
                    yield ProofError(
                        f"Invalid Proof: Expiration ({proof.payload.exp}) is before parent's 'not before' ({ucan.payload.nbf})"
                    )

                if check_version_monotonic and ucan.header.ucv.lt(proof.header.ucv):
                    yield ProofError(
                        f"Invalid Proof: Version ({proof.header.ucv}) is higher "
                        f"than parent's version ({ucan.header.ucv})"
                    )

                yield proof

            except ProofError as e:  # noqa: PERF203
                yield e

            except Exception as e:
                yield ProofError(f"Error when trying to parse UCAN proof: {e}")

    return _validate_proofs_inner
