# py-ucan

[![pypi](https://img.shields.io/pypi/v/py-ucan.svg?color=4B8BBE)](https://pypi.org/project/py-ucan/)

This is a Python library to help the web applications make use
of UCANs in their authorization flows. To learn more about UCANs and how you
might use them in your application, visit [ucan website](https://ucan.xyz) or
read the [spec](https://github.com/ucan-wg/spec).


<a id="contents"></a>

# **Contents**

- [Installation](#installation)
- [Usage](#usage)
    - [Ucan Objects](#ucan-objects)
        - [ucan.ResourcePointer](#ucan-objects-resource-pointer)
    - [Validating UCAN Tokens](#validating-ucan-tokens)
    - [Verifying UCAN Invocations](#verifying-ucan-invocations)

<a id="installation"></a>

## Installation [`⇧`](#contents)

```
pip install -U py-ucan
```

<a id="usage"></a>

## Usage [`⇧`](#contents)

<a id="ucan-objects"></a>

### Ucan objects

All the objects are based on [Pydantic V2](https://docs.pydantic.dev/latest/) models. Ideally you would only need to use [`model_validate`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate) and [`model_dump`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump) of pydantic model functions, but please go through the docs for advanced usage.

NOTE: Ojects can be instantiated with field names in camel case, but to access those fields, you need to use their snake case names.

<a id="ucan-objects-resource-pointer"></a>

#### ucan.ResourcePointer

```py

from ucan import ResourcePointer

# -- from string
resource = ResourcePointer.decode("fileverse://solo.fileverse.io")
print(resource.scheme, resource.hier_part)
# output: fileverse //solo.fileverse.io

# -- from json: snake case
resource = ResourcePointer.model_validate({"scheme": "fileverse", "hier_part": "//solo.fileverse.io"})
print(resource.scheme, resource.hier_part)
# output: fileverse //solo.fileverse.io

# -- from json: camel case
resource = ResourcePointer.model_validate({"scheme": "fileverse", "hierPart": "//solo.fileverse.io"})
print(resource.scheme, resource.hier_part)
# output: fileverse //solo.fileverse.io

# -- from kwargs: snake case
resource = ResourcePointer(scheme="fileverse", hier_part="//solo.fileverse.io")
print(resource.scheme, resource.hier_part)
# output: fileverse //solo.fileverse.io

# -- from kwargs: camel case
resource = ResourcePointer(scheme="fileverse", hierPart="//solo.fileverse.io")
print(resource.scheme, resource.hier_part)
# output: fileverse //solo.fileverse.io

# dump to python dict
# all the objects above will dump to a dict with camel case fields
print(resource.model_dump()) 
# output: {"scheme": "fileverse", "hierPart": "//solo.fileverse.io"}

```


### Validating UCAN Tokens

To validate a token, you need to use the `validate` function.

```py

import ucan

# receive the token from user request.
encoded_token = "eyJhbG..."  # request.headers.get("Authorization") or similar
# parse and validate the token

try:
    # here `parsed_token` is an instance of `ucan.Ucan`.
    parsed_token = await ucan.validate(encoded_token)

except Exception as e:
    # Invalid token
    pass

```

### Verifying UCAN Invocations

Using a UCAN to authorize an action is called "invocation".

To verify invocations, you need to use the `verify` function.

```py

import ucan

# receive the token from user request.
encoded_token = "eyJhbG..."  # request.headers.get("Authorization") or similar

# generate service keypair
service_key = ucan.EdKeypair.generate()
service_did = service_key.did()  # will return "did:key:zabcde..."

# known resource and user to validate against
doc_id = "some-id"
user_did = "did:key:z6Mk..."

result = await ucan.verify(
    encoded_token,
    # to make sure we're the intended recipient of this UCAN
    audience=service_did,
    # capabilities required for this invocation & which owner we expect for each capability
    required_capabilities=[
        ucan.RequiredCapability(
            capability=ucan.Capability(
                with_=ucan.ResourcePointer(
                    scheme="fileverse", hier_part="//portal.fileverse.io"
                ),
                can=ucan.Ability(namespace=doc_id, segments=["EDIT", "VIEW"]),
            ),
            # check against a known owner of the `doc_id` resource
            root_issuer=user_did,
        ),
    ],
)

# result will be one of the following:
# error: ucan.VerifyResultError(ok=False, errors=[Exception("...")]
# success: ucan.VerifyResultOk(ok=True, value=[ucan.Verification(..)])

if isinstance(result, ucan.VerifyResultOk):
    # The UCAN authorized the user
    pass

else:
    # Unauthorized
    pass
```
