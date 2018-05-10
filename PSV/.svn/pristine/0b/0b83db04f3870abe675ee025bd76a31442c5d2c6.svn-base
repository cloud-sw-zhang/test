#coding=utf-8
''' Genie test with Android '''
''' anthor Cloud 2018-03-13'''
'''v1.0 '''
from API._API import *
def test_Step_1():
    log.info('step-1 Set DUT wireless ssid channel security')
    from selenium import webdriver
    from selenium.webdriver.support.select import Select 
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSetup
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    if ProjectName == 'R6300v2':
        driver.find_element_by_name("passphrase").clear()
        driver.find_element_by_name("passphrase").send_keys('88888888')
    if ProjectName == 'R7900' or ProjectName == 'R8500' or ProjectName == 'R8000':
        try:
            driver.find_element_by_name('enable_5g_band_steering').click()
            str = driver.switch_to.alert
            str.accept()
        except:
            time.sleep(1)
    driver.find_element_by_name("ssid_an").clear()
    driver.find_element_by_name("ssid_an").send_keys('GenieAPP_ATE_5G')
    sel3 = driver.find_element_by_name("w_channel_an")
    Select(sel3).select_by_value("36")
    try:
        str = driver.switch_to.alert
        str.accept()
    except:
        time.sleep(1)
    # sel4 = driver.find_element_by_name("opmode_an")
    # Select(sel4).select_by_value("300Mbps")
    driver.find_element_by_id("5gAes").click()
    driver.find_element_by_name("passphrase_an").clear()
    driver.find_element_by_name("passphrase_an").send_keys('88888888')
    driver.find_element_by_name("Apply").click()
    try:
        str = driver.switch_to.alert
        str.accept()
    except:
        time.sleep(1)
    time.sleep(25)
    driver.quit()

def test_Step_2_1():
    log.info('step-2-1 disable wireless 2G enbale')
    from selenium import webdriver
    from selenium.webdriver.support.select import Select 
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSettings
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)
    str2g = driver.find_element_by_name("enable_ap").is_selected()
    str5g = driver.find_element_by_name("enable_ap_an").is_selected()
    if str5g == False:
        driver.find_element_by_name("enable_ap_an").click()
        if str2g == True:
            driver.find_element_by_name("enable_ap").click()
        driver.find_element_by_name("Apply").click()
        time.sleep(2)
        driver.quit()
        time.sleep(160)
    else:    
        if str2g == True:
            driver.find_element_by_name("enable_ap").click()
            driver.find_element_by_name("Apply").click()
            time.sleep(2)
            driver.quit()
            time.sleep(160)
        else:
            time.sleep(2)
            driver.quit()

def test_Step_2():
    log.info('step-2 Android device 5G connect to DUT')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.MiuiSettings'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    str = driver.find_element_by_id("miui:id/value_right").get_attribute('text')
    if str == 'GenieAPP_ATE_5G':
        print 'device had connect DUT'
        driver.quit()
    else:
        print 'wireless open'
        driver.find_element_by_id("miui:id/value_right").click()
        time.sleep(2)
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        str = ''
        for i in range(1,20):
            driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
        time.sleep(2)
        driver.find_element_by_name(u"其他...").click()
        driver.activate_ime_engine('com.google.android.inputmethod.pinyin/.PinyinIME')
        driver.find_element_by_class_name('android.widget.EditText').send_keys('GenieAPP_ATE_5G')
        driver.find_element_by_id("android:id/text1").click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("WPA/WPA2 PSK")').click() 
        driver.find_element_by_id("com.android.settings:id/password").send_keys(u'88888888')
        driver.find_element_by_id("android:id/button2").click()
        time.sleep(15)
        str = ''
        try:
            str = driver.find_element_by_name(u"GenieAPP_ATE_5G")
        except:
            print 'pass'
        driver.quit()
        if str == '':
            sendCommandAndGetReturn(com,'reboot')
            sendCommandAndGetReturn(com,'reset')
            time.sleep(TimeLoad)

