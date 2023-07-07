import re

def is_url(text, info_color = "\033[96m"):
    url_regex = r"^((http|https|ftp)://)?([A-Za-z0-9-]+\.)?[A-Za-z0-9-]+\.[A-Za-z0-9]+(/[A-Za-z0-9-]*)*$"
    match = re.match(url_regex, text)

    # match groups
    # 0 - example.com
    # 1 - http:// or https://
    # 2 - http or https
    # 3 - www.
    # 4 ???

    try:
        if match.group(1) is None:
            print(info_color + "URL query must include a protocol (e.g. http://)")
            print()
            return False
        else:
            return True
    except:
        return False
