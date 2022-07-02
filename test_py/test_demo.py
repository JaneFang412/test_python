import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        #加入cookie不使用浏览器复用
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

    def teardwon_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get("https://home.testing-studio.com/")
        # self.driver.find_element(By.LINK_TEXT, "热门").click()
        # self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False,
        #      'value': 'true'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
        #      'value': ''},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688858065321371'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970326652979838'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688858065321371'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '4354901040'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a8378616'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '9351611473381564'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'mVws8Umlak4pMEVW498ZLJscp67MboJ6DRtmZpreTaivA5B-iQ7Or2xK6SQQwPUg'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1681721781, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': '0N8Tya6n-c08DMDwfXS9nk-Kjs8aRxs4JCcWlkrASAe_zSqRd6rtAGSxFy7_-nZPUDyVdnbgxIubgDeh5bGIIWJcrlsg_V5Xu2aoGCeHq-O8XzkrmcGDT7A5s3q2ZctPh_toTmnhuQgTomHVfSG4UAVUWKdm9Bua-e-FGmzjFCx-x2r7ke0m3pPdczUB3CJJL9aW6fNFAZ7LP_RBXZdEldo9Ko-lpHF1F_BNOn7Vx4-B40S5IqgH62mU7Qdd98at9fNcNRzvacSdm6mlBuHniQ'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1652778869, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'}]
        #在一个打开的浏览器页面get这个页面的cookies,并打印
        # print(self.driver.get_cookies())
        #加入cookie前先要访问页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #上面获取的cookies信息太多，放在代码中不方便，可以把获取的cookies信息存放在shelve数据库中，python自带小型数据库
        #此时可以使用浏览器复用
        #运行成功后会在当前目录下生成三个文件cookies.bak, cookies.dat, cookies.dir
        db = shelve.open("cookies")
        #把页面上的cookies保存在db中
        # db['cookie'] = self.driver.get_cookies()
        #db中存储了cookies,现在取出cookies
        cookies = db['cookie']
        #把获取的cookies设置成变量cookies,然后循环取出每一个cookie,把每个cookie在打开浏览器后再加入，就可以不用登录而能自动登录了
        #在获取的ecookies中如果expiry变量对应的值存在小数有可能报错，处理方法是把expiry从数组中删掉
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        #加入cookie后再进行访问
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)
        db.close()