''' [PSV-2016-0075] XSS vulnerability    '''
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
    log.info('step-1 The XSS injection code should NOT be executed')
    url = host + urlLogs
    token = getIDToken(url)
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSetup
    driver.get(url)
    time.sleep(15)
    driver.find_element_by_name("ssid").clear()
    driver.find_element_by_name("ssid").send_keys('''<script>alert(1)</script>""''')
    driver.find_element_by_name("Apply").click()
    try:
        sec = driver.switch_to.alert
        sec.accept()
    except:
        time.sleep(1)
    time.sleep(35)
    ssidname = driver.find_element_by_name("ssid").get_attribute('value')
    driver.quit()
    log.info(ssidname)
    if ssidname == '''<script>alert(1)</script>""''':
        result = 'fail'
    else:
        result = 'pass'
    assert result == 'pass', "This action should work." 
