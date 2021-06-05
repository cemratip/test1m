#FAILED STRATEGY
import requests, json, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def GetMarketPrice():
    response = json.loads((requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')).text)
    marketprice = response['result']['XXBTZUSD']['c'][0]
    return marketprice


nexttrade = "buy"
period = '1m'
url = f'https://s.tradingview.com/embed-widget/technical-analysis/?locale=uk#%7B%22interval%22%3A%22{period}%22%2C%22width%22%3A425%2C%22isTransparent%22%3Afalse%2C%22height%22%3A450%2C%22symbol%22%3A%22KRAKEN%3AXBTUSD%22%2C%22showIntervalTabs%22%3Atrue%2C%22colorTheme%22%3A%22light%22%2C%22utm_source%22%3A%22cem-ratip-portfolio.000webhostapp.com%22%2C%22utm_medium%22%3A%22widget_new%22%2C%22utm_campaign%22%3A%22technical-analysis%22%7D'
options = webdriver.ChromeOptions()
#options.add_argument('headless')
#capa = DesiredCapabilities.CHROME
#capa["pageLoadStrategy"] = "none"
#driver = webdriver.Chrome(executable_path="C:\Python 38\chromedriver_win32 (1)\chromedriver.exe", options=options, desired_capabilities=capa)
#driver.set_window_size(1440,900)

while True:
    options.add_argument('headless')
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(executable_path="C:\Python 38\chromedriver_win32 (1)\chromedriver.exe", options=options, desired_capabilities=capa)
    driver.set_window_size(1440,900)
    driver.get(url)
    time.sleep(15)
    plain_text = driver.page_source
    soup = BeautifulSoup(plain_text, 'lxml')
    soupstr = str(soup)
    if ("speedometerSignal-DPgs-R4s buyColor-DPgs-R4s" in soupstr) and (nexttrade == "buy"):
        temp = str(soup.find_all(class_="speedometerSignal-DPgs-R4s buyColor-DPgs-R4s"))
        if ("Strong" in temp) and (nexttrade == 'buy'):
            marketprice = GetMarketPrice()
            print('strong buy @ ', marketprice)
            nexttrade = "sell"
            while nexttrade == "sell":
                options.add_argument('headless')
                capa = DesiredCapabilities.CHROME
                capa["pageLoadStrategy"] = "none"
                driver = webdriver.Chrome(executable_path="C:\Python 38\chromedriver_win32 (1)\chromedriver.exe", options=options, desired_capabilities=capa)
                driver.set_window_size(1440,900)
                driver.get(url)
                time.sleep(15)
                plain_text = driver.page_source
                soup = BeautifulSoup(plain_text, 'lxml')
                soupstr = str(soup)
                temp = str(soup.find_all(class_="speedometerSignal-DPgs-R4s sellColor-DPgs-R4s"))
                if ">Sell<" in temp:
                    marketprice = GetMarketPrice()
                    print('sell @ ', marketprice)
                    break
                driver.close()
    elif ("speedometerSignal-DPgs-R4s sellColor-DPgs-R4s" in soupstr) and (nexttrade == "sell"):
        temp = str(soup.find_all(class_="speedometerSignal-DPgs-R4s sellColor-DPgs-R4s"))
        if ("Strong" in temp) and (nexttrade == 'sell'):
            marketprice = GetMarketPrice()
            print('strong sell @ ', marketprice)
            nexttrade = "buy"
            while nexttrade == "buy":
                options.add_argument('headless')
                capa = DesiredCapabilities.CHROME
                capa["pageLoadStrategy"] = "none"
                driver = webdriver.Chrome(executable_path="C:\Python 38\chromedriver_win32 (1)\chromedriver.exe", options=options, desired_capabilities=capa)
                driver.set_window_size(1440,900)
                driver.get(url)
                time.sleep(15)
                plain_text = driver.page_source
                soup = BeautifulSoup(plain_text, 'lxml')
                soupstr = str(soup)
                temp = str(soup.find_all(class_="speedometerSignal-DPgs-R4s buyColor-DPgs-R4s"))
                if ">Buy<" in temp:
                    marketprice = GetMarketPrice()
                    print('buy @ ', marketprice)
                    break
                driver.close()

    driver.close()



#kraken public api key: NcYz0XyXRqhONr0Tqc6a9J5JVoNJ4uxwanJjw1KbiyHZMXphhNINRHKN
#kraken private api key: yTiERkyi1xD746de+df5MY/tIsSY/tGgpcMlYTdZ92j+pM3/h0TCFXZG3GL1eYQWbwEUvUw1rkZ8auaNjZa8GQ==

#test if I should sell when Strong Buy goes down to Buy   OR   sell when Strong Buy and buy when Strong sell
#test on all time frames
