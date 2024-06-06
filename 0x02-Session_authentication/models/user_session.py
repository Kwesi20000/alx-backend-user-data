#!/usr/bin/env python3
"""A user session module.
"""
from models.base import Base


class UserSession(Base):
    """A user session class.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """this initializes a User session instance.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
