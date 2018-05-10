''' [PSV-2017-0386] Management Console Vulnerable to CSRF  '''
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
    log.info('step-1 RCE via device_name parameter ')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {
            'Host': hostip,
            'Cache-Control': 'max-age=0',
            'Authorization': Authorization,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        }
        data = 'remote_mg_enable=disable&rm_access=all&http_rmport=8080&todo=save&this_file=FW_remote.htm&next_file=FW_remote.htm&c4_local_ip_=&c4_start_ip_=&c4_fin_ip_=&h_old_remote_mg=disable&h_remote_mg_enable=enable&h_rm_access=all&SID'
        if console_type == 'cable':
            post_url = host + 'goform/setup'
        else:
            post_url = host + 'setup.cgi'
        r = requests.post(post_url, headers=headers, data=data,timeout=5) 
        log.info(r.status_code)
        if r.status_code == 404:
            case = 'pass'
        else:
            case = 'fail'
    assert case == 'pass', "The function should not work." 
