'''[PSV-2017-0790] Remote code execution (pre-auth)  '''
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
    log.info("step-1 Remote code execution shouldn't succeed.")
    # fname = "/proc/self/maps"
    # uri = "/" * (72-len(fname)) + "../" + fname + "/genieping.cgi"
    # get_url = 'http://' + hostip + url
    # log.info( get_url)
    # tmpHTML = requests.get(get_url,auth=(user,passwd))
    log.info('This case need run in kali testplatform')
    case = 'fail'
    assert case == 'pass', "The function should not work." 
