'''[PSV-2017-2451] Command injection when change Device Name '''
''' anthor Cloud 2017-12-12'''
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
    log.info("step-1 UUT will suffer command injection when config device name as $(utelnetd) or $(telnetd).")
    if ProjectName == 'R8000':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlLANSetup
    elif ProjectName == 'R6700' or ProjectName == 'R7000P' or ProjectName == 'R6900' or ProjectName == 'Orbi':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDeviceName
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlLANSetup
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(15)
    str = ''
    try:
        str = driver.find_element_by_name("device_name")
    except:
        time.sleep(1)
    if str != '':
        driver.find_element_by_name("device_name").clear()
        driver.find_element_by_name("device_name").send_keys('$(utelnetd)')
    else:
        driver.find_element_by_name("system_name").clear()
        driver.find_element_by_name("system_name").send_keys('$(utelnetd)')
    # if ProjectName == 'R6700' or ProjectName == 'R7000P':
        # driver.find_element_by_name("device_name").clear()
        # driver.find_element_by_name("device_name").send_keys('$(utelnetd)')
    # else:
        # driver.find_element_by_name("system_name").clear()
        # driver.find_element_by_name("system_name").send_keys('$(utelnetd)')
    try:
        driver.find_element_by_name("Apply").click()
        driver.find_element_by_xpath("//div[3]/input").click()
    except:    
        print('###############')
    time.sleep(5)
    driver.quit()

def test_Step_2():
    log.info( 'step-2 check telnet dut')
    str2 = judjeduttelnet()  
    if str2 == 'pass':
        log.info(str2)
        log.info( "check telnet dut pass")
        time.sleep(1)
    else:
        log.info(str2)
        log.info( "check telnet dut fail")
    assert str2 == 'pass', "This action should work." 

def test_Step_3():
    log.info( 'step-3 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 