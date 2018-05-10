''' [PSV-2016-0100] XSS in recover.cgi     '''
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
    log.info('step-1 Commend injection detected on R7000&R6400--DUT should not accept such command')
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
        driver.find_element_by_name("logout").click()
        driver.find_element_by_name("logout").click()
    except:
        time.sleep(1)
    time.sleep(5)
    driver.quit()
    if console_type == 'cable':
        cmd = '"curl.exe" ' + host + 'goform/PwdRec_checkserial'
    else:
        cmd = '"curl.exe" ' + host + 'cgi-bin/PwdRec_AskQuestion.cgi'
    log.info('run %s command',cmd)
    p1 = os.popen(cmd)
    str = p1.read()
    log.info(str)
    if str.find('401') != -1 or str.find('passwd') == -1:
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "This action should not work."     
