import requests


def download_course_data() -> list:
    """
    Fetches data from API about courses and trainers
    :return: list with nested dicts and lists
    """
    print("Downloading all future course data... ", end='')
    res = requests.get("https://proagile.se/api/publicEvents")
    data = res.json()
    # print("Done.")
    # pprint.pprint(data)
    return data
