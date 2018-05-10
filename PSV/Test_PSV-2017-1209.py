'''[PSV-2017-1209] Chained attack  '''
''' anthor Cloud 2017-12-13'''
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
    log.info('step-1 CSRF tokensID should be generated using more complex algorithms')
    log.info('new testplatform not support')
    log.info('same as PSV-2017-1206')
    case = 'fail'
    assert case == 'pass', "The function should not work." 

def test_Step_2():
    log.info('step-2 There is a root level command injection vulnerability in the device_name parameter on the lan.cgi page ')
    url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
    headers = {
        'Host': hostip,
        'Authorization':Authorization,
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
        index2 = '1'
    elif hostip == '192.168.1.250':
        index1 = '1'
        index2 = '250'
    else:
        index1 = '0'
        index2 = '1'
    if console_type == 'cable':
        data = 'action=Apply&device_name=C7000-100NAS%3Breboot&sysLANIPAddr1=192&sysLANIPAddr2=168&sysLANIPAddr3=0&sysLANIPAddr4=1&sysLANSubnetMask1=255&sysLANSubnetMask2=255&sysLANSubnetMask3=255&sysLANSubnetMask4=0&dhcp_server=dhcp_server&sysPoolStartingAddr4=10&sysPoolFinishAddr4=254&select=-1&device_name_tmp=C7000-100NAS%3Breboot&lan_ipaddr=192.168.0.1&lan_netmask=255.255.255.0&rip_enable=0&rip_multicast=1&rip_version=2&lan_proto=dhcp&dhcp_start=192.168.0.10&dhcp_end=192.168.0.254&dhcp_start_old=192.168.0.10&dhcp_end_old=192.168.0.254&pptp_wan_ipaddr=...&l2tp_wan_ipaddr=...&pppoe_wan_ipaddr=&pptp_serv_ipaddr=&l2tp_serv_ipaddr=&wan_dns1_pri=&wan_dns1_sec=&wan_proto=dhcp&wan_ipaddr=0.0.0.0&wan_netmask=0.0.0.0&repeater=0&repeater_an=0&dlna_autoip_en=0&tmp_lan_ipaddr=192.168.0.1&tmp_lan_netmask=0.0.0.0&tmp_lan_proto=null&tmp_rip_enable=null'
    else:
        data = {
            'action':'Apply',
            'device_name' : 'R8500;touch /tmp1/MickCheckFiles' ,
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
    if console_type == 'cable':
        if ProjectName == 'C6300':
            post_url = host + 'cgi-bin/lan' + token
            data = 'buttonHit=cfAlert_Apply&buttonValue=Start+Test&cfAlert_Apply=Start+Test&DiagnosticUtility=1&ip_type=ipv4&PingDestinationIP1=192&PingDestinationIP2=168&PingDestinationIP3=0&PingDestinationIP4=10&PingDestinationIPv6=&PingSize=64&NumberOfPing=3&TimeBetweePings=1000&TracerouteHost=tw.yahoo.com%3Breboot&TracerouteMaxHops=30&TracerouteDataSize=32&TracerouteBasePort=33434&TracerouteResolveHost=0&PingToolStatus=' + '+' * 56 + 'Waiting+for+input...++++++%0D%0A%0D%0A' + '+' * 52 + '&UtilityCommand=1&lan_ipaddr=192.168.0.1&PingDest_ipaddr=192.168.0.10&PingDestinationIP='
        else: 
            post_url = host + 'goform/LANSetup' + token
    else:
        if ProjectName == 'V6510':
            post_url = host + 'lan_m.cgi' + token
        else:
            post_url = host + 'lan.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info(r.text)
        assert r.status_code == 200, "The function should work." 
    else:
        assert r == '', "The function should work." 

def test_Step_3():
    log.info( 'step-3 Check file in console ')
    str = sendCommandAndGetReturn('com1','ls -al /tmp/')
    log.info(str)
    assert str.find('MickCheckFiles') == -1, "This action should work." 

def test_Step_4():
    log.info('step-4 There is a root level command injection vulnerability in the device_name parameter on the lan.cgi page ')
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
        index2 = '1'
    elif hostip == '192.168.1.250':
        index1 = '1'
        index2 = '250'
    else:
        index1 = '0'
        index2 = '1'
    if console_type == 'cable':
        post_url = host + 'goform/LANSetup' + token
        data = 'action=Apply&device_name=Mick-change&sysLANIPAddr1=192&sysLANIPAddr2=168&sysLANIPAddr3=0&sysLANIPAddr4=1&sysLANSubnetMask1=255&sysLANSubnetMask2=255&sysLANSubnetMask3=255&sysLANSubnetMask4=0&dhcp_server=dhcp_server&sysPoolStartingAddr4=10&sysPoolFinishAddr4=254&select=-1&device_name_tmp=C7000-100NAS%3Breboot&lan_ipaddr=192.168.0.1&lan_netmask=255.255.255.0&rip_enable=0&rip_multicast=1&rip_version=2&lan_proto=dhcp&dhcp_start=192.168.0.10&dhcp_end=192.168.0.254&dhcp_start_old=192.168.0.10&dhcp_end_old=192.168.0.254&pptp_wan_ipaddr=...&l2tp_wan_ipaddr=...&pppoe_wan_ipaddr=&pptp_serv_ipaddr=&l2tp_serv_ipaddr=&wan_dns1_pri=&wan_dns1_sec=&wan_proto=dhcp&wan_ipaddr=0.0.0.0&wan_netmask=0.0.0.0&repeater=0&repeater_an=0&dlna_autoip_en=0&tmp_lan_ipaddr=192.168.0.1&tmp_lan_netmask=0.0.0.0&tmp_lan_proto=null&tmp_rip_enable=null'
    else:
        if ProjectName == 'V6510':
            post_url = host + 'lan_m.cgi' + token
        else:
            post_url = host + 'lan.cgi' + token
        data = {
            'action':'Apply',
            'device_name' : 'R8500;touch /tmp/MickCheckFiles_PSV-2017-1208' ,
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

def test_Step_5():
    log.info( 'step-5 Check file in console ')
    str = sendCommandAndGetReturn('com1','ls -al /tmp/')
    log.info(str)
    assert str.find('MickCheckFiles') == -1, "This action should work." 
