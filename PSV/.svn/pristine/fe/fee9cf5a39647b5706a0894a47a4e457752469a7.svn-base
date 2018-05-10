''' [PSV-2016-0061] Issue8 Passwords Stored in Plaintext   '''
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
    log.info( 'step-1 check The password should not be Plaintext.')
    if console_type == 'cable':
        print 'This case NA'
        str3 = 'admin:Password!'
    else:
        str3 = sendCommandAndGetReturn(com,'cat ./etc/passwd')
        print str3
    assert str3.find('admin:Password!') == -1, "This action should work." 
