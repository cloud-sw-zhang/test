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
        time.sleep(65)
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
    log.info('step-3 Use Genie app to check Network Map')
    print 'Use Genie app to check Network Map'
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlRouterStatus
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    versionGUI = driver.find_element_by_xpath('//tr[4]/td[2]').text
    versionGUI = versionGUI.split('_',)[0]
    MacGUI = driver.find_element_by_xpath('//tr[10]/td[2]').text
    DeviceGUI = driver.find_element_by_xpath('//tr[2]/td[2]').text
    log.info(versionGUI)
    log.info(MacGUI)
    log.info(DeviceGUI)
    print versionGUI
    print MacGUI
    print DeviceGUI
    driver.quit()
    time.sleep(2)
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_name(u"网络地图").click()
    time.sleep(28)
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
    driver.tap([(450,990),(640,1000)],500)
    time.sleep(2)
    driver.tap([(300,700),(800,800)],500)
    time.sleep(2)
    Devicename = ''
    Typename = ''
    Ipaddress = ''
    MacAddress = ''
    try:
        Devicename = driver.find_element_by_id("com.dragonflow:id/device_detail_customName").get_attribute('text')
        Typename = driver.find_element_by_id("com.dragonflow:id/device_detail_typename").get_attribute('text')
        Ipaddress = driver.find_element_by_id("com.dragonflow:id/device_detail_ipaddress").get_attribute('text')
        MacAddress = driver.find_element_by_id("com.dragonflow:id/device_detail_mac_address").get_attribute('text')
    except:
        print 'pass'
    print Devicename,Ipaddress,MacAddress
    if MacGUI.find(MacAddress) != -1 and DeviceGUI.find(Devicename) != -1 and Typename == u'路由器' and Ipaddress == hostip:
        caseresult1 = 'pass'
    else:
        caseresult1 = 'fail'
    print 'caseresult1=',caseresult1
    time.sleep(10)
    driver.find_element_by_id("com.dragonflow:id/common_toolbar_leftbtn").click()
    time.sleep(2)
    driver.tap([(690,1470),(820,1560)],500)
    time.sleep(2)
    driver.tap([(400,1370),(830,1510)],500)
    time.sleep(2)
    AndroidDevicename = ''
    AndroidIpaddress = ''
    AndroidSignalStrength = ''
    AndroidDatarate = ''
    AndroidMacAdress = ''
    try:
        AndroidDevicename = driver.find_element_by_id("com.dragonflow:id/device_detail_customName").get_attribute('text')
        AndroidIpaddress = driver.find_element_by_id("com.dragonflow:id/device_detail_ipaddress").get_attribute('text')
        AndroidSignalStrength = driver.find_element_by_id("com.dragonflow:id/device_detail_signal_strength").get_attribute('text')
        AndroidDatarate = driver.find_element_by_id("com.dragonflow:id/device_detail_link_rate").get_attribute('text')
        AndroidMacAdress = driver.find_element_by_id("com.dragonflow:id/device_detail_mac_address").get_attribute('text')
    except:
        print 'pass'
    driver.quit()
    print AndroidDevicename,AndroidIpaddress,AndroidSignalStrength,AndroidDatarate,AndroidMacAdress
    if AndroidDevicename.find('MI4LTE') != -1 or AndroidDevicename.find('4LTE_e2b2d2') != -1 and AndroidIpaddress.find('192.168.') != -1 and AndroidSignalStrength.find('%') != -1 and AndroidDatarate.find('N/A') != -1 and  AndroidMacAdress == "74:51:BA:65:04:DB":
        caseresult2 = 'pass'
    elif AndroidDevicename.find('MI4LTE') != -1 or AndroidDevicename.find('4LTE_e2b2d2') != -1 and AndroidIpaddress.find('192.168.') != -1 and AndroidSignalStrength.find('%') != -1 and AndroidDatarate.find('Mbps') != -1 and  AndroidMacAdress == "74:51:BA:65:04:DB":
        caseresult2 = 'pass'
    else:
        caseresult2 = 'fail'
    print 'caseresult2=',caseresult2
    if caseresult1 == 'pass' and caseresult2 == 'pass':
        caseresult = 'pass'
    else:
        caseresult = 'fail'    
    assert caseresult == 'pass', "Use Genie app to check Network Map pass" 

def test_Step_4():
    log.info('step-4 Change LAN IP in GUI')
    global hostip
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlLANSetup
    print hostip
    if hostip == '192.168.1.1':
        changeip = '0'
    else:
        changeip = '1'
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_name("sysLANIPAddr3").clear()
    driver.find_element_by_name("sysLANIPAddr3").send_keys(changeip)
    time.sleep(1)
    driver.find_element_by_name("dhcp_server").click()
    driver.find_element_by_name("dhcp_server").click()
    driver.find_element_by_name("action").click()
    time.sleep(10)
    driver.quit()
    hostip = '192.168.' + changeip + '.1'
    time.sleep(TimeLoad)

