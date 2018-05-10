'''	[PSV-2018-0074] Admin Password Disclosure via BSW_wsw_summary.htm '''
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
    log.info("step-1 Admin Password Disclosure via BSW_wsw_summary.htm")
    driver = webdriver.Firefox()
    httpurl = "http://" + user + ':' + passwd + "@" + hostip + '/BSW_wsw_summary.htm'
    driver.get(httpurl)
    time.sleep(15)
    str = driver.page_source
    driver.quit()
    if str.find('admin') == -1 and str.find('Password!') == -1:
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "This action should not work." 
