'''	[PSV-2017-2454] Security questions allows plain password recovery '''
''' anthor Cloud 2018-01-03'''
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
    log.info("step-1 Admin password shouldn't be obtained even security questions are known.")
    log.info('Get Serial number')
    if console_type == 'cable':
        driver = webdriver.Firefox()
        httpurl = "http://" + user + ':' + passwd + "@" + hostip + '/SetPassword.htm'
        driver.get(httpurl)
        time.sleep(15)
        str = driver.page_source
        driver.quit()
        str1 = re.findall(r"var tagValueList = (.+?);",str)
        a = str1[0].split('|',)
        answer1 = a[3]
        answer2 = a[5]
    else:
        sendCommandAndGetReturn('com1',console_type + ' set enable_password_recovery=1')
        sendCommandAndGetReturn('com1',console_type + ' save')
        url = host + urlLogs
        token = getIDToken(url)
        str = sendCommandAndGetReturn(com,'burnsn')
        sn = str.split()[4]
    driver = webdriver.Firefox()
    httpurl = "http://" + hostip + '/MNU_access_unauthorized_checkSerial.htm'
    if console_type == 'cable':
        httpurl = "http://" + hostip + '/PwdRec_checkserial.htm'
        sn = 'BTA17C78A003B'
    driver.get(httpurl)
    log.info(sn)
    time.sleep(15)
    try:
        sec = driver.switch_to.alert
        sec.dismiss()
    except:
        time.sleep(2)
    if console_type == 'cable':
        driver.find_element_by_name("insert_serial").send_keys(sn)
    else:
        driver.find_element_by_name("serialNumber").send_keys(sn)
    time.sleep(5)
    driver.find_element_by_name("Continue").click()
    time.sleep(5)
    if console_type == 'cable':
        driver.find_element_by_name("insert_answer1").send_keys(answer1)
        driver.find_element_by_name("insert_answer2").send_keys(answer2)
    else:
        driver.find_element_by_name("answer1").send_keys('1')
        driver.find_element_by_name("answer2").send_keys('1')
    driver.find_element_by_name("Continue").click()
    time.sleep(5)
    try:
        sec = driver.switch_to.alert
        sec.dismiss()
    except:
        time.sleep(2)
    str = driver.page_source
    driver.quit()
    log.info(str)
    if console_type == 'cable':
        if str.find('admin') != -1 and str.find('password') != -1:
            case = 'fail'
        else:
            case = 'pass'
    else:
        if str.find('admin') != -1 and str.find('Password!') != -1:
            case = 'fail'
        else:
            case = 'pass'
    assert case == 'pass', "This action should not work." 
