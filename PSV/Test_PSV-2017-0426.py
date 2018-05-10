''' [PSV-2017-0426] Download debug log without authentication     '''
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
    log.info('step-1 User should not be able to download this file without authorization.')
    if hostip == '192.168.0.1':
        if console_type == 'cable':
            cmd = '"curl.exe" --interface' + '192.168.0.88 -P--ftp-port -o Debug_log1.zip http://192.168.0.1/NETGEAR_' + ProjectName + '-Console.log' 
            if ProjectName == 'C3700-100NAS':
                cmd = '"curl.exe" --interface' + '192.168.0.88 -P--ftp-port -o Debug_log1.zip http://192.168.0.1/NETGEAR_' + ProjectName + '-Config.log?captureLogOption=0' 
        else:
            cmd = '"curl.exe" --interface' + '192.168.0.88 -P--ftp-port -o Debug_log1.zip http://192.168.0.1/LGO_logout.htm/Debug_log.zip'
    elif hostip == '192.168.100.1':
        cmd = '"curl.exe" --interface' + '192.168.100.88 -P--ftp-port -o Debug_log1.zip http://192.168.100.1/LGO_logout.htm/Debug_log.zip'
    elif hostip == '192.168.1.250':
        cmd = '"curl.exe" --interface' + '192.168.1.88 -P--ftp-port -o Debug_log1.zip http://192.168.1.250/LGO_logout.htm/Debug_log.zip'
    else:
        cmd = '"curl.exe" --interface' + '192.168.1.88 -P--ftp-port -o Debug_log1.zip http://192.168.1.1/LGO_logout.htm/Debug_log.zip'
    log.info('run %s command',cmd)
    p1 = os.popen(cmd)
    time.sleep(5)
    log.info(p1)
    cmd1 = 'expand Debug_log1.zip Debug_log1.txt'
    log.info('run %s command',cmd1)
    p2 = os.popen(cmd1)
    time.sleep(5)
    str1 = os.path.exists('Debug_log1.txt')
    log.info(str1)
    if str1 == 'true':
        file = open('Debug_log1.txt')
        txtstr = file.read()
        file.close()
        if txtstr.find('admin') != -1 or txtstr.find('Password!') != -1: 
            case = 'pass'
        else:
            case = 'fail'
    else:
        case = 'pass'
    assert case == 'pass',"This action should not work." 
