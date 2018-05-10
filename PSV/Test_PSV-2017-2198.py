'''	[PSV-2017-2198] Automatic Logout is Ineffective '''
''' anthor Cloud 2018-01-04'''
'''v1.0 '''
from API._API import *

# #def test_step_0():
    # #log.info( 'step-0-0 dut loaddrfault wait 160s')
    # #aploaddefault()
    # #log.info( "step-0-1 AP Genie over leap done")
    # #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 The automatic logout functionality on the WNDR4500v3 is ineffective and can be trivially bypassed.')
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip
    driver.get(url)
    time.sleep(15)
    str3 = sendCommandAndGetReturnUntil(com,'nvram show | grep https ','#')
    if str3.find('httpsEnable') != -1:
        driver.find_element_by_name("logout").click()
    time.sleep(300)
    driver.refresh()
    try:
        str = ''
        sec = driver.switch_to_alert
        str1 = sec.text
        str = str1.encode("utf-8")
    except:
        time.sleep(1)   
    driver.quit()
    if str == '' or len(str) < 150:
        case = 'pass'
    else:
        case = 'fail'
    time.sleep(5)
    print str
    log.info(sec)
    assert case == 'pass', "The function should work."