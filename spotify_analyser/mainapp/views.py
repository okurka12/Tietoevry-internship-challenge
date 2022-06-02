from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

if __name__ == "__main__":  # its only set up here like this so that my ide would recognize the module and load snippets
    from tools import spotify_api
else:
    from mainapp.tools import spotify_api


def home(request):
    print(f"\ncookies\n{request.COOKIES}\n")
    if "auth_code" not in request.COOKIES:
        text = "Zdravíčko, abys viděl svoji spotify knihovnu, klikni na odkaz."
        data = {
            "text": text,
            "url": spotify_api.get_authorize_url(),
            "link_text": "Autorizovat aplikaci k přístupu do mojí knihovny"
        }
        return render(request, "mainapp/authorize.html", data)
    elif "auth_code" in request.COOKIES:
        token = spotify_api.get_token(request.COOKIES["auth_code"])
        print(50*"--tady--")
        songs = spotify_api.get_songs(token)
        response = HttpResponse(f"<p>{repr(songs)}</p>")
        response.delete_cookie("auth_code")
        print(songs)
        print(f"\n\nstr songs\n{str(songs)}\n")
        print(f"\nrepr songs\n{repr(songs)}")
        print(f"\n\ntype songs\n{type(songs)}")
        print(50 * "--konec--")
        return response


def process_redirect_from_api(request, query_str: str = ""):
    # print(request.GET["code"])
    # print(dir(request))
    # print(query_str)
    response = HttpResponseRedirect("/")
    response.set_cookie("auth_code", request.GET["code"])
    return response
