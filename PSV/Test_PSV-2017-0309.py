'''[PSV-2017-0309] Unauthenticated information leak through /multi_login.cgi (admin hostname & IP)     '''
''' anthor Cloud 2017-12-08'''
'''v1.0 '''
#from API._API import *

#def test_step_0():
    #log.info( 'step-0-0 dut loaddrfault wait 160s')
    #aploaddefault()
    #log.info( "step-0-1 AP Genie over leap done")
    #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 Anyone who should NOT get the information without authentication.')
    log.info('this case need another lan pc to Access http://192.168.1.1 and login as admin. ate no test envoriment')
    str = 'fail'
    assert str == 'pass', "This action should work." 