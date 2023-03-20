from datetime import timedelta

SIMPLE_JWT_CONF = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),  # Lifetime can be anything of our choice.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),  # Lifetime can be anything of our choice.
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
}