def test_Step_3():
    log.info('step-3 Enable Guest Access')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    try:
        driver.find_element_by_name(u"访客 WiFi").click()
        driver.find_element_by_name(u"访客 WiFi").click()
    except:
        print 'pass'
    try:
        str1 = ''
        str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
        if str1 == u'关闭':
            driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
            time.sleep(2)
            driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
    except:
        print 'pass'
    str = ''
    try:
        str = driver.find_element_by_id("com.dragonflow:id/local_access_login").get_attribute('text')
    except:
        print 'pass'
    try:
        str1 = ''
        str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
        if str1 == u'关闭':
            driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
            time.sleep(2)
            driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
    except:
        print 'pass'
    if str == u'登录':  
        driver.activate_ime_engine('com.google.android.inputmethod.pinyin/.PinyinIME')
      #  driver.find_element_by_id("com.dragonflow:id/local_access_username").clear()
      #  driver.find_element_by_id("com.dragonflow:id/local_access_username").send_keys('admin')
        driver.find_element_by_id("com.dragonflow:id/local_access_password").clear()
        driver.find_element_by_id("com.dragonflow:id/local_access_password").send_keys('Password!')
        driver.hide_keyboard()
        driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        time.sleep(2)
        try:
            str = ''
            str = driver.find_element_by_id("com.dragonflow:id/na_next_btn").get_attribute('text')
            if str == u'下一步':
                driver.find_element_by_id("com.dragonflow:id/noaccess_backbtn").click()
                time.sleep(2)
                driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        except:
            print 'pass' 
        try:
            str1 = ''
            str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
            if str1 == u'关闭':
                driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
                time.sleep(2)
                driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        except:
            print 'pass'
    time.sleep(GenieWaitTime)
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width * 3 / 4, height / 4, width / 16, height / 4, 500)
    time.sleep(GenieWaitTime)
    str = ''
    try:
        str = driver.find_element_by_id("com.dragonflow:id/guestsetting_switch_enable").get_attribute('text')
    except:
        print 'pass'  
    if str == u'关闭':
        driver.find_element_by_id("com.dragonflow:id/guestsetting_switch_enable").click()   
        print 'open Guest Acess'
        driver.find_element_by_id("com.dragonflow:id/common_toolbar_righttxt").click()
        str1 = ''
        try:
            str1 = driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").get_attribute('text')
        except:
            print 'pass'
        if str1 == u'确定':
            driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").click()
            time.sleep(10)
            driver.quit()
            time.sleep(160)
    else:
        print 'Guest Acess open'
        driver.quit()

def test_Step_4():
    log.info('step-4 Change the Guest Access SSID/Time Period/Security Options and click Apply')   
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    try:
        driver.find_element_by_name(u"访客 WiFi").click()
        driver.find_element_by_name(u"访客 WiFi").click()
    except:
        print 'pass'
    try:
        str1 = ''
        str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
        if str1 == u'关闭':
            driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
            time.sleep(2)
            driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
    except:
        print 'pass'
    str = ''
    try:
        str = driver.find_element_by_id("com.dragonflow:id/local_access_login").get_attribute('text')
    except:
        print 'pass'
    if str == u'登录':  
        driver.activate_ime_engine('com.google.android.inputmethod.pinyin/.PinyinIME')
      #  driver.find_element_by_id("com.dragonflow:id/local_access_username").clear()
      #  driver.find_element_by_id("com.dragonflow:id/local_access_username").send_keys('admin')
        driver.find_element_by_id("com.dragonflow:id/local_access_password").clear()
        driver.find_element_by_id("com.dragonflow:id/local_access_password").send_keys('Password!')
        driver.hide_keyboard()
        driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        time.sleep(2)
        try:
            str = ''
            str = driver.find_element_by_id("com.dragonflow:id/na_next_btn").get_attribute('text')
            if str == u'下一步':
                driver.find_element_by_id("com.dragonflow:id/noaccess_backbtn").click()
                time.sleep(2)
                driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        except:
            print 'pass' 
        try:
            str1 = ''
            str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
            if str1 == u'关闭':
                driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
                time.sleep(2)
                driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        except:
            print 'pass'
    time.sleep(GenieWaitTime)
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width * 3 / 4, height / 4, width / 16, height / 4, 500)
    time.sleep(GenieWaitTime)
    str = ''
    try:
        str = driver.find_element_by_id("com.dragonflow:id/guestsetting_switch_enable").get_attribute('text')
    except:
        print 'pass'  
    time.sleep(4)
    driver.activate_ime_engine('com.google.android.inputmethod.pinyin/.PinyinIME')
    driver.find_element_by_id("com.dragonflow:id/guestsettings_txt_ssid").clear()
    driver.find_element_by_id("com.dragonflow:id/guestsettings_txt_ssid").send_keys('GenieAPP_ATE_5G_Guest')
    driver.hide_keyboard()
    driver.find_element_by_id("com.dragonflow:id/guest_security_value").click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("WPA2-PSK")').click() 
    driver.find_element_by_id("com.dragonflow:id/guestsettings_txt_password").clear()
    driver.find_element_by_id("com.dragonflow:id/guestsettings_txt_password").send_keys(u'00000000')
    driver.hide_keyboard()
    driver.find_element_by_id("com.dragonflow:id/guestsettings_txt_timeperiod").click()
    #driver.find_element_by_android_uiautomator('new UiSelector().text(u"1 小时")').click() 
    driver.find_element_by_name(u"1 小时").click()
    driver.find_element_by_id("com.dragonflow:id/common_toolbar_righttxt").click()
    str1 = ''
    try:
        str1 = driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").get_attribute('text')
    except:
        print 'pass'
    if str1 == u'确定':
        driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").click()
        time.sleep(10)
        driver.quit()
        time.sleep(160)
    else:
        time.sleep(1)
        driver.quit()

