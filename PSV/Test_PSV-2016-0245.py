''' [PSV-2016-0245] Commend injection detected on R7000 & R6400    '''
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
    cmd1 = '"curl.exe" ' + host + 'cgi-bin/;reboot'
    cmd2 = '"curl.exe" ' + host + 'cgi-bin/reboot'
    cmd3 = '"curl.exe" ' + host + 'cgi-bin/||reboot'
    cmd4 = '"curl.exe" ' + host + 'cgi-bin/&&reboot'
    cmd5 = '"curl.exe" ' + host + "cgi-bin/;telnetd$IFS-p$IFS'23'"
    log.info('run %s command',cmd1)
    log.info('run %s command',cmd2)
    log.info('run %s command',cmd3)
    log.info('run %s command',cmd4)
    log.info('run %s command',cmd5)
    p1 = os.popen(cmd1)
    log.info(p1)
    p2 = os.popen(cmd2)
    log.info(p2)
    p3 = os.popen(cmd3)
    log.info(p3)
    p4 = os.popen(cmd4)
    log.info(p4)
    p5 = os.popen(cmd5)
    log.info(p5)

def test_Step_2():
    str2 = judjeduttelnet()
    log.info( 'step-2 check telnet dut')
    if str2 == 'pass':
        log.info(str2)
        log.info( "check telnet dut pass")
        time.sleep(1)
    else:
        log.info(str2)
        log.info( "check telnet dut fail")
    assert str2 == 'pass', "This action should work." 

def test_Step_3():
    log.info( 'step-3 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 
