''' [PSV-2017-0709] RCE via pppoe2_domain.cgi  '''
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
    log.info('step-1 Buffer overflow attack')
    if console_type == 'cable':
        print 'This case NA'
        result = 'fail'
        assert result == 'pass', "The function should work." 
    else:
        url = host + urlLogs
        token = getIDToken(url)
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {'Authorization': Authorization}
        data = 'policyIndex=aaaaaaaaaaaaaaaaaaaaaaaaaaaa%40V%08%00%C4%3F%ED%00aaaaaaaaaaaaaaaaaaaaaaaaT%2C%02%00'
        post_url = host + 'pppoe2_domain.cgi' + token + '&unauth.cgi'
        r = requests.post(post_url, data = data, auth = ('sleep 5', 'test'),timeout=5)
        log.info(r.text)
        assert r.status_code == 401, "The function should work." 

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    if console_type == 'cable':
        print 'This case NA'
        str = 'fail'
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
        str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 