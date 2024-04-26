from functools import wraps
from typing import Any, Callable

import requests
from flask import Flask, current_app, jsonify
from flask.typing import ResponseReturnValue
from flask_jwt_extended import JWTManager, jwt_required
from jwt.algorithms import RSAAlgorithm


def conditional_jwt_required(fn: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if current_app.config["AUTH_ENABLED"]:
            return jwt_required()(fn)(*args, **kwargs)
        return fn(*args, **kwargs)
    return wrapper


def expired_token_callback(_expired_jwt_header: Any, _expired_jwt_data: Any) -> ResponseReturnValue:
    return jsonify({
        "msg": "The token has expired",
        "status": 401,
    }), 401


def invalid_token_callback(error_string: str) -> ResponseReturnValue:
    return jsonify({
        "msg": error_string,
        "status": 401,
    }), 401


def unauthorized_callback(error_string: str) -> ResponseReturnValue:
    return jsonify({
        "msg": error_string,
        "status": 401,
    }), 401


def needs_fresh_token_callback(_jwt_header: Any, _jwt_data: Any) -> ResponseReturnValue:
    return jsonify({
        "msg": "Fresh token required",
        "status": 401,
    }), 401


def revoked_token_callback(_jwt_header: Any, _jwt_data: Any) -> ResponseReturnValue:
    return jsonify({
        "msg": "Token has been revoked",
        "status": 401,
    }), 401


def token_verification_failed_callback() -> ResponseReturnValue:
    return jsonify({
        "msg": "User claims verification failed",
        "status": 401,
    }), 401


def apply_jwt_manager(app: Flask) -> None:
    jwt = JWTManager(app)

    jwt.expired_token_loader(expired_token_callback)
    jwt.invalid_token_loader(invalid_token_callback)
    jwt.unauthorized_loader(unauthorized_callback)
    jwt.needs_fresh_token_loader(needs_fresh_token_callback)
    jwt.revoked_token_loader(revoked_token_callback)
    jwt.token_verification_failed_loader(token_verification_failed_callback)


def urljoin(*args: str) -> str:
    return "/".join(map(lambda x: str(x).rstrip("/"), args))


def generate_jwt_public_key(realm_url: str, jwt_algorithm: str = "RS256") -> RSAAlgorithm:
    if jwt_algorithm != "RS256":
        raise ValueError(f"Unsupported JWT algorithm: {jwt_algorithm}")
        # TODO: Support other algorithms
    ordc_config = requests.get(
        urljoin(realm_url, ".well-known/openid-configuration"),
        timeout=5
    ).json()
    oidc_jwks = requests.get(ordc_config["jwks_uri"], timeout=5).json()
    try:
        oidc_jwk = next(key for key in oidc_jwks["keys"] if key["alg"] == jwt_algorithm)
    except StopIteration as e:
        raise ValueError(f"JWK for {jwt_algorithm} not found") from e

    return RSAAlgorithm.from_jwk(oidc_jwk)  # type: ignore
