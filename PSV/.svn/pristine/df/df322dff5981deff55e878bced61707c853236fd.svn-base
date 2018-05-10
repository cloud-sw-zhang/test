'''[PSV-2017-2331] Authentication Bypass  '''
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
    log.info("step-1 To bypass authentication one must append '&ess_=true' to the end of the requested URL.")
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        driver = webdriver.Firefox()
        url = "http://" + user + ':' + passwd + "@" + hostip + '/start.htm?test=1&ess_=true'
        driver.get(url)
        time.sleep(15)
        str = driver.page_source
        driver.quit()
        log.info(str)
        if str.find('404') != -1:
            case = 'NA'
        else:
            case = 'fail'
    assert case == 'pass', "This action should work." 
