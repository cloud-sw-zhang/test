''' [PSV-2017-0333] CSRF:Change Ethernet settings     '''
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
    log.info('step-1 R8500 should check the CSRF tokenID on ether.cgi and to prevent the CSRF attack.')
    url = host + urlLogs
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
    data ='apply=Apply&system_name=Mick_R8500-11111&domain_name=&WANAssign=dhcp&DNSAssign=0&MACAssign=0&runtest=no&wan_proto=dhcp&wan_ipaddr=10.7.5.249&wan_netmask=255.0.0.0&wan_gateway=10.7.5.253&wan_dns_sel=0&wan_dns1_pri=...&wan_dns1_sec=...&wan_hwaddr_sel=0&wan_hwaddr_def=2C%3A30%3A33%3AE3%3AB6%3AEF&wan_hwaddr2=function+toUpperCase%28%29+%7B+%5Bnative+code%5D+%7D&wan_hwaddr_pc=A0%3AD3%3AC1%3A24%3A18%3A5B&lan_ipaddr=' + hostip + '&lan_netmask=255.255.255.0&parental_control=0&ipv6_proto=disable'
    if console_type == 'cable':
        post_url = host + 'goform/BasicSettingsBottom' + token
    else:
        post_url = host + 'ether.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info(r.status_code)
    time.sleep(60)
    data1 ='apply=Apply&system_name=Mick_R8500-2222&domain_name=&WANAssign=dhcp&DNSAssign=0&MACAssign=0&runtest=no&wan_proto=dhcp&wan_ipaddr=10.7.5.249&wan_netmask=255.0.0.0&wan_gateway=10.7.5.253&wan_dns_sel=0&wan_dns1_pri=...&wan_dns1_sec=...&wan_hwaddr_sel=0&wan_hwaddr_def=2C%3A30%3A33%3AE3%3AB6%3AEF&wan_hwaddr2=function+toUpperCase%28%29+%7B+%5Bnative+code%5D+%7D&wan_hwaddr_pc=A0%3AD3%3AC1%3A24%3A18%3A5B&lan_ipaddr=' + hostip + '&lan_netmask=255.255.255.0&parental_control=0&ipv6_proto=disable'
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data1,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info(r.status_code)

def test_Step_2():
    log.info('step-2 Check system name')
    driver = webdriver.Firefox()
    if ProjectName == 'R8000':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlInternetSetup
    elif ProjectName == 'R6700' or ProjectName == 'R7000P' or ProjectName == 'R6900' or ProjectName == 'Orbi':
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDeviceName
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlInternetSetup
    driver.get(url)
    time.sleep(15)
    str = ''
    try:
        str = driver.find_element_by_name("device_name")
    except:
        time.sleep(1)
    if str != '':
        systemname = driver.find_element_by_name("device_name").get_attribute('value')
    else:
        systemname = driver.find_element_by_name("system_name").get_attribute('value')
    # if ProjectName == 'R6700' or ProjectName == 'R7000P':
        # systemname = driver.find_element_by_name("device_name").get_attribute('value')
    # else:
        # systemname = driver.find_element_by_name("system_name").get_attribute('value')
    driver.quit()
    log.info(systemname)
    if systemname != 'Mick_R8500-2222' or systemname != 'Mick_R8500-11111':
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "This action should not work."    