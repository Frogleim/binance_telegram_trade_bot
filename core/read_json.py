import json


def read():
    file = open("response.json", encoding="utf8")
    data = json.load(file)
    return data["data"][0:11]


if __name__ == "__main__":
    res = read()
    print(res)
