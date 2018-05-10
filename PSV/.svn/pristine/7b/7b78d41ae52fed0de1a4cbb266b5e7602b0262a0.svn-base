''' [PSV-2017-0334] Access_control change CSRF attack    '''
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
    log.info('step-1 Using ?id to disable ACL and check')
    log.info('enable access control')
    url = host + urlDevicecontrol
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd)
    headers = {
        'Host': hostip,
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Authorization': Authorization,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    }
    if hostip == '192.168.1.1':
        data ='action=Apply&select=-1&rule_status_org=allow&rule_status_org=allow&enable_access_control=1&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=2%3AA0%3AD3%3AC1%3A24%3A18%3A5B%3A1%3A00%3A05%3A1B%3A9E%3A03%3A08%3A1%3A&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=192.168.1.2&is_edit_itself='
        data1 ='action=Apply&enable_acl=enable_acl&access_all=allow_all&select=-1&rule_status_org=allow&rule_status_org=allow&enable_access_control=0&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=2%3AA0%3AD3%3AC1%3A24%3A18%3A5B%3A1%3A00%3A05%3A1B%3A9E%3A03%3A08%3A1%3A&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=192.168.1.2&is_edit_itself='
    elif hostip == '192.168.100.1':
        data ='action=Apply&select=-1&rule_status_org=allow&rule_status_org=allow&enable_access_control=1&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=2%3AA0%3AD3%3AC1%3A24%3A18%3A5B%3A1%3A00%3A05%3A1B%3A9E%3A03%3A08%3A1%3A&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=192.168.100.2&is_edit_itself='
        data1 ='action=Apply&enable_acl=enable_acl&access_all=allow_all&select=-1&rule_status_org=allow&rule_status_org=allow&enable_access_control=0&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=2%3AA0%3AD3%3AC1%3A24%3A18%3A5B%3A1%3A00%3A05%3A1B%3A9E%3A03%3A08%3A1%3A&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=192.168.100.2&is_edit_itself='
    elif hostip == '192.168.0.1':
        data ='action=Apply&select=-1&rule_status_org=allow&rule_status_org=allow&enable_access_control=1&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=2%3AA0%3AD3%3AC1%3A24%3A18%3A5B%3A1%3A00%3A05%3A1B%3A9E%3A03%3A08%3A1%3A&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=192.168.0.2&is_edit_itself='
        data1 ='action=Apply&enable_acl=enable_acl&access_all=allow_all&select=-1&rule_status_org=allow&rule_status_org=allow&enable_access_control=0&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=2%3AA0%3AD3%3AC1%3A24%3A18%3A5B%3A1%3A00%3A05%3A1B%3A9E%3A03%3A08%3A1%3A&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=192.168.0.2&is_edit_itself='
    else:	
        data ='action=Apply&select=-1&rule_status_org=allow&rule_status_org=allow&enable_access_control=1&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=2%3AA0%3AD3%3AC1%3A24%3A18%3A5B%3A1%3A00%3A05%3A1B%3A9E%3A03%3A08%3A1%3A&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=192.168.1.2&is_edit_itself='
        data1 ='action=Apply&enable_acl=enable_acl&access_all=allow_all&select=-1&rule_status_org=allow&rule_status_org=allow&enable_access_control=0&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=2%3AA0%3AD3%3AC1%3A24%3A18%3A5B%3A1%3A00%3A05%3A1B%3A9E%3A03%3A08%3A1%3A&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=192.168.1.2&is_edit_itself='
    if console_type == 'cable':
        data ='action=Apply&access_all=allow_all&rule_status_org=allow&enable_access_control=1&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=a0%3Ad3%3Ac1%3A24%3A18%3A5b&is_edit_itself='
        data1 ='action=Apply&access_all=allow_all&rule_status_org=allow&enable_access_control=1&access_all_setting=1&allowed_text=Allowed&blocked_text=Blocked&rule_settings=&delete_white_lists=&delete_black_lists=&edit_lists=&router_access_user=a0%3Ad3%3Ac1%3A24%3A18%3A5b&is_edit_itself='
        post_url = host + 'goform/AccessControl' + token
    else:
        post_url = host + 'access_control.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info(r.text)
        time.sleep(10)
    log.info('disable access control using same token')
    r1 = ''
    try:
        r1 = requests.post(post_url, headers=headers, data=data1,timeout=5)
    except:
        time.sleep(1)
    if r1 != '':
        log.info(r1.text)
        if console_type == 'cable':
            if r.status_code == 401 and r1.status_code == 401:
                case = 'pass'
            else:
                case = 'fail'
        else:
            if r.status_code == 200 and r1.status_code == 200:
                case = 'pass'
            else:
                case = 'fail'
        assert case == 'pass','This is should work'
    else:
        assert r1 == '','This is should work'

def test_Step_2():
    log.info('step-2 dut should prevent the CSRF attack')
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    driver.get(url)
    time.sleep(15)
    AclStatus = driver.find_element_by_name("enable_acl").is_selected()
    driver.quit()
    assert AclStatus == False,'This is should not work'