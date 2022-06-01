import requests as rq
from key import auth_code, SECRET_KEY
import base64 as b64
import json
CLIENT_ID = "1370eaae12cf4cce90818ae130d85091"  # Client ID spotify aplikace analyser
REDIRECT_URI = "http://localhost:8080/"
SCOPES = ["user-library-read"]


def stringify(*query_args: str) -> str:  # takes a list of string arguments and
    # returns ? + arguments separated by ampersand
    return "?" + "&".join(query_args)


token = "BQBGTT-t5ffe6kpwyOEekzxGXwiFG7vDqHith_I4k1MEpbCpy2Qfkrt5SGUjQGPuTTcBQNtriu4j9FpSp8c6NsVMPX2QKJM9wLFyXGTUelO-GLYUdYz3Eq9QMU8r_pmbt2jst-yn3o-M-3FThR91msc8QEpS9S7f"


def get_token(authorization_code: str) -> str:
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": REDIRECT_URI
    }
    headers = {
        "Authorization": "Basic " + b64.b64encode(f"{CLIENT_ID}:{SECRET_KEY}".encode("utf-8")).decode("utf-8"),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = rq.post(url, data=data, headers=headers)
    data = json.loads(response.content.decode("utf-8"))
    return data["access_token"]


def get_authorize_url():
    return "https://accounts.spotify.com/authorize" + stringify(
        f"client_id={CLIENT_ID}",
        f"response_type=code",
        f"scope=" + "&20".join(SCOPES),
        f"redirect_uri={REDIRECT_URI}"
    )


def get_songs():
    headers = {
        "Authorization": f"Bearer {token}",  # TADY TO OPRAVIT
        "Content-Type": "application/json"
    }
    url = "https://api.spotify.com/v1/me/tracks" + stringify("limit=50")

    response = rq.get(url, headers=headers)
    print(response)
    print(response.content)


def main():
    print(get_authorize_url())
    get_songs()


if __name__ == "__main__":
    main()
