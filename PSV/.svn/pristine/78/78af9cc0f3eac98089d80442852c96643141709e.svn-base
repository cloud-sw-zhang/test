''' [PSV-2017-0330] Disclose username/password via passwordrecovered.cgi '''
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
    log.info("step-1 you should NOT get the router's admin username and password.")
    url = host + urlLogs
    token = getIDToken(url)
    if console_type == 'cable':
        post_url = host + "goform/SetPassword" + token
    else:
        post_url = host + "passwordrecovered.cgi" + token
    log.info( post_url)
    r = ''
    try:
        r = requests.get(post_url,auth=(user,passwd))
        log.info(r.text)
    except:
        time.sleep(1)
    if r != '':
        if r.text.find('admin') == -1 and r.text.find('Password!') == -1:
            case = 'pass'
        else:
            case = 'fsil'
    else:
        case = 'pass'
    assert case == 'pass', "The function should not work." 
