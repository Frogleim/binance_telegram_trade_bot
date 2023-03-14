import json

full_path = "C:\\Users\\GSD Beast N10\\Desktop\\upwork jobs\\telegram_bot\\core\\"


def read_traders():
    file = open(f"{full_path}response.json", encoding="utf8")
    data = json.load(file)
    return data["data"][0:11]


def read_trades():
    file = open(f"{full_path}Trades.json", encoding="utf8")
    data = json.load(file)
    return data


if __name__ == "__main__":
    res = read_trades()
    print(res)
