''' This script can burn dut ether mac'''
''' anthor Cloud 2017-11-24'''
'''v1.0 '''
from API._API import *
from API._Console import *
from API._FormatCheckLib import *
from API._logging import *
def test_Step_1():
    log.info( 'step-1 dut loaddrfault wait 160s')
    aploaddefault()

def test_Step_2():
    log.info( "step-2 AP Genie over leap done")
    Genie_overleap()

def test_step_0():
    log.info( 'step-0-0 dut loaddrfault wait 160s')
    aploaddefault()
    log.info( "step-0-1 AP Genie over leap done")
    Genie_overleap()
    log.info( "step-0-2 disable changed-url token")
    Disable_changedToken()