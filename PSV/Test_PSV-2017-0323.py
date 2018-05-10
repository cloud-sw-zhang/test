'''[PSV-2017-0323] stored XSS via User_setup.htm'''
''' anthor Cloud 2017-12-11'''
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
    log.info('step-1 The XSS injection code should not be executed')
    if console_type == 'cable':
        print 'This case NA'
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
        if console_type == 'cable':
            post_url = host + 'goform/user_setup_add' + token
        else:
            post_url = host + 'user_setup_add.cgi' + token
        data = {
            'add':'Add',
            'username':'test',
            'passwd':'password<script>alert(1)</script>',
            'repasswd' : 'password<script>alert(1)</script>',
            'mail':'LocalUser'
        }
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.text)
#    assert r.status_code == 200, "The function should not work." 

def test_Step_2():
    log.info( 'step-2 Check info in user_setup.htm')
    if console_type == 'cable':
        print 'This case NA'
        str = 'to change admin password'
    else:
        cmd = '"curl.exe" -u admin:password ' + host + 'User_setup.htm'
        log.info('run %s command',cmd)
        p1 = os.popen(cmd)
        str = p1.read()
        print str
    assert str.find('to change admin password') == -1, "This action should not work."  