def test_Step_5():
    log.info('step-5 Check Guest wireless settings in DUT GUI')
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlGuestNetwork5G
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(10)
    ssid5g = driver.find_element_by_name("ssid_an").get_attribute('value')
    passpharse5g = ''
    try:
        passpharse5g = driver.find_element_by_name("passphrase_an").get_attribute('value')
    except:
        print 'pass'
    status5g = driver.find_element_by_name("enable_bssid_an").is_selected()
    time.sleep(1)
    driver.quit()
    print ssid5g
    print passpharse5g
    print status5g
    log.info(ssid5g)
    log.info(passpharse5g)
    log.info(status5g)
    if ssid5g == 'GenieAPP_ATE_5G_Guest' and passpharse5g == '00000000' and status5g == True:
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "Genie app check wireless settings pass"

def test_Step_6_1():
    log.info('test_Step_1 Set DUT wireless 5G ssid')
    from selenium import webdriver
    from selenium.webdriver.support.select import Select 
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSetup
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_name("ssid_an").clear()
    driver.find_element_by_name("ssid_an").send_keys('000_test')
    driver.find_element_by_id("5gAes").click()
    driver.find_element_by_name("passphrase_an").clear()
    driver.find_element_by_name("passphrase_an").send_keys('88888888')
    driver.find_element_by_name("Apply").click()
    try:
        str = driver.switch_to.alert
        str.accept()
    except:
        time.sleep(1)
    time.sleep(35)
    driver.quit()

def test_Step_6():
    log.info('step-6 android device can connect to DUT with Guest Access settings')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.MiuiSettings'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    str = driver.find_element_by_id("miui:id/value_right").get_attribute('text')
    if str == 'GenieAPP_ATE_5G_Guest':
        print 'device had connect DUT'
        driver.quit()
    else:
        print 'wireless open'
        driver.find_element_by_id("miui:id/value_right").click()
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        str = ''
        for i in range(1,20):
            driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
        time.sleep(2)
        driver.find_element_by_name(u"其他...").click()
        driver.activate_ime_engine('com.google.android.inputmethod.pinyin/.PinyinIME')
        driver.find_element_by_class_name('android.widget.EditText').send_keys('GenieAPP_ATE_5G_Guest')
        driver.find_element_by_id("android:id/text1").click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("WPA/WPA2 PSK")').click() 
        driver.find_element_by_id("com.android.settings:id/password").send_keys(u'00000000')
        driver.find_element_by_id("android:id/button2").click()
        time.sleep(15)
        str = ''
        try:
            str = driver.find_element_by_name(u"GenieAPP_ATE_5G_Guest")
        except:
            print 'pass'
        driver.quit()
        if str == '':
            sendCommandAndGetReturn(com,'reboot')
            sendCommandAndGetReturn(com,'reset')
            time.sleep(TimeLoad)

