'''[PSV-2017-0325] HTTP Auth used over HTTP leads to password leakage via MITM  '''
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
    log.info('step-1 CSRF-Router reboot using/newgui_adv_home.cgi----DUT should prevent the CSRF attack')
    if console_type == 'cable':
        print 'This case NA'
        scase = 'fail'
    else:
        url = host + urlRemoteManagement
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
            post_url = host + 'goform/RemoteManagementRetail' + token
            data = 'apply=Apply&remote_mg_enable=remote_mg&remote_mg_enable_https&rm_access=all&http_rmport=8080&https_rmport=8443&http_rmenable=1&http_rmstartip=0.0.0.0&http_rmendip=255.255.255.255&http_wanipaddr=10.11.0.13'
        else:
            data = 'apply=Apply&remote_mg_enable=remote_mg&rm_access=all&http_rmport=8443&http_rmenable=1&http_rmstartip=0.0.0.0&http_rmendip=255.255.255.255&http_wanipaddr=88.0.0.47'
            post_url = host + 'fwRemote.cgi' + token
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        if r.status_code == 200:
            case1 = 'pass'
        else:
            case1 = 'fail'
        codestr1 = Authorization.split(' ')
        codestr = codestr1[1]
        print codestr
        a1 = codestr.decode('base64')
        print a1
        if a1 == 'admin:Password!':
            case2 = 'fail'
        else:
            case2 = 'pass'
        if case1 == 'pass' and case2 == 'pass':
            case = 'pass'
        else:
            case = 'fail'
    assert case == 'pass', "The function should not work." 

def test_Step_2():
    log.info( 'step-2 check remotemanagement is enable')
    if console_type == 'cable':
        print 'This case NA'
        str = False
    else:
        driver = webdriver.Firefox()
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlRemoteManagement
        driver.get(url)
        time.sleep(15)
        str = driver.find_element_by_name("remote_mg_enable").is_selected()
        driver.quit()
    assert str == True, "This action should work." 
