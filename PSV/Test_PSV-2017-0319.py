'''[PSV-2017-0319] Full authentication byPass  '''
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
    log.info('step-1 Authorization header should never be bypassed when change DUT configurations')
    url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
    headers = {
        'Host': hostip,
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    }
    if hostip == '192.168.1.1':
        index1 = '1'
        index2 = '1'
    elif hostip == '192.168.100.1':
        index1 = '100'
        index2 = '250'
    elif hostip == '192.168.1.250':
        index1 = '1'
        index2 = '250'
    else:
        index1 = '0'
        index2 = '1'
    if console_type == 'cable':
        post_url = host + 'goform/LANSetup' + token +'&x=.gif'
        data = 'action=Apply&device_name=Mick-change&sysLANIPAddr1=192&sysLANIPAddr2=168&sysLANIPAddr3=0&sysLANIPAddr4=1&sysLANSubnetMask1=255&sysLANSubnetMask2=255&sysLANSubnetMask3=255&sysLANSubnetMask4=0&dhcp_server=dhcp_server&sysPoolStartingAddr4=10&sysPoolFinishAddr4=254&select=-1&device_name_tmp=C7000-100NAS%3Breboot&lan_ipaddr=192.168.0.1&lan_netmask=255.255.255.0&rip_enable=0&rip_multicast=1&rip_version=2&lan_proto=dhcp&dhcp_start=192.168.0.10&dhcp_end=192.168.0.254&dhcp_start_old=192.168.0.10&dhcp_end_old=192.168.0.254&pptp_wan_ipaddr=...&l2tp_wan_ipaddr=...&pppoe_wan_ipaddr=&pptp_serv_ipaddr=&l2tp_serv_ipaddr=&wan_dns1_pri=&wan_dns1_sec=&wan_proto=dhcp&wan_ipaddr=0.0.0.0&wan_netmask=0.0.0.0&repeater=0&repeater_an=0&dlna_autoip_en=0&tmp_lan_ipaddr=192.168.0.1&tmp_lan_netmask=0.0.0.0&tmp_lan_proto=null&tmp_rip_enable=null'
    else:
        if ProjectName == 'V6510':
            post_url = host + 'lan_m.cgi' + token +'&x=.gif'
        else:
            post_url = host + 'lan.cgi' + token +'&x=.gif'
        data = {
            'action':'Apply',
            'device_name' : 'Mick-' ,
            'sysLANIPAddr1' : '192' ,
            'sysLANIPAddr2' : '168' ,
            'sysLANIPAddr3' : index1 ,
            'sysLANIPAddr4' : index2 ,
            'sysLANSubnetMask1' : '255' ,
            'sysLANSubnetMask2' : '255' ,
            'sysLANSubnetMask3' : '255' ,
            'sysLANSubnetMask4' : '0' ,
            'rip_direction' : '1' ,
            'sysRIPVersion' : 'Disabled' ,
            'dhcp_server' : 'dhcp_server' ,
            'sysPoolStartingAddr4' : '2' ,
            'sysPoolFinishAddr4' : '254' ,
            'select' : '1' ,
            'arp_enable' : 'disable' ,
            'ipmac_token' : '0' ,
            'dev_name' : 'R8500mge' ,
            'lan_ipaddr' : hostip ,
            'lan_netmask' : '255.255.255.0' ,
            'rip_enable' : '0' ,
            'rip_multicast' : '1' ,
        }
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '': 
        log.info(r.text)
        assert r.status_code == 401, "The function should not work." 
    else:
        assert r == '', "The function should not work." 

def test_Step_2():
    log.info('step-2 Check Internet AccountName')
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
        accountname = driver.find_element_by_name("device_name").get_attribute('value')
    else:
        accountname = driver.find_element_by_name("system_name").get_attribute('value')
    # if ProjectName == 'R6700' or ProjectName == 'R7000P':
        # accountname = driver.find_element_by_name("device_name").get_attribute('value')
    # else:
        # accountname = driver.find_element_by_name("system_name").get_attribute('value')
    driver.quit()
    log.info(accountname)
    assert accountname.find('Mick') == -1,"The function should not work." 