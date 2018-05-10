''' [PSV-2017-0791] Buffer overflow (pre-auth)  '''
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
    log.info('step-1 DUT should block this traversal directory behavior')
    url = host + urlLogs
    token = getIDToken(url)
    post_url = host + "shares.cfg" + "A"*500
    try:
        r = requests.get(post_url, auth=(user, passwd))
    except:
        print 'get nothing'

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 