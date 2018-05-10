'''[PSV-2017-0425] Path traversal   '''
''' anthor Cloud 2017-12-12'''
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
    log.info('step-1 An authenticated user can access files from the router by using a path traversal vulnerability. ')
    if hostip == '192.168.0.1':
        if console_type == 'cable':
            cmd1 = '"curl.exe" --interface 192.168.0.88 -P--ftp-port -O -u admin:password http://192.168.0.1/../../../../../../etc/passwd'
        else:
            cmd1 = '"curl.exe" --interface 192.168.0.88 -P--ftp-port -O -u admin:Password! http://192.168.0.1/../../../../../../etc/passwd'
    elif hostip == '192.168.1.250':
        cmd1 = '"curl.exe" --interface 192.168.1.88 -P--ftp-port -O -u admin:Password! http://192.168.1.250/../../../../../../etc/passwd'
    elif hostip == '192.168.100.1':
        cmd1 = '"curl.exe" --interface 192.168.100.88 -P--ftp-port -O -u admin:Password! http://192.168.100.1/../../../../../../etc/passwd'
    elif hostip == '192.168.1.100':
        cmd1 = '"curl.exe" --interface 192.168.1.88 -P--ftp-port -O -u admin:Password! http://192.168.1.100/../../../../../../etc/passwd'
    else:
        cmd1 = '"curl.exe" --interface 192.168.1.88 -P--ftp-port -O -u admin:Password! http://192.168.1.1/../../../../../../etc/passwd'
    log.info('run %s command',cmd1)
    p1 = os.popen(cmd1)
    log.info(p1)
    str = ''
    try:
        file = open('passwd')
        str = file.read()
        file.close()
    except:
        time.sleep(1)
    if str.find('401') != -1 or str.find('admin') == -1 or str == '':
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "This action should work." 