from sample import sample


def output_tracks(items: list) -> list:
    output = []
    for item in items:
        artists = ", ".join([artist["name"] for artist in item["track"]["album"]["artists"]])
        name = item["track"]["name"]
        if not item["track"]["is_local"]:
            url = item["track"]["external_urls"]["spotify"]
        else:
            url = "/"
        output.append({"name": f"{artists} - {name}", "url": url})
    return output


def first_and_last(items: list, length: int = 5) -> (list, list):
    first = items[:length]
    last = items[len(items) - length:]
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
    shortest = min(items, key=lambda x: x["track"]["duration_ms"])
    longest = max(items, key=lambda x: x["track"]["duration_ms"])
    return shortest, longest, avg


def main(sample=sample):
    pass



if __name__ == "__main__":
    main()
