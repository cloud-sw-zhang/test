''' [PSV-2017-0590] Directory traversal    '''
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
    log.info('step-1 Commend injection detected on R7000&R6400--DUT should not accept such command')
    if hostip == '192.168.0.1':
        if console_type == 'cable':
            cmd1 = '"curl.exe" --interface 192.168.0.88 -P--ftp-port -O -u admin:password http://192.168.0.1/img/../../etc/group'
            cmd2 = '"curl.exe" --interface 192.168.0.88 -P--ftp-port -O -u admin:password http://192.168.0.1/script/../../tmp/Debug_log.zip'
        else:
            cmd1 = '"curl.exe" --interface 192.168.0.88 -P--ftp-port -O -u admin:Password! http://192.168.0.1/img/../../etc/group'
            cmd2 = '"curl.exe" --interface 192.168.0.88 -P--ftp-port -O -u admin:Password! http://192.168.0.1/script/../../tmp/Debug_log.zip'
    elif hostip == '192.168.1.250':
        cmd1 = '"curl.exe" --interface 192.168.1.88 -P--ftp-port -O -u admin:Password! http://192.168.1.250/img/../../etc/group'
        cmd2 = '"curl.exe" --interface 192.168.1.88 -P--ftp-port -O -u admin:Password! http://192.168.1.250/script/../../tmp/Debug_log.zip'
    elif hostip == '192.168.100.1':
        cmd1 = '"curl.exe" --interface 192.168.100.88 -P--ftp-port -O -u admin:Password! http://192.168.100.1/img/../../etc/group'
        cmd2 = '"curl.exe" --interface 192.168.100.88 -P--ftp-port -O -u admin:Password! http://192.168.100.1/script/../../tmp/Debug_log.zip'
    else:
        cmd1 = '"curl.exe" --interface 192.168.1.88 -P--ftp-port -O -u admin:Password! http://192.168.1.1/img/../../etc/group'
        cmd2 = '"curl.exe" --interface 192.168.1.88 -P--ftp-port -O -u admin:Password! http://192.168.1.1/script/../../tmp/Debug_log.zip'
	log.info('run %s command',cmd1)
    log.info('run %s command',cmd2)
    p1 = os.popen(cmd1)
    log.info(p1)
    p2 = os.popen(cmd2)
    log.info(p2)
    cmd3 = 'expand Debug_log.zip Debug_log.txt'
    log.info('run %s command',cmd1)
    p3 = os.popen(cmd3)
    log.info(p3)
    str1 = os.path.exists('Debug_log.txt')
    str2 = os.path.exists('group')
    if str1 == 'true':
        file = open('Debug_log1.txt')
        txtstr1 = file.read()
        file.close()
        if txtstr1.find('admin') != -1:
            case1 = 'pass'
        else:
            case1 = 'fail'
    else:
        case1 = 'pass'
    if str2 == 'true':
        file = open('group')
        txtstr2 = file.read()
        file.close()
        if txtstr2.find('admin') != -1: 
            case2 = 'pass'
        else:
            case2 = 'fail'
    else:
        case2 = 'pass'
    if case1 == 'pass' and case2 == 'pass':
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "This action should not work." 

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should not work." 
