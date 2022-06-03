import requests as rq
import base64 as b64
import json
from time import perf_counter
if __name__ == "__main__":  # so that IDE is not confused but also django project will work
    from key import SECRET_KEY
else:
    from mainapp.tools import key
    SECRET_KEY = key.SECRET_KEY


CLIENT_ID = "1370eaae12cf4cce90818ae130d85091"  # Client ID spotify aplikace analyser
REDIRECT_URI = "http://localhost/proceed_with_auth_code/"  # set this to the domain the project is currently running on
SCOPES = ["user-library-read"]


def stringify(*query_args: str) -> str:  # takes a list of string arguments and
    # returns ? + arguments separated by ampersand
    return "?" + "&".join(query_args)


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


def get_authorize_url() -> str:
    return "https://accounts.spotify.com/authorize" + stringify(
        f"client_id={CLIENT_ID}",
        f"response_type=code",
        f"scope=" + "&20".join(SCOPES),
        f"redirect_uri={REDIRECT_URI}"
    )


def get_songs(token: str) -> dict:
    t = perf_counter()
    headers = {
        "Authorization": f"Bearer {token}",  # TADY TO OPRAVIT
        "Content-Type": "application/json"
    }
    url = "https://api.spotify.com/v1/me/tracks" + stringify("limit=50")

    response = rq.get(url, headers=headers)
    output = json.loads(response.content.decode("utf-8"))
    # tady zmena
    song_count = output["total"]
    for i in range(1, song_count//50 + 1):
        next_response = rq.get("https://api.spotify.com/v1/me/tracks" + stringify("limit=50", f"offset={i*50}"), headers=headers)
        print(f"Obtaining songs {i*50} - {i*50 + 50} out of {song_count} - {next_response}")
        output["items"].extend(json.loads(next_response.content.decode("utf-8"))["items"])
    items = output["items"]
    print(f"obtained {song_count} items in {i + 1} requests in {perf_counter() - t:.7} s")
    return output


def main():
    print(get_authorize_url())
    get_songs()


if __name__ == "__main__":
    main()