def test_Step_5():
    log.info('step-5 Use Genie app to check Network Map again')
    print 'step-5 Genie app to check Network Map again'
    print hostip
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlRouterStatus
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    versionGUI = driver.find_element_by_xpath('//tr[4]/td[2]').text
    versionGUI = versionGUI.split('_',)[0]
    MacGUI = driver.find_element_by_xpath('//tr[10]/td[2]').text
    DeviceGUI = driver.find_element_by_xpath('//tr[2]/td[2]').text
    log.info(versionGUI)
    log.info(MacGUI)
    log.info(DeviceGUI)
    print versionGUI
    print MacGUI
    print DeviceGUI
    driver.quit()
    time.sleep(2)
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_name(u"网络地图").click()
    time.sleep(18)
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
    driver.tap([(450,990),(640,1000)],500)
    time.sleep(2)
    driver.tap([(300,700),(800,800)],500)
    time.sleep(2)
    Devicename = ''
    Typename = ''
    Ipaddress = ''
    MacAddress = ''
    try:
        Devicename = driver.find_element_by_id("com.dragonflow:id/device_detail_customName").get_attribute('text')
        Typename = driver.find_element_by_id("com.dragonflow:id/device_detail_typename").get_attribute('text')
        Ipaddress = driver.find_element_by_id("com.dragonflow:id/device_detail_ipaddress").get_attribute('text')
        MacAddress = driver.find_element_by_id("com.dragonflow:id/device_detail_mac_address").get_attribute('text')
        time.sleep(8)
        driver.find_element_by_id("com.dragonflow:id/common_toolbar_leftbtn").click()
    except:
        print 'pass'
    print Devicename,Ipaddress,MacAddress
    if MacGUI.find(MacAddress) != -1 and DeviceGUI.find(Devicename) != -1 and Typename == u'路由器' and Ipaddress == hostip:
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    time.sleep(2)
    driver.quit()
    assert caseresult == 'pass', "Use Genie app to check Network Map pass" 

def test_Step_6():
    log.info('step-6 Use Genie app to enable/disable')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_name(u"网络地图").click()
    time.sleep(8)
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
    str1 = ''
    try:
        str1 = driver.find_element_by_id("com.dragonflow:id/textView").get_attribute('text')
        driver.find_element_by_id("com.dragonflow:id/nm_accesscontrol_enable").click()
    except:
        print 'pass'
    if str1 == u'访问控制':
        caseresult1 = 'pass'
    else:
        caseresult1 = 'fail'
    time.sleep(20)
    print 'caseresult1=',caseresult1
    driver.quit()
    time.sleep(TimeLoad)
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    str2 = driver.find_element_by_id("enable_acl").is_selected()
    if str2 == True:
        caseresult2 = 'pass'
    else:
        caseresult2 = 'fail'
    time.sleep(2)
    print 'caseresult2=',caseresult2
    driver.quit()
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_name(u"网络地图").click()
    time.sleep(8)
    try:
        str1 = ''
        str1 = driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").get_attribute('text')
        if str1 == u'关闭':
            driver.find_element_by_id("com.dragonflow:id/local_but_loginclose").click()
            time.sleep(2)
            driver.find_element_by_id("com.dragonflow:id/local_access_login").click()
    except:
        print 'pass'
    str3 = ''
    try:
        str3 = driver.find_element_by_id("com.dragonflow:id/local_access_login").get_attribute('text')
    except:
        print 'pass'
    if str3 == u'登录':  
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
        time.sleep(4)
    time.sleep(GenieWaitTime)
    driver.find_element_by_id("com.dragonflow:id/nm_accesscontrol_enable").click()
    time.sleep(20)
    driver.quit()
    time.sleep(TimeLoad)
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    str4 = driver.find_element_by_id("enable_acl").is_selected()
    if str4 == False:
        caseresult3 = 'pass'
    else:
        caseresult3 = 'fail'
    time.sleep(2)
    print 'caseresult3=',caseresult3
    driver.quit()
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' 
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_name("logout").click()
    driver.quit()
    if caseresult1 == 'pass' and caseresult2 == 'pass' and caseresult3 == 'pass':
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "Use Genie app to check Network Map pass" 

def test_Step_7():
    log.info('step-7 Android device can open browser longin DUT')
    from appium import webdriver
    print hostip
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'org.mozilla.firefox'
    desired_caps['appActivity'] = '.App'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_id("org.mozilla.firefox:id/url_bar_title").click() 
    url = 'http://admin:Password!@' + hostip + '/'
    print url
    driver.find_element_by_id("org.mozilla.firefox:id/url_bar_translating_edge").send_keys(url)
    driver.press_keycode(66)
    time.sleep(2)
    str = ''
    try:
        str = driver.find_element_by_id("android:id/button1").get_attribute('text')
    except:
        print 'pass'  
    if str == u'确定':
        driver.find_element_by_id("android:id/button1").click()
    time.sleep(15)    
    driver.get_screenshot_as_file('F:\\ATE_script\\GenieApp_test\\buffer\\netgearhome.png')
    driver.quit()
    if hostip == '192.168.1.1':
        image1 = Image.open("F:\\ATE_script\\GenieApp_test\\buffer\\netgearhome_SPEC1.png")
    else:
        image1 = Image.open("F:\\ATE_script\\GenieApp_test\\buffer\\netgearhome_SPEC2.png")
    image2 = Image.open("F:\\ATE_script\\GenieApp_test\\buffer\\netgearhome.png") 
    h1 = image1.histogram() 
    h2 = image2.histogram() 
    result = math.sqrt(reduce(operator.add, list(map(lambda a,b:(a-b)**2,h1,h2))))
    print result
    if result < 300000:
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "This case step pass"   
