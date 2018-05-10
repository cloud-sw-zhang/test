''' [PSV-2017-1206] CSRF token hash is available without authentication     '''
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
    log.info('step-1 CSRF tokensID should be generated using more complex algorithms')
    log.info('new testplatform not support')
    case = 'fail'
    assert case == 'pass', "The function should not work." 
