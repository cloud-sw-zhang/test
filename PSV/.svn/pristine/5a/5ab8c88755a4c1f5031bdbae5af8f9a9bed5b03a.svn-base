''' [PSV-2017-0342] Stored XSS at usb_adv.cgi    '''
''' anthor Cloud 2017-12-08'''
'''v1.0 '''
from API._API import *

#def test_step_0():
    #log.info( 'step-0-0 dut loaddrfault wait 160s')
    #aploaddefault()
    #log.info( "step-0-1 AP Genie over leap done")
    #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 set usb readyshare group name ">>"<img src=x onerror=alert(25)>" ,check dut will reject')
    url = host + urlLogs
    token = getIDToken(url)
    if ProjectName == 'R6700' or ProjectName == 'R7000P' or ProjectName == 'R6900' or ProjectName == 'Orbi':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDeviceName
    elif ProjectName == 'R6300v2' or ProjectName == 'V6510' or ProjectName == 'WNR3500Lv2' or ProjectName == 'VEGN2610' or ProjectName == 'R6250' or ProjectName == 'DGN2200v4' or ProjectName == 'DC112A':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USB_adv_main.htm'
    elif console_type == 'cable':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USBAdvRetail.htm'
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/USB_adv_tab.htm'
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(15)
    str = ''
    try:
        str = driver.find_element_by_name("deviceName")
    except:
        time.sleep(1)
    if str == '':
        driver.find_element_by_name("device_name").clear()
        driver.find_element_by_name("device_name").send_keys('''>'>\"<img src=x onerror=alert(25)>''')
    else:
        driver.find_element_by_name("deviceName").clear()
        driver.find_element_by_name("deviceName").send_keys('''>'>\"<img src=x onerror=alert(25)>''')
    if ProjectName == 'R6700' or ProjectName == 'R7000P':
        driver.find_element_by_xpath("//div[3]/input").click()
    else:
        try:
            sec = driver.switch_to.alert
            sec.accept()
        except:
            time.sleep(2)
    time.sleep(25)
    if str == '':
        devicename = driver.find_element_by_name("device_name").get_attribute('value')
    else:
        devicename = driver.find_element_by_name("deviceName").get_attribute('value')
    driver.quit()   
    assert devicename != '''>'>\"<img src=x onerror=alert(25)>''', "This action should work." 
