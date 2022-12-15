import requests
import pprint


def download_course_data() -> list:
    """
    Fetches data from API about courses and trainers
    :return: list with nested dicts and lists
    """
    print("Downloading all future course data... ", end='')
    res = requests.get("https://proagile.se/api/publicEvents")
    data = res.json()
    # pprint.pprint(data)
    return data


def download_employee_data() -> list:
    """
    Fetches data from API about employees and phonenumbers etc
    :return: list with nested dicts and lists
    """
    print("Downloading all future course data... ", end='')
    res = requests.get("https://proagile.se/api/publicEmployees")
    employee_data = res.json()
    # pprint.pprint(employee_data)
    return employee_data
