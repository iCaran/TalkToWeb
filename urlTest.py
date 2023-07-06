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

    """if match is None:
        return False
    elif match.group(1) is None and match.group(3) is None:
        print("Error: URL must include a protocol and a domain (e.g. http://www.)")
    elif match.group(1) is None:
        print("Error: URL must include a protocol (e.g. http://)")
        return False
    elif match.group(3) is None:
        print("Error: URL must include a domain (e.g. www.)")
        return False
    else:
        return True"""

    try:
        if match.group(1) is None:
            print(info_color + "URL query must include a protocol (e.g. http://)")
            print()
            error = True
            return False
        else:
            return True
    except:
        return False