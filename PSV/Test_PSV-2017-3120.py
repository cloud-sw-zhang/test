'''[PSV-2017-3120] Authentication-Bypass '''
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
    log.info('step-1 It will redirect to genie initial page which disclose current wireless password')
    url = host + 'MNU_access_unauthorized_checkSerial.htm'
    if console_type == 'cable':
        url = host + 'PwdRec_checkserial.htm'
    token = ''
    try:
        token = getIDToken(url)
    except:
        time.sleep(1)
    if token == '':
        assert token == '', "This action should not  work."
    else:
        Authorization = 'Basic ' + base64.b64encode(user+ ':' + passwd) 
        headers = {'Authorization': Authorization}
        data = 'apply=Execute'
        post_url = host + 'genieDisableLanChanged.cgi' + token
        r = ''
        try:
            r = requests.post(post_url, headers=headers, data=data,timeout=5)
        except:
            time.sleep(1)
        if r != '': 
            log.info(r.status_code)
            time.sleep(5)
            r = requests.post(post_url, headers=headers, data=data,timeout=5)
            log.info(r.status_code)
            assert r.status_code == 401, "This action should not  work."
        else:
            assert r == '', "This action should not  work."

def test_Step_2():
    log.info('step-2 check dut will redirect to genie initial page')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 

def test_Step_3():
    log.info('step-3 burn original ethermac')
    if console_type == 'cable':
        time.sleep(1)
    else:
        f1 = open('F:\ATE_script\PSV\mac.txt')
        Burnethmac = f1.read()
        print Burnethmac
        f1.close()
        f2 = open('F:\ATE_script\PSV\sn.txt')
        Burnsn =  f2.read()
        print Burnsn
        f2.close()
        sendCommandAndGetReturn(com,'burnethermac ' + Burnethmac)
        sendCommandAndGetReturn(com,'burnsn ' + Burnsn)
        sendCommandAndGetReturn(com,console_type + ' save')
        sendCommandAndGetReturn(com,'reboot')
        time.sleep(60)
