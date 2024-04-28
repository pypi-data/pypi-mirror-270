"""
Get cookie for LeetCode API
"""


def get_cookies(cookie_file: str) -> dict:
    """
    Load all cookies from a Netscape HTTP Cookie File

    Args:
        cookie_file (str): path to Netscape HTTP Cookie File

    Returns:
        dict: dictionary of all cookie keys and values
    """
    cookies = {}

    KEY_COLUMN = 5
    VALUE_COLUMN = 6

    try:
        with open(cookie_file, 'r') as file:
            for line in file:
                if not line.startswith('#'):
                    items = line.strip().split('\t')

                    # make sure cookie file has correct number of columns
                    if len(items) > VALUE_COLUMN:
                        key = items[KEY_COLUMN]
                        value = items[VALUE_COLUMN]

                        cookies[key] = value

    except FileNotFoundError:
        print(f'Could not find {cookie_file}')

    if not cookies:
        print('No cookies found')

    return cookies
