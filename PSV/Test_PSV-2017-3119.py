'''[PSV-2017-3119]Path traversal in Netgear EX7000 Wifi Repeater '''
''' anthor Cloud 2018-01-04'''
'''v1.0 '''
from API._API import *

# #def test_step_0():
    # #log.info( 'step-0-0 dut loaddrfault wait 160s')
    # #aploaddefault()
    # #log.info( "step-0-1 AP Genie over leap done")
    # #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 It will redirect to genie initial page which disclose current wireless password')
    if hostip == '192.168.1.250':
        url = host + urlLogs
        token = getIDToken(url)
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {'Authorization': Authorization}
        data = 'buttonHit=&buttonValue=&submit_flag=browser_close&nodenumber=2&currentpath=%2Ftmp%2Fmnt%2Fusb0%2Fpart1%2F..%2F..%2F..%2F..%2F&nodevalue=1*System+Volume+Information*0%2Ftmp%2Fmnt%2Fusb0%2F part1%2F..%2F..%2F..%2F..%2F0'
        post_url = host + 'usb_browse.cgi' + token
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.status_code)
        if r.status_code == 401:
            case = 'pass'
        else:
            case = 'fail'
    else:
        case = 'NA'
    assert case == 'pass', "This action should not  work."
