# 获取cookies 到本地
def get_cookies(url,driver):
    driver.get(url)
    time.sleep(20)  # 留时间进行扫码
    Cookies = driver.get_cookies()  # 获取list的cookies
    jsCookies = json.dumps(Cookies)  # 转换成字符串保存
    with open('cookies.txt', 'w') as f:
        f.write(jsCookies)
    print('cookies已重新写入！')


# 读取本地的cookies
def read_cookies(domain):
    with open('cookies.txt', 'r', encoding='utf8') as f:
        Cookies = json.loads(f.read())
    cookies = []
    for cookie in Cookies:
        cookie_dict = {
            'domain': domain,
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            'expires': '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        cookies.append(cookie_dict)
    return cookies

def set_cookie(driver,domain):
    cookies = read_cookies(domain)
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(3)
    driver.refresh()  # 刷新网页

    return driver