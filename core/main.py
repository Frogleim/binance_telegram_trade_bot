from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
import time
import re
import subprocess
import json

urls = []


def get_traders(arg):
    args_json = json.dumps([arg])
    result = subprocess.check_output(['node', './core/get_traders.js', args_json])
    print(result.decode('utf-8'))


def read(trader_type):
    # trader_type = "DELIVERY"
    get_traders(trader_type)
    file = open("response.json", encoding="utf8")
    data = json.load(file)
    return data["data"][0:11]


def get_trades(trader_type):
    global urls
    res = read(trader_type)
    for users_id in res:
        user_id = users_id["encryptedUid"]
        base_url = f"https://www.binance.com/en/futures-activity/leaderboard/user/um?encryptedUid={user_id}"
        print(base_url)
        urls.append(base_url)
    return urls


class GetData:
    def __init__(self, urls_data):
        self.urls = urls_data
        self.driver = uc.Chrome()
        self.data_dict = {}
        self.final_data = []

    def get_data(self):
        with self.driver as main_driver:
            for url in self.urls:
                main_driver.get(url)
                try:
                    accept_cookies = main_driver.find_element(By.XPATH,
                                                              "/html/body/div[4]/div[3]/div/div[1]/div/div["
                                                              "2]/div/button[1]")
                    accept_cookies.click()
                    time.sleep(2)
                    cookies_choices = main_driver.find_element(By.XPATH,
                                                               "/html/body/div[4]/div[2]/div[3]/div[1]/button[2]")
                    cookies_choices.click()

                except Exception:
                    print("No Cookies...")
                time.sleep(2)
                count = 0
                while True:
                    try:
                        count += 1
                        username = main_driver.find_element(By.XPATH,
                                                            "/html/body/div[1]/div[2]/div[1]/div/div[1]/div[1]/div["
                                                            "1]/div[ "
                                                            "2]/div[1]/div[1]")

                        symbol = main_driver.find_element(By.XPATH,
                                                          f"/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div["
                                                          f"2]/div/div[ "
                                                          f"2]/div/div/div/div/table/tbody/tr[{count}]/td[1]/div/div[1]"
                                                          )
                        direction = main_driver.find_element(By.XPATH,
                                                             f"/html/body/div[1]/div[2]/div[1]/div/div["
                                                             f"2]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/"
                                                             f"tr[{count}]/"
                                                             f"td[1]/div/div[2]/div[1]")
                        leverage = main_driver.find_element(By.XPATH,
                                                            f"/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div["
                                                            f"2]/div/div[2]/div/div/div/div/table/tbody/tr[{count}]/td["
                                                            f"1]/div/div[2]/div[2]/div")
                        size = main_driver.find_element(By.XPATH,
                                                        f"/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[2]"
                                                        f"/div/div["
                                                        f"2]/div/div/div/div/table/tbody/tr[{count}]/td[2]")
                        entry_price = main_driver.find_element(By.XPATH,
                                                               f"/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div["
                                                               f"2]/div/div[2]/div/div/div/div/table/tbody/"
                                                               f"tr[{count}]/td["
                                                               f"3]")
                        pnl = main_driver.find_element(By.XPATH,
                                                       f"/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div["
                                                       f"2]/div/div/div/div/table/tbody/tr[{count}]/td[5]/div/span[1]")
                        roe = main_driver.find_element(By.XPATH,
                                                       f'/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div['
                                                       f'2]/div/div/div/div/table/tbody/tr[{count}]/td[5]/div/span[2]')
                        times = main_driver.find_element(By.XPATH,
                                                         f"/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div["
                                                         f"2]/div/div[ "
                                                         f"2]/div/div/div/div/table/tbody/tr[{count}]/td[6]")

                        d = {
                            "username": username.text,
                            "Symbol": symbol.text,
                            "Direction": direction.text,
                            "Leverage": leverage.text,
                            "size": size.text,
                            "Entry price": entry_price.text,
                        }

                        self.final_data.append(d)
                        print(
                            f"User: {username.text}| Symbol: {symbol.text} | Direction: {direction.text}| "
                            f"Leverage: {leverage.text} | "
                            f"Size: {size.text} | Entry Price:"
                            f" {entry_price.text}| PNL: {pnl.text} | ROE%: {roe.text} | Time: {times.text}")
                    except NoSuchElementException:
                        print("End..")
                        break

    def save_data(self):
        with open("Trades.json", "w") as save_file:
            json.dump(self.final_data, save_file)
        print("Save successfully")

    def run_all(self):
        self.get_data()
        self.save_data()


if __name__ == "__main__":
    import sys, os

    get_trades()
    trades_data = GetData(urls_data=urls)
    trades_data.get_data()
    time.sleep(1.3)
    trades_data.save_data()
