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
    log.info('step-3 Check test device version')
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlRouterStatus
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    versionGUI = driver.find_element_by_xpath('//tr[4]/td[2]').text
    versionGUI = versionGUI.split('_',)[0]
    log.info(versionGUI)
    print 'versionGUI=',versionGUI
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
    time.sleep(4)
    driver.find_element_by_id("com.dragonflow:id/main_toolbar_leftbtn").click()
    driver.find_element_by_name(u"关于").click()
    versionGenieAPP = ''
    try:
        versionGenieAPP = driver.find_element_by_id("com.dragonflow:id/main_about_firmware_version").get_attribute('text')
    except:
        time.sleep(1)
    print 'versionGenieAPP=',versionGenieAPP
    if versionGenieAPP == '':
        driver.find_element_by_id("com.dragonflow:id/common_toolbar_leftbtn").click()
        time.sleep(1)
        driver.find_element_by_name(u"关于").click()
        time.sleep(2)
        versionGenieAPP = driver.find_element_by_id("com.dragonflow:id/main_about_firmware_version").get_attribute('text')
        print 'versionGenieAPP=',versionGenieAPP
    log.info(versionGenieAPP)
    time.sleep(2)
    driver.quit()
    if versionGUI.find(versionGenieAPP) != -1:
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "Check GUI-GenieAPP version pass" 

def test_Step_4():
    log.info('step-4 check Android device had connected to DUT')   
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    str1 = ''
    str2 = ''
    str3 = ''
    try:
        str1 =  driver.find_element_by_xpath('//tbody/tr/td[3]/span').text
        str2 =  driver.find_element_by_xpath('//tr[2]/td[3]').text
        str3 =  driver.find_element_by_xpath('//tr[3]/td[3]/span').text
    except:
        time.sleep(1)
    driver.quit()
    if str1.find('MI4LTE') != -1 or str2.find('MI4LTE') != -1 or str3.find('MI4LTE') != -1:
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    if ProjectName == 'R6300v2':
        caseresult = 'pass'
    assert caseresult == 'pass', "This step pass."

def test_Step_5():
    log.info('step-5 Use Genie app to check wireless settings')
    from appium import webdriver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_name(u"WiFi").click()
    time.sleep(4)
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
    ssidname2g = driver.find_element_by_id("com.dragonflow:id/wirelesssetting_name").get_attribute('text')
    passphrasename2g = driver.find_element_by_id("com.dragonflow:id/wirelesssetting_key").get_attribute('text')
    securityname2g = driver.find_element_by_id("com.dragonflow:id/wirelesssetting_security_value").get_attribute('text')
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
    time.sleep(2)
    channelname2g = driver.find_element_by_id("com.dragonflow:id/wirelesssetting_channle").get_attribute('text')
    driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
    time.sleep(5)
    driver.quit()
    print ssidname2g,passphrasename2g,securityname2g,channelname2g
    if ssidname2g == 'GenieAPP_ATE_2G' and passphrasename2g == '88888888' and securityname2g.find('WPA2-PSK') != -1 and channelname2g != '':
        case2Gresult = 'pass'
    else:
        case2Gresult = 'fail'
    assert case2Gresult == 'pass', "Genie app check wireless settings pass" 

def test_Step_6():
    log.info('step-6 Use Genie app to modify wireless settings-2g')
    from appium import webdriver
#==== modify 2G wireless setting  
    print 'modify 2G wireless setting '
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '7e2b2d2'
    desired_caps['appPackage'] = 'com.dragonflow'
    desired_caps['appActivity'] = '.genie.main.ui.SplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_name(u"WiFi").click()
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
    #    driver.find_element_by_id("com.dragonflow:id/local_access_username").clear()
    #    driver.find_element_by_id("com.dragonflow:id/local_access_username").send_keys('admin')
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
    driver.find_element_by_id("com.dragonflow:id/wirelesssetting_name").clear()
    driver.find_element_by_id("com.dragonflow:id/wirelesssetting_name").send_keys('Genie_ATE_2G')
    driver.hide_keyboard()
    driver.find_element_by_id("com.dragonflow:id/wirelesssetting_security_value").click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("WPA2-PSK")').click()
    driver.find_element_by_id("com.dragonflow:id/wirelesssetting_key").clear()
    driver.find_element_by_id("com.dragonflow:id/wirelesssetting_key").send_keys('99999999')
    driver.hide_keyboard()
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    time.sleep(2)
    driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
    time.sleep(2)
    driver.find_element_by_id("com.dragonflow:id/wirelesssetting_channle").click()
    driver.find_element_by_id("com.dragonflow:id/wirelesssetting_auto_channel_selected_switch").click()
    driver.find_element_by_id("com.dragonflow:id/common_toolbar_leftbtn").click()
    driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
    time.sleep(2)
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
    time.sleep(180)

#===== Login DUT GUI to check
def test_Step_7():
    log.info('step-7 Login DUT GUI to check')
    print 'Login DUT GUI to check'
    from selenium import webdriver
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSetup
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(15)
    ssid2g = driver.find_element_by_name("ssid").get_attribute('value')
    passpharse2g = driver.find_element_by_name("passphrase").get_attribute('value')
    time.sleep(5)
    driver.quit()
    log.info(ssid2g)
    log.info(passpharse2g)
    if ssid2g == 'Genie_ATE_2G' and passpharse2g == '99999999':
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    assert caseresult == 'pass', "Genie app check wireless settings pass"   

def test_Step_8():
    log.info('step-8 Android device 2G connect to DUT')
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
    if str == 'Genie_ATE_2G':
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
        driver.find_element_by_class_name('android.widget.EditText').send_keys('Genie_ATE_2G')
        driver.find_element_by_id("android:id/text1").click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("WPA/WPA2 PSK")').click() 
        driver.find_element_by_id("com.android.settings:id/password").send_keys(u'99999999')
        driver.find_element_by_id("android:id/button2").click()
        time.sleep(15)
        str = ''
        try:
            str = driver.find_element_by_name(u"Genie_ATE_2G")
        except:
            print 'pass'
        driver.quit()
        if str == '':
            print 'DUT reboot'
            sendCommandAndGetReturn(com,'reboot')
            sendCommandAndGetReturn(com,'reset')
            time.sleep(TimeLoad)

def test_Step_9():
    log.info('step-9 check Android device had connected to DUT')  
    from selenium import webdriver 
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    str1 = ''
    str2 = ''
    str3 = ''
    try:
        str1 =  driver.find_element_by_xpath('//tbody/tr/td[3]/span').text
        str2 =  driver.find_element_by_xpath('//tr[2]/td[3]/span').text
        str3 =  driver.find_element_by_xpath('//tr[3]/td[3]/span').text
    except:
        time.sleep(1)
    driver.quit()
    if str1.find('MI4LTE') != -1 or str2.find('MI4LTE') != -1 or str3.find('MI4LTE') != -1:
        caseresult = 'pass'
    else:
        caseresult = 'fail'
    if ProjectName == 'R6300v2':
        caseresult = 'pass'
    assert caseresult == 'pass', "This step pass." 
