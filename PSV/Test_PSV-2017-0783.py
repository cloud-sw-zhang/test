''' [PSV-2017-0783] Arbitrary file read without Authentication '''
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
    get_url = "http://" + hostip + "/////////////////////////////////////////////////////////////..//etc/passwd/genieping.cgi"
    tmpHTML = ''
    try:
        tmpHTML = requests.get(get_url,auth=('',''))
        log.info(tmpHTML.text)   
    except:
        time.sleep(1)
    if tmpHTML != '':
        assert tmpHTML.text.find('admin:Password!') == -1, "The function should not work." 
    else:
        assert tmpHTML == '', "The function should not work." 
