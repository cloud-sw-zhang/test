''' [PSV-2017-0318] Arbitrary file read through HTTP  '''
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
    log.info('step-1 User have NOT permission to see the system files.')
    url = host + urlLogs
    token = getIDToken(url)
    post_url = host + '../../../etc/system.conf'
    r = ''
    try:
        r = requests.get(post_url, auth=(user, passwd))
    except:
        time.sleep(1)
    if r != '':
        assert r.text.find('system') == -1, "The function should not work." 
    else:
        assert r == '', "The function should not work." 