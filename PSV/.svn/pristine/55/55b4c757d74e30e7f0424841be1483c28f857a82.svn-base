''' [PSV-2017-0745] CSRF leads to RCE through CVE-2017-6334  '''
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
    log.info('step-1 DUT should NOT accept this request and need to response "timestamp is expired"')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        cmd = '"curl.exe" -u admin:Password! -d "lookup=Lookup&host_name=www.google.com" ' + host + 'dnslookup.cgi' + token
        log.info('run %s command',cmd)
        p1 = os.popen(cmd)
        str = p1.read()
        if str.find('404') != -1 or str.find('timestamp is expired') != -1:
            case = 'fail'
        else:
            case = 'pass'
    assert case == 'pass', "The function should work." 
