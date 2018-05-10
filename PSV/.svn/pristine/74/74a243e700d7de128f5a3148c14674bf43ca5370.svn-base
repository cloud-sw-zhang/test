'''[PSV-2016-0122] Arbitrary File Read via ReadyShare / USB  '''
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
    log.info("step-1 DUT can't be used symbolic link to retrieve other files in the system by readyshare ")
    url = host + urlLogs
    token = getIDToken(url)
    if console_type == 'cable':
        get_url = host + 'USBBrowse.htm'
    else:
        get_url = host + 'USB_folderBrowse.htm'
    log.info( get_url)
    r = requests.get(get_url,auth=(user,passwd))
    log.info(r.text)
    if r.text.find('passwd') != -1 or r.text.find('init.d') != -1 or  r.text.find('resolv.con') != -1:
        case = 'fail'
    else:
        case = 'pass'
    assert case == 'pass', "The function should not work."  