def test_Step_7():
    log.info('step-7 On this device, access www.routerlogin.com, verify it will be blocked, access www.netgear.com, verify it can visit successfully')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'org.mozilla.firefox'
    desired_caps['appActivity'] = '.App'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)
    driver.find_element_by_id("org.mozilla.firefox:id/url_bar_title").click() 
    driver.find_element_by_id("org.mozilla.firefox:id/url_bar_translating_edge").send_keys('www.routerlogin.com')
    driver.press_keycode(66)
    time.sleep(5)
    driver.get_screenshot_as_file('F:\\ATE_script\\GenieApp_test\\buffer\\routerlogin1.png')
    time.sleep(2)
    driver.quit()
    time.sleep(2)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)
    driver.find_element_by_id("org.mozilla.firefox:id/url_bar_title").click() 
    driver.find_element_by_id("org.mozilla.firefox:id/url_bar_translating_edge").send_keys('www.netgear.com')
    driver.press_keycode(66)
    time.sleep(5)
    driver.get_screenshot_as_file('F:\\ATE_script\\GenieApp_test\\buffer\\netgear1.png')
    time.sleep(2)
    driver.quit()
    image1 = Image.open("F:\\ATE_script\\GenieApp_test\\buffer\\Routerlogin_SPEC.png")
    image2 = Image.open("F:\\ATE_script\\GenieApp_test\\buffer\\routerlogin1.png") 
    h1 = image1.histogram() 
    h2 = image2.histogram() 
    result1 = math.sqrt(reduce(operator.add, list(map(lambda a,b:(a-b)**2,h1,h2))))
    image3 = Image.open("F:\\ATE_script\\GenieApp_test\\buffer\\Routerlogin_SPEC.png")
    image4 = Image.open("F:\\ATE_script\\GenieApp_test\\buffer\\netgear1.png") 
    h3 = image3.histogram() 
    h4 = image4.histogram() 
    result2 = math.sqrt(reduce(operator.add, list(map(lambda a,b:(a-b)**2,h3,h4))))
    print result1,result2
    if result1 < 3000 and result2 > 20000:
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "This case step pass"

def test_Step_8():
    log.info('step-8 Run NETGEAR Genie app and login on this device, verify it can’t be login.')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    try:
        driver.find_element_by_name(u"访客 WiFi").click()
        driver.find_element_by_name(u"访客 WiFi").click()
    except:
        print 'pass'
    try:
        str1 = ''
        str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
        if str1 == u'关闭':
            driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
            time.sleep(2)
            driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
    except:
        print 'pass'
    str = ''
    try:
        str = driver.find_element_by_id("com.dragonflow:id/local_access_login").get_attribute('text')
    except:
        print 'pass'
    if str == u'登录':  
        driver.activate_ime_engine('com.google.android.inputmethod.pinyin/.PinyinIME')
      #  driver.find_element_by_id("com.dragonflow:id/local_access_username").clear()
      #  driver.find_element_by_id("com.dragonflow:id/local_access_username").send_keys('admin')
        driver.find_element_by_id("com.dragonflow:id/local_access_password").clear()
        driver.find_element_by_id("com.dragonflow:id/local_access_password").send_keys('Password!')
        driver.hide_keyboard()
        driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        time.sleep(2)
        try:
            str = ''
            str = driver.find_element_by_id("com.dragonflow:id/na_next_btn").get_attribute('text')
            if str == u'下一步':
                driver.find_element_by_id("com.dragonflow:id/noaccess_backbtn").click()
                time.sleep(2)
                driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        except:
            print 'pass' 
        try:
            str1 = ''
            str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
            if str1 == u'关闭':
                driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
                time.sleep(2)
                driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        except:
            print 'pass' 
    time.sleep(GenieWaitTime)
    str1 = ''
    try:
        str1 = driver.find_element_by_id("com.dragonflow:id/local_access_login").get_attribute('text')
    except:
        print 'pass'  
    driver.quit()
    time.sleep(30)
    if str1 == '':
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "This case step pass"

def test_Step_9_1():
    log.info('test_Step_9_1 Set DUT wireless 5G ssid')
    from selenium import webdriver
    from selenium.webdriver.support.select import Select 
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSetup
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_name("ssid_an").clear()
    driver.find_element_by_name("ssid_an").send_keys('GenieAPP_ATE_5G')
    driver.find_element_by_id("5gAes").click()
    driver.find_element_by_name("passphrase_an").clear()
    driver.find_element_by_name("passphrase_an").send_keys('88888888')
    driver.find_element_by_name("Apply").click()
    try:
        str = driver.switch_to.alert
        str.accept()
    except:
        time.sleep(1)
    time.sleep(65)
    driver.quit()

