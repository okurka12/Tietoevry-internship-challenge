from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

if __name__ == "__main__":  # its only set up here like this so that my ide would recognize the module and load snippets
    from tools import spotify_api
    from tools import song_processing
else:
    from mainapp.tools import spotify_api
    from mainapp.tools import song_processing


def home(request):
    print(f"\ncookies\n{request.COOKIES}\n")
    if "auth_code" not in request.COOKIES:
        text = "Zdravíčko, abys viděl svoji spotify knihovnu, klikni na odkaz."
        data = {
            "text": text,
            "url": spotify_api.get_authorize_url(),
            "link_text": "Získat oblíbené písně"
        }
        return render(request, "mainapp/authorize.html", data)
    elif "auth_code" in request.COOKIES:
        return HttpResponseRedirect("/analysed_data")


def view_analysed_data(request):
    if "auth_code" in request.COOKIES:
        token = spotify_api.get_token(request.COOKIES["auth_code"])
        songs = spotify_api.get_songs(token)
        items = songs["items"]
        shortest, longest, avg = song_processing.min_max_avg(items)  # str str str
        shortests, longests = song_processing.by_length(items)  # list, list
        least_popular, most_popular = song_processing.by_artist_popularity(items)  # list list
        data = {
            "min": shortest, "max": longest, "avg": avg,
            "shortests": shortests, "longests": longests,
            "least_popular": least_popular, "most_popular": most_popular
        }
        response = render(request, "mainapp/data.html", data)
        response.delete_cookie("auth_code")
        return response
    else:
        return HttpResponseRedirect("/")


def process_redirect_from_api(request, query_str: str = ""):
    # print(request.GET["code"])
    # print(dir(request))
    # print(query_str)
    response = HttpResponseRedirect("/")
    response.set_cookie("auth_code", request.GET["code"])
    return response
