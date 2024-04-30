""" This implements joining the base url with the given path"""

from urllib.parse import urljoin
from decouple import config


def join_url(path: str) -> str:
    """
    Join URL with Paystack API URL
    :param path:
    :return:
    """
    base_url = config("MONNIFY_BASE_URL")
    if path.startswith("/"):
        path = path[1:]
    return urljoin(base_url, path)