def test_Step_9():
    log.info('step-9 Android device 5G connect to DUT')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.MiuiSettings'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    str = driver.find_element_by_id("miui:id/value_right").get_attribute('text')
    if str == 'GenieAPP_ATE_5G':
        print 'device had connect DUT'
        driver.quit()
    else:
        print 'wireless open'
        driver.find_element_by_id("miui:id/value_right").click()
        time.sleep(2)
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        str = ''
        for i in range(1,20):
            driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
        time.sleep(2)
        driver.find_element_by_name(u"其他...").click()
        driver.activate_ime_engine('com.google.android.inputmethod.pinyin/.PinyinIME')
        driver.find_element_by_class_name('android.widget.EditText').send_keys('GenieAPP_ATE_5G')
        driver.find_element_by_id("android:id/text1").click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("WPA/WPA2 PSK")').click() 
        driver.find_element_by_id("com.android.settings:id/password").send_keys(u'88888888')
        driver.find_element_by_id("android:id/button2").click()
        time.sleep(15)
        str = ''
        try:
            str = driver.find_element_by_name(u"GenieAPP_ATE_5G")
        except:
            print 'pass'
        driver.quit()
        if str == '':
            sendCommandAndGetReturn(com,'reboot')
            sendCommandAndGetReturn(com,'reset')
            time.sleep(TimeLoad)

def test_Step_10():
    log.info('step-10 Run NETGEAR Genie app-select Disable Guest Access and click Apply')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    try:
        driver.find_element_by_name(u"访客 WiFi").click()
        driver.find_element_by_name(u"访客 WiFi").click()
    except:
        print 'pass'
    try:
        str1 = ''
        str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
        if str1 == u'关闭':
            driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
            time.sleep(2)
            driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
    except:
        print 'pass'
    str = ''
    try:
        str = driver.find_element_by_id("com.dragonflow:id/local_access_login").get_attribute('text')
    except:
        print 'pass'
    if str == u'登录':  
        driver.activate_ime_engine('com.google.android.inputmethod.pinyin/.PinyinIME')
      #  driver.find_element_by_id("com.dragonflow:id/local_access_username").clear()
      #  driver.find_element_by_id("com.dragonflow:id/local_access_username").send_keys('admin')
        driver.find_element_by_id("com.dragonflow:id/local_access_password").clear()
        driver.find_element_by_id("com.dragonflow:id/local_access_password").send_keys('Password!')
        driver.hide_keyboard()
        driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        time.sleep(2)
        try:
            str = ''
            str = driver.find_element_by_id("com.dragonflow:id/na_next_btn").get_attribute('text')
            if str == u'下一步':
                driver.find_element_by_id("com.dragonflow:id/noaccess_backbtn").click()
                time.sleep(2)
                driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        except:
            print 'pass' 
        try:
            str1 = ''
            str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
            if str1 == u'关闭':
                driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
                time.sleep(2)
                driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
        except:
            print 'pass'
    time.sleep(GenieWaitTime)
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width * 3 / 4, height / 4, width / 16, height / 4, 500)
    time.sleep(GenieWaitTime)
    str = ''
    try:
        str = driver.find_element_by_id("com.dragonflow:id/guestsetting_switch_enable").get_attribute('text')
    except:
        print 'pass'  
    if str == u'开启':
        driver.find_element_by_id("com.dragonflow:id/guestsetting_switch_enable").click()   
        print 'Close Guest Acess'
        time.sleep(10)
        driver.find_element_by_id("com.dragonflow:id/common_toolbar_righttxt").click()
        str1 = ''
        try:
            str1 = driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").get_attribute('text')
        except:
            print 'pass'
        if str1 == u'确定':
            driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").click()
            time.sleep(10)
            driver.quit()
            time.sleep(160)
    else:
        print 'Guest Acess Closed'
        driver.quit()

def test_Step_11():
    log.info('step-11 Check DUT Guest Access will be disabled')
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlGuestNetwork5G
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(10)
    status5g = driver.find_element_by_name("enable_bssid_an").is_selected()
    time.sleep(1)
    print status5g
    driver.quit()
    if status5g == False:
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "Genie app check wireless settings pass"
