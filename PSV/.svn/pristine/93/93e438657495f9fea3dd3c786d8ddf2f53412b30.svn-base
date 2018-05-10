'''  [PSV-2016-0115] Username and password used as cookie value (extender)  '''
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
    log.info('step-1 The credential information should NOT show in plaintext. ')
    if console_type == 'cable':
        print 'This case NA'
        str = 'NA'
        assert str != 'NA', "The function should not work."  
    else:
        url = host + urlLogs
        token = getIDToken(url)
        get_url = host + urlLogs
        log.info( get_url)
        r = requests.get(get_url,auth=(user,passwd))
        assert r.text.find('admin') == -1, "The function should not work."  
