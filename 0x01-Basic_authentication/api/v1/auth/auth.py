#!/usr/bin/env python3
"""
An Authentication module
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """
    An authentiication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        A method to check  if auth is required.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """A method to get authorization header"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A method to get user from request"""
        return None
