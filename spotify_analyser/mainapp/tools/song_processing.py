if __name__ == "__main__":
    from sample import sample


def ms_to_human(ms: int) -> str:
    s = round(ms / 1000) % 60
    m = int((ms / 1000) // 60)
    return f"{m}:{s}"


def output_tracks(items: list) -> list:
    output = []
    for item in items:
        artists = ", ".join([artist["name"] for artist in item["track"]["album"]["artists"]])
        name = item["track"]["name"]
        length = ms_to_human(item["track"]["duration_ms"])
        popularity = item["track"]["popularity"]
        if not item["track"]["is_local"]:
            url = item["track"]["external_urls"]["spotify"]
        else:
            url = "/"
        output.append({"name": f"{artists} - {name}", "url": url, "length": length, "popularity": popularity})
    return output


def first_and_last(items: list, length: int = 5) -> (list, list):
    first = items[:length]
    last = items[len(items) - length:]
    last.reverse()
    return output_tracks(first), output_tracks(last)


def by_length(items: list, length: int = 5):
    items.sort(key=lambda x: x["track"]["duration_ms"])
    return first_and_last(items, length=length)


def by_artist_popularity(items: list, length: int = 5):
    items.sort(key=lambda x: x["track"]["popularity"])
    return first_and_last(items, length=length)


def min_max_avg(items: list) -> (int, int, int):
    avg = 0
    for item in items:
        avg += item["track"]["duration_ms"]
    avg /= len(items)
    shortest = min(items, key=lambda x: x["track"]["duration_ms"])["track"]["duration_ms"]
    longest = max(items, key=lambda x: x["track"]["duration_ms"])["track"]["duration_ms"]
    return ms_to_human(shortest), ms_to_human(longest), ms_to_human(avg)


def main():
    pass



if __name__ == "__main__":
    main()
