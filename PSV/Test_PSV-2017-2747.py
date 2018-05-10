''' 	[PSV-2017-2747] CSRF in password change  '''
''' anthor Cloud 2018-01-03'''
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
    log.info('step-1 CSRF token not work in password change')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        if hostip == '192.168.1.250':
            log.info('Get Settings password token id')
            url = host + 'pwdSettings.html'
            token = getIDToken(url)
            Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd)
            headers = {
                'Host': hostip,
                'Authorization': Authorization,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            }
            data = 'onoff=0&new_username=&new_pwd=&question1=&question2=&answer2='
            post_url = host + 'password.cgi'
            r = requests.post(post_url, headers=headers, data=data,timeout=5)
            log.info(r.status_code)
            time.sleep(5)
            tmpHTML = requests.get(url,auth=(user,passwd))
            if tmpHTML.status_code == 200:
                case = 'pass'
            else:
                case = 'fail'
        else:
            case = 'NA'
    assert case == 'pass', "This action should not work." 
