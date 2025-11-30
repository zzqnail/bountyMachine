"""
Schematics for the authorization
API calls, etc.
"""

import os
import requests
import asyncio
from src.core.settings import (
CLIENT_ID, CLIENT_SECRET,
)

_ACCESS_TOKEN_URL = 'https://api.hh.ru/token'
redirect_url = 'url/temp'

async def get_access_token(access_code: str = None):
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": access_code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_url,
    }
    #API request to change access_code to access_token
    response = requests.post(
        url=_ACCESS_TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        json = payload,
    )

async def get_refresh_token(rf_token: str = None):
    payload = {
        "refresh_token": rf_token,
        "grant_type": "refresh_token",
        "redirect_uri": redirect_url,
    }
    response = requests.post(
        url=_ACCESS_TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        json = payload,
    )