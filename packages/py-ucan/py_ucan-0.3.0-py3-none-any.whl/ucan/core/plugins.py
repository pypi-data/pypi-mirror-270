from __future__ import annotations

import ucan.typing as ut
from ucan.core.types import DidKeyPlugin
from ucan.schemas import DidString, validate_call
from ucan.utils import has_prefix, parse_prefixed_bytes


@validate_call
def parse_did_method(did: DidString) -> str:
    parts = did.split(":")
    if len(parts[1]) < 1:
        raise Exception(f"No DID method included: {did}")

    return parts[1]


class Plugins:
    keys: list[DidKeyPlugin]

    @validate_call
    def __init__(self, keys: list[DidKeyPlugin]) -> None:
        self.keys = keys

    @validate_call
    def _validate_did_method(self, did: DidString) -> str:
        did_method = parse_did_method(did)
        if did_method != "key":
            msg = f"Unknow did type: {did_method}. Expected 'key'."
            raise ValueError(msg)

        return did_method

    @validate_call
    async def verify_issuer_alg(self, did: DidString, jwt_alg: str) -> bool:
        self._validate_did_method(did)

        prefixed_bytes = parse_prefixed_bytes(did)

        for key_plugin in self.keys:
            if has_prefix(prefixed_bytes, key_plugin.prefix):
                return key_plugin.jwt_alg == jwt_alg

        msg = f"DID method not supported by plugins: {did}"
        raise ValueError(msg)

    @validate_call
    async def verify_signature(
        self, did: DidString, data: bytes, signature: bytes
    ) -> bool:
        self._validate_did_method(did)

        prefixed_bytes = parse_prefixed_bytes(did)

        for key_plugin in self.keys:
            if has_prefix(prefixed_bytes, key_plugin.prefix):
                return await key_plugin.verify_signature(did, data, signature)

        msg = f"DID method not supported by plugins: {did}"
        raise ValueError(msg)
