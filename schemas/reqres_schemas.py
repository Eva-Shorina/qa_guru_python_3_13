from voluptuous import Schema, PREVENT_EXTRA

new_user_schema = Schema(
    {
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_user_schema = Schema(
    {
    "name": str,
    "job": str,
    "updatedAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

login_schema = Schema(
    {
    "token": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)

