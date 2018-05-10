#coding=utf-8
''' Genie test with Android '''
''' anthor Cloud 2018-03-13'''
'''v1.0 '''
from API._API import *
def test_Step_0():
    log.info('step-0 ADB push test1.txt to Android device')
    cmd = '"adb.exe" push F:\\ATE_script\\GenieApp_test\\buffer\\test1.txt sdcard/'
    os.system(cmd)

def test_Step_1():
    log.info('step-1 Set DUT wireless ssid channel security')
    from selenium import webdriver
    from selenium.webdriver.support.select import Select 
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSetup
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_name("ssid").clear()
    driver.find_element_by_name("ssid").send_keys('GenieAPP_ATE_2G')
    sel1 = driver.find_element_by_name("w_channel")
    Select(sel1).select_by_value("6")
    if ProjectName == 'R8500' or ProjectName == 'R8000':
        try:
            driver.find_element_by_xpath('//tr[12]/td/input').click()
        except:
            time.sleep(1)
    else:
        try:
            driver.find_element_by_xpath('//tr[17]/td/input').click()
        except:
            time.sleep(1)
    try:
        str = driver.switch_to.alert
        str.accept()
    except:
        time.sleep(1)
    driver.find_element_by_name("passphrase").clear()
    driver.find_element_by_name("passphrase").send_keys('88888888')
    if ProjectName == 'R6300v2':
        driver.find_element_by_name("passphrase_an").clear()
        driver.find_element_by_name("passphrase_an").send_keys('88888888')
    driver.find_element_by_name("Apply").click()
    try:
        str = driver.switch_to.alert
        str.accept()
    except:
        time.sleep(1)
    time.sleep(15)
    driver.quit()

def test_Step_2_1():
    log.info('step-2-1 disable wireless 5G enbale')
    from selenium import webdriver
    from selenium.webdriver.support.select import Select 
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSettings
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    str2g = driver.find_element_by_name("enable_ap").is_selected()
    str5g = driver.find_element_by_name("enable_ap_an").is_selected()
    if str2g == False:
        driver.find_element_by_name("enable_ap").click()
        if str5g == True:
            driver.find_element_by_name("enable_ap_an").click()
        driver.find_element_by_name("Apply").click()
        time.sleep(5)
        driver.quit()
        time.sleep(160)
    else:    
        if str5g == True:
            driver.find_element_by_name("enable_ap_an").click()
            driver.find_element_by_name("Apply").click()
            time.sleep(5)
            driver.quit()
            time.sleep(160)
        else:
            time.sleep(5)
            driver.quit()

def test_Step_2():
    log.info('step-2 Android device 2G connect to DUT')
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
    if str == 'GenieAPP_ATE_2G':
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
        driver.find_element_by_class_name('android.widget.EditText').send_keys('GenieAPP_ATE_2G')
        driver.find_element_by_id("android:id/text1").click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("WPA/WPA2 PSK")').click() 
        driver.find_element_by_id("com.android.settings:id/password").send_keys(u'88888888')
        driver.find_element_by_id("android:id/button2").click()
        time.sleep(15)
        str = ''
        try:
            str = driver.find_element_by_name(u"GenieAPP_ATE_2G")
        except:
            print 'pass'
        driver.quit()
        if str == '':
            sendCommandAndGetReturn(com,'reboot')
            sendCommandAndGetReturn(com,'reset')
            time.sleep(TimeLoad)

def test_Step_3():
    log.info('step-3 Del test1.txt in DUT USBStorage')
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
        driver.find_element_by_name(u"ReadySHARE").click()
        driver.find_element_by_name(u"ReadySHARE").click()
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
        time.sleep(8)
    time.sleep(GenieWaitTime)
    driver.tap([(540,228),(1080,372)],500)
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/file_ico").click()
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/common_toolbar_rightbtn").click()
    time.sleep(2)
    driver.tap([(660,860),(950,900)],500)
    try:
        driver.find_element_by_name(u"test1.txt").click()
        driver.find_element_by_id("com.dragonflow:id/menuitem_upordownload").click()
    except:
        print 'pass'
    str = ''
    try:
        str = driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").get_attribute('text')
    except:
        print 'pass'
    time.sleep(5)
    if str == u'确定':
        driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").click()
        driver.quit()
    else:
        driver.quit()

def test_Step_4():
    log.info('step-4 Upload file from Android to DUT USBStorage')
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
        driver.find_element_by_name(u"ReadySHARE").click()
        driver.find_element_by_name(u"ReadySHARE").click()
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
        time.sleep(8)
    time.sleep(GenieWaitTime)
    driver.tap([(0,228),(540,372)],500)
    time.sleep(2)
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    str = ''
    for i in range(1,20):
        driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/common_toolbar_rightbtn").click()
    time.sleep(2)
    driver.tap([(660,570),(950,600)],500)
    time.sleep(2)
    driver.find_element_by_name(u"test1.txt").click()
    driver.find_element_by_id("com.dragonflow:id/menuitem_upordownload").click()
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/file_ico").click()
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/pastebar_save").click()
    time.sleep(8)
    str = ''
    try:
        str = driver.find_element_by_name(u"test1.txt").get_attribute('text')
    except:
        print 'pass'
    driver.quit()
    if str == u'test1.txt':
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "Upload file from Android to DUT USBStorage pass"

def test_Step_5():
    log.info('step-5 Del test1.txt from Android device')
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
        driver.find_element_by_name(u"ReadySHARE").click()
        driver.find_element_by_name(u"ReadySHARE").click()
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
        time.sleep(8)
    time.sleep(GenieWaitTime)
    driver.tap([(0,228),(540,372)],500)
    time.sleep(3)
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    for i in range(1,20):
        driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/common_toolbar_rightbtn").click()
    time.sleep(2)
    driver.tap([(660,860),(950,900)],500)
    time.sleep(2)
    driver.find_element_by_name(u"test1.txt").click()
    driver.find_element_by_id("com.dragonflow:id/menuitem_upordownload").click()
    try:
        str = driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").get_attribute('text')
    except:
        print 'pass'
    if str == u'确定':
        time.sleep(2)
        driver.find_element_by_id("com.dragonflow:id/common_msgdialog_button3").click()
        time.sleep(2)
        driver.quit()
    else:
        driver.quit()

def test_Step_6():
    log.info('step-6 Download file from DUT USBStorage to Android')
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
        driver.find_element_by_name(u"ReadySHARE").click()
        driver.find_element_by_name(u"ReadySHARE").click()
    except:
        print 'pass'
    driver.tap([(540,228),(1080,372)],500)
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/file_ico").click()
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/common_toolbar_rightbtn").click()
    time.sleep(2)
    driver.tap([(660,570),(950,600)],500)
    time.sleep(2)
    driver.find_element_by_name(u"test1.txt").click()
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/menuitem_upordownload").click()
    time.sleep(2)
    driver.tap([(0,228),(540,372)],500)
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/pastebar_save").click()
    time.sleep(8)
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    for i in range(1,20):
            driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
    str = ''
    try:
        str = driver.find_element_by_name(u"test1.txt").get_attribute('text')
    except:
        print 'pass'
    time.sleep(2)
    driver.quit()
    if str == u'test1.txt':
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "Download file from DUT USBStorage to Android"
