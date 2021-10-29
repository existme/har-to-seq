import json


def read_json_file(filename):
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def find_base_url(url):
    end_pos = find_nth(url, '/', 4)
    return url[0:end_pos]
