from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login_amz():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options=options)

    driver.get("https://www.amazon.com/")

    # Sign in
    time.sleep(3)
    sign_in_btn_el = driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&']")

    time.sleep(3)
    sign_in_btn_el.click()

    # Email or Username
    time.sleep(3)
    sign_in_email_el = driver.find_element(By.XPATH, "//input[@type='email']")

    time.sleep(1.5)
    sign_in_email_el.send_keys("muchamadfaizjse@gmail.com")

    time.sleep(3)
    sign_in_btn_email_el = driver.find_element(By.XPATH, "//input[@type='submit']")

    time.sleep(3)
    sign_in_btn_email_el.click()

    # Password
    time.sleep(3)
    sign_in_pass_el = driver.find_element(By.XPATH, "//input[@type='password']")

    time.sleep(1.5)
    sign_in_pass_el.send_keys("Faiz6*-7")

    time.sleep(3)
    sign_in_btn_pass_el = driver.find_element(By.XPATH, "//input[@type='submit']")

    time.sleep(3)
    sign_in_btn_pass_el.click()

    time.sleep(3)
    search_el = driver.find_element(By.XPATH, "//input[@type='text']")

    time.sleep(2)
    search_btn_el = driver.find_element(By.ID, "nav-search-submit-button")
    # print(search_btn.get_attribute("class"))

    time.sleep(2)
    search_btn_el.click()

    time.sleep(3)
    current_url = driver.current_url + "s?"
    time.sleep(3)

    return current_url

def get_product_links(page, query, current_url):
    # URL = "https://www.amazon.com/s?k=computer+monitor&sprefix=compu%2Caps%2C451&ref=nb_sb_ss_pltr-ranker-1hour_2_5"
    URL = current_url # "https://www.amazon.com/s?"
    # Headers for request
    HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '3.4',
    'dpr': '1',
    'referer': 'https://www.amazon.com/',
    'ect': '4g',
    'rtt': '50',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1.1',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-viewport-width': '811',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'viewport-width': '811'       
    }
    PARAMS = {
        'k' : query,
        'page' : page,
        # "crid" : "374OZ2EFZ8MUU",
        # "qid" : "1667236444",
        # "sprefix" : "iphone,aps,1150",
        # "ref" : "sr_pg_5"
    }
    response = req.get(url=URL, params=PARAMS, headers=HEADERS)
    # response = req.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    tags = soup.find_all("div", {"data-component-type" : "s-search-result"})
    # print(len(tags))
    links = []
    for tag in tags:
        product_link = tag.find("a")['href'].strip()
        link = "https://www.amazon.com" + product_link
        links.append(link) 
    return links
        

def parse_product(url):
# response = req.get(url=test_link, headers=HEADERS)
    HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '3.4',
    'dpr': '1.1',
    'ect': '4g',
    'rtt': '50',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1.1',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-viewport-width': '1242',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'viewport-width': '1242'       
    }
    response = req.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    link = url
    try:
        title = soup.find("span", {"class" : "a-size-large product-title-word-break"}).get_text().strip()
    except AttributeError as err:
        title = ""

    try:
        price_whole = soup.find("span", {"class" : "a-price-whole"}).text.strip()
        price_fraction = soup.find("span", {"class" : "a-price-fraction"}).text.strip()
        price_symbol = soup.find("span", {"class" : "a-price-symbol"}).text.strip()
        price = price_symbol + price_whole + price_fraction
    except AttributeError as err:
        price = ""

    try:
        rating_value = soup.find("i", {"class" : "a-icon a-icon-star a-star-4-5"}).text[0:3]
    except AttributeError as err:
        rating_value = ""
        
    try:
        review_number = re.findall(r"\d\S+", soup.find("span", {"id" : "acrCustomerReviewText"}).text)[0]
    except AttributeError as err:
        review_number = ""
    except IndexError as err:
        review_number = ""

    try: 
        dimension = soup.find("td", {"class" : "a-size-base prodDetAttrValue"}).text.strip()
    except AttributeError as err:
        dimension = ""    
    
    try:
        image = soup.find("div",{"id" : "imgTagWrapperId"}).find("img")["src"]
    except AttributeError as err:
        image = ""

    product = {
        "title" : title, # Westinghouse Home Office Monitor (32" 4K Ultra HD VA 60Hz)
        "price" : price, # $309.99
        "rating_value" : rating_value, # 4.3
        "review_number" : review_number, # 43
        "dimension" : dimension, # 32 inches
        "link" : link, # https://www.amazon.com/Westinghouse-Home-Office-Monitor-Ultra/dp/B09ZMN4M28/ref=sr_1_1_sspa?keywords=computer+monitor&qid=1667238811&qu=eyJxc2MiOiI4LjAwIiwicXNhIjoiNy4zMCIsInFzcCI6IjYuNjUifQ%3D%3D&sprefix=compu%2Caps%2C451&sr=8-1-spons&psc=1
        "image" : image # https://m.media-amazon.com/images/I/81ZOtaNT1-L._AC_SX425_.jpg
    }
    return product


def save_CSV (results,query):
    df = pd.DataFrame(results)
    df.to_csv(query + ".csv", index=False)


def save_XLX (results,query):
    df = pd.DataFrame(results)
    df.to_excel(query + ".xlsx", index=False)


def main():
    current_url = login_amz()
    results = []
    query = input("Enter Keyword: ")
    page_number = int(input("How many page do you want to scrape?: "))
    for x in range (1, page_number):
        print(f"getting page {x}")
        urls = get_product_links(x, query, current_url)
        for url in urls:
            # print(parse_product(url))
            results.append(parse_product(url))
        print("Total results: ", len(results))
        save_CSV(results, query)
        print("save to CSV success!!")
        save_XLX(results, query)
        print("save to XLX success!!")  


if __name__ == "__main__":
    main()
