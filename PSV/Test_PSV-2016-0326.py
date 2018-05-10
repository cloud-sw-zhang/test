'''[PSV-2017-0326] Unable to Clear HTTP Auth Header from browser - leads to account hijack  '''
''' anthor Cloud 2017-12-13'''
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
    log.info("step-1 DUT can be used symbolic link to retrieve other files in the system by readyshare ")
    url = host + urlLogs
    token = getIDToken(url)
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip
    driver.get(url)
    time.sleep(15)
    try:
        sec = driver.switch_to.alert
    except:
        time.sleep(1)
    try:
        sec.dismiss()
    except:
        time.sleep(1)
    str3 = sendCommandAndGetReturnUntil(com,'nvram show | grep https ','#')
    if str3.find('httpsEnable') != -1:
        driver.find_element_by_name("logout").click()
    driver.find_element_by_name("logout").click()
    time.sleep(5)
    driver.back()
    try:
        sec1 = driver.switch_to.alert
    except:
        time.sleep(1)
    str = ''
    try:
        str = sec1.text
        log.info(sec1.text)
    except:
        time.sleep(1)
    driver.quit()
    assert str.find('http') != -1, "The function should work."  
