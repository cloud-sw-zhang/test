''' [PSV-2016-0257] URL injection in "ErrorMsg.htm"   '''
''' anthor Cloud 2017-12-07'''
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
    log.info('step-1 Buffer overflow in the URL timestamp parameter')
    url = host + urlLogs
    token = getIDToken(url)
    if hostip == '192.168.0.1':
        post_url = host + "ErrorMsg.htm?url=http://192.168.0.15:8080&msg=Lock%20here%20hahaha%20YAYAYA"
    else:
        post_url = host + "ErrorMsg.htm?url=http://192.168.1.15:8080&msg=Lock%20here%20hahaha%20YAYAYA"
    r = requests.get(post_url,auth=(user,passwd))
    log.info(r.text)
    if r.text.find('Lock here hahaha YAYAYA') == -1:
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "This action should not work." 
