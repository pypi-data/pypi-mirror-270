"""ucan package root."""

from __future__ import annotations

import typing_extensions as te

import pydantic as pyd
import pydantic.dataclasses

from ucan.core import attenuation as attenuationlib
from ucan.core import token as tokenlib
from ucan.core import verify as verifylib
from ucan.core.plugins import Plugins
from ucan.default_plugins import ed25519_plugin, EdKeypair


__version__ = "0.3.0"


__all__ = (
    "Plugins",
    "PluginInjectedAPI",
    "default_plugins",
    "injected_api",
    # plugins
    "EdKeypair",
    "ed25519_plugin",
)


@pyd.dataclasses.dataclass(
    frozen=True,
    kw_only=True,
    config=pyd.ConfigDict(extra="forbid", frozen=True, arbitrary_types_allowed=True),
)
class PluginInjectedAPI:
    """Ucan API with plugins injected."""

    delegation_chains: attenuationlib.DelegationChainsFunc
    validate: tokenlib.TokenValidateFunc
    validate_proofs: tokenlib.ValidateProofFunc
    verify: verifylib.VerifyTokenFunc

    @classmethod
    def from_plugins(cls, plugins: Plugins) -> te.Self:
        """Build `PluginInjectedAPI` from a `Plugins` object."""
        return cls(
            validate=tokenlib.validate(plugins),
            verify=verifylib.verify(plugins),
            validate_proofs=tokenlib.validate_proofs(plugins),
            delegation_chains=attenuationlib.delegation_chains(plugins),
        )


default_plugins = Plugins([ed25519_plugin])
injected_api = PluginInjectedAPI.from_plugins(default_plugins)

delegation_chains = injected_api.delegation_chains
validate = injected_api.validate
validate_proofs = injected_api.validate_proofs
verify = injected_api.verify
