from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

if __name__ == "__main__":  # its only set up here like so so my ide would recognize the module and load snippets
    from tools import spotify_api
else:
    from mainapp.tools import spotify_api


def home(request):
    if "auth_code" not in request.COOKIES:
        text = "Zdravíčko, abys viděl svoji spotify knihovnu, klikni na odkaz."
        data = {
            "x": text,
            "url": spotify_api.get_authorize_url(),
            "link_text": "Autorizovat aplikaci k přístupu do mojí knihovny"
        }
        return render(request, "mainapp/home.html", data)


def process_redirect_from_api(request, query_str: str = ""):
    print(request)
    print(dir(request))
    print(query_str)
    return HttpResponseRedirect("/")
