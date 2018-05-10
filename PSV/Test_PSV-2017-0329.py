''' [PSV-2017-0329] RCE via device_name parameter    '''
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
    if hostip == '192.168.1.1':
        data = 'action=Apply&device_name=R8500%3Aping%20192.168.1.2&sysLANIPAddr1=192&sysLANIPAddr2=168&sysLANIPAddr3=1&sysLANIPAddr4=1&sysLANSubnetMask1=255&sysLANSubnetMask2=255&sysLANSubnetMask3=255&sysLANSubnetMask4=0&rip_direction=1&sysRIPVersion=Disabled&dhcp_server=dhcp_server&sysPoolStartingAddr4=2&sysPoolFinishAddr4=254&select=-1&arp_enable=disable&ipmac_token=0&dev_name=R8500&lan_ipaddr=192.168.1.1&lan_netmask=255.255.255.0&rip_enable=0&rip_multicast=1&rip_version=2&lan_proto=dhcp&dhcp_start=192.168.1.2&dhcp_end=192.168.1.254&dhcp_start_old=192.168.1.2&dhcp_end_old=192.168.1.254&pptp_wan_ipaddr=...&l2tp_wan_ipaddr=...&pppoe_wan_ipaddr=...&pptp_serv_ipaddr=10.0.0.138&l2tp_serv_ipaddr=&wan_dns1_pri=&wan_dns1_sec=&wan_proto=dhcp&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&repeater=0&repeater_an=0&dlna_autoip_en=0&tmp_lan_ipaddr=0.0.0.0&tmp_lan_netmask=0.0.0.0&tmp_lan_proto=null&tmp_rip_enable=null'
    elif hostip == '192.168.100.1':
        data = 'action=Apply&device_name=R8500%3Aping%20192.168.100.2&sysLANIPAddr1=192&sysLANIPAddr2=168&sysLANIPAddr3=100&sysLANIPAddr4=250&sysLANSubnetMask1=255&sysLANSubnetMask2=255&sysLANSubnetMask3=255&sysLANSubnetMask4=0&rip_direction=1&sysRIPVersion=Disabled&dhcp_server=dhcp_server&sysPoolStartingAddr4=2&sysPoolFinishAddr4=254&select=-1&arp_enable=disable&ipmac_token=0&dev_name=R8500&lan_ipaddr=192.168.100.1&lan_netmask=255.255.255.0&rip_enable=0&rip_multicast=1&rip_version=2&lan_proto=dhcp&dhcp_start=192.168.100.2&dhcp_end=192.168.1.254&dhcp_start_old=192.168.100.2&dhcp_end_old=192.168.1.254&pptp_wan_ipaddr=...&l2tp_wan_ipaddr=...&pppoe_wan_ipaddr=...&pptp_serv_ipaddr=10.0.0.138&l2tp_serv_ipaddr=&wan_dns1_pri=&wan_dns1_sec=&wan_proto=dhcp&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&repeater=0&repeater_an=0&dlna_autoip_en=0&tmp_lan_ipaddr=0.0.0.0&tmp_lan_netmask=0.0.0.0&tmp_lan_proto=null&tmp_rip_enable=null'
    elif hostip == '192.168.1.250':
        data = 'action=Apply&device_name=R8500%3Aping%20192.168.1.2&sysLANIPAddr1=192&sysLANIPAddr2=168&sysLANIPAddr3=1&sysLANIPAddr4=250&sysLANSubnetMask1=255&sysLANSubnetMask2=255&sysLANSubnetMask3=255&sysLANSubnetMask4=0&rip_direction=1&sysRIPVersion=Disabled&dhcp_server=dhcp_server&sysPoolStartingAddr4=2&sysPoolFinishAddr4=254&select=-1&arp_enable=disable&ipmac_token=0&dev_name=R8500&lan_ipaddr=192.168.1.250&lan_netmask=255.255.255.0&rip_enable=0&rip_multicast=1&rip_version=2&lan_proto=dhcp&dhcp_start=192.168.1.2&dhcp_end=192.168.1.254&dhcp_start_old=192.168.1.2&dhcp_end_old=192.168.1.254&pptp_wan_ipaddr=...&l2tp_wan_ipaddr=...&pppoe_wan_ipaddr=...&pptp_serv_ipaddr=10.0.0.138&l2tp_serv_ipaddr=&wan_dns1_pri=&wan_dns1_sec=&wan_proto=dhcp&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&repeater=0&repeater_an=0&dlna_autoip_en=0&tmp_lan_ipaddr=0.0.0.0&tmp_lan_netmask=0.0.0.0&tmp_lan_proto=null&tmp_rip_enable=null'
    else:
        data = 'action=Apply&device_name=R8500%3Aping%20192.168.0.2&sysLANIPAddr1=192&sysLANIPAddr2=168&sysLANIPAddr3=0&sysLANIPAddr4=1&sysLANSubnetMask1=255&sysLANSubnetMask2=255&sysLANSubnetMask3=255&sysLANSubnetMask4=0&rip_direction=1&sysRIPVersion=Disabled&dhcp_server=dhcp_server&sysPoolStartingAddr4=2&sysPoolFinishAddr4=254&select=-1&arp_enable=disable&ipmac_token=0&dev_name=R8500&lan_ipaddr=192.168.1.1&lan_netmask=255.255.255.0&rip_enable=0&rip_multicast=1&rip_version=2&lan_proto=dhcp&dhcp_start=192.168.1.2&dhcp_end=192.168.1.254&dhcp_start_old=192.168.1.2&dhcp_end_old=192.168.0.254&pptp_wan_ipaddr=...&l2tp_wan_ipaddr=...&pppoe_wan_ipaddr=...&pptp_serv_ipaddr=10.0.0.138&l2tp_serv_ipaddr=&wan_dns1_pri=&wan_dns1_sec=&wan_proto=dhcp&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&repeater=0&repeater_an=0&dlna_autoip_en=0&tmp_lan_ipaddr=0.0.0.0&tmp_lan_netmask=0.0.0.0&tmp_lan_proto=null&tmp_rip_enable=null'
    if console_type == 'cable':
        data = 'action=Apply&device_name=C7000-100NAS%3Bping 192.168.0.12&sysLANIPAddr1=192&sysLANIPAddr2=168&sysLANIPAddr3=0&sysLANIPAddr4=1&sysLANSubnetMask1=255&sysLANSubnetMask2=255&sysLANSubnetMask3=255&sysLANSubnetMask4=0&dhcp_server=dhcp_server&sysPoolStartingAddr4=10&sysPoolFinishAddr4=254&select=-1&device_name_tmp=C7000-100NAS%3Breboot&lan_ipaddr=192.168.0.1&lan_netmask=255.255.255.0&rip_enable=0&rip_multicast=1&rip_version=2&lan_proto=dhcp&dhcp_start=192.168.0.10&dhcp_end=192.168.0.254&dhcp_start_old=192.168.0.10&dhcp_end_old=192.168.0.254&pptp_wan_ipaddr=...&l2tp_wan_ipaddr=...&pppoe_wan_ipaddr=&pptp_serv_ipaddr=&l2tp_serv_ipaddr=&wan_dns1_pri=&wan_dns1_sec=&wan_proto=dhcp&wan_ipaddr=0.0.0.0&wan_netmask=0.0.0.0&repeater=0&repeater_an=0&dlna_autoip_en=0&tmp_lan_ipaddr=192.168.0.1&tmp_lan_netmask=0.0.0.0&tmp_lan_proto=null&tmp_rip_enable=null'
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
    tsharkCapture(interface='LAN',packetsize='',packetcount='',duration='30',protocol='icmp',file='F:/ATE_script/PSV/Log/pcap.cap')
    time.sleep(30)
    str = tsharkRead(optionV='YES',filter='icmp',packetfile='F:/ATE_script/PSV/Log/pcap.cap')
    assert str.find('Type: 0') == -1, "The function should not work." 
