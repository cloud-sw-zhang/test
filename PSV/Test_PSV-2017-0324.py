'''[PSV-2017-0324] Unauthenticated buffer overflow '''
''' anthor Cloud 2017-12-11'''
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
    log.info('step-1 The XSS injection code should not be executed')
    url = host + urlLogs
    token = getIDToken(url)
    if ProjectName == 'C7000-100NAS':
        url = host + 'DashBoard.htm'
    else:
        url = host + start
    try:
        r = ''
        r = requests.get(url, auth=('adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn', 'passworddddddddddddddddddd'))
        log.info(r.text)
    except:
        time.sleep(1)
    if r != '':
        assert r.status_code == 401, "The function should not work."
    else:
        assert r == '', "The function should not work."

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 