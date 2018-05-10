''' [PSV-2017-0335] UnAuthenticated Access to VPN Configuration  '''
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
    log.info('step-1 All pages cannot access in both LAN/WAN interface without authorized.')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        cmd1 = '"curl.exe" ' + host + 'windows.zip'
        cmd2 = '"curl.exe" ' + host + 'nonwindows.zip'
        cmd3 = '"curl.exe" ' + host + 'smartphone.zip'
        log.info('run %s command',cmd1)
        log.info('run %s command',cmd2)
        log.info('run %s command',cmd3)
        p1 = os.popen(cmd1)
        p2 = os.popen(cmd2)
        p3 = os.popen(cmd3)
        str1 = p1.read()
        str2 = p2.read()
        str3 = p3.read()
        log.info(str1)
        log.info(str2)
        log.info(str3)
        if str1.find('401') != -1 and str2.find('401') != -1 and str3.find('401') != -1:
            case = 'pass'
        else:
            case = 'fail'
    assert case == 'pass', "This action should not work." 

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    if console_type == 'cable':
        print 'This case NA'
        str = 'fail'
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
        str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 