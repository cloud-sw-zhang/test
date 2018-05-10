''' [PSV-2016-0133] Unsafe Use of system()function in net-cgi  '''
''' anthor Cloud 2017-12-07'''
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
    log.info('step-1  Unsafe Use of "system () " function in "net-cgi"-----DUT should not execute the sheel  command(ping) by request HTTP packet)')
    url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
    if console_type == 'cable':
        Referer = host + 'BasicSettingsBottom.htm'
    else:
        Referer = host + 'BAS_ether.htm'
    headers = {
        'Host': hostip,
        'Cache-Control': 'max-age=0',
        'Origin': 'http://' + hostip,
        'Upgrade-Insecure-Requests': '1',
        'Authorization': Authorization,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': Referer,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    if hostip == '192.168.0.1':
        data ='apply=Apply&system_name=R8500&domain_name=&WANAssign=dhcp&DNSAssign=0&MACAssign=0&runtest=no&wan_proto=dhcp&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&wan_gateway=10.7.5.253&wan_dns_sel=0&wan_dns1_pri=10.7.5.253&wan_dns1_sec=...&wan_hwaddr_sel=0&wan_hwaddr_def=2C%3A30%3A33%3A51%3A84%3A3F&wan_hwaddr2=function%20toUpperCase%28%29%20%7B%20%5Bnative%20code%5D%20%7D&wan_hwaddr_pc=A0%3AD3%3AC1%3A24%3A18%3A5B&lan_ipaddr=192.168.0.1%60ping%2520192.168.0.2%60&lan_netmask=255.255.255.0&parental_control=0&ipv6_proto=disable'
    elif hostip == '192.168.1.250':
        data ='apply=Apply&system_name=R8500&domain_name=&WANAssign=dhcp&DNSAssign=0&MACAssign=0&runtest=no&wan_proto=dhcp&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&wan_gateway=10.7.5.253&wan_dns_sel=0&wan_dns1_pri=10.7.5.253&wan_dns1_sec=...&wan_hwaddr_sel=0&wan_hwaddr_def=2C%3A30%3A33%3A51%3A84%3A3F&wan_hwaddr2=function%20toUpperCase%28%29%20%7B%20%5Bnative%20code%5D%20%7D&wan_hwaddr_pc=A0%3AD3%3AC1%3A24%3A18%3A5B&lan_ipaddr=192.168.1.250%60ping%2520192.168.1.2%60&lan_netmask=255.255.255.0&parental_control=0&ipv6_proto=disable'
    else:
        data ='apply=Apply&system_name=R8500&domain_name=&WANAssign=dhcp&DNSAssign=0&MACAssign=0&runtest=no&wan_proto=dhcp&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&wan_gateway=10.7.5.253&wan_dns_sel=0&wan_dns1_pri=10.7.5.253&wan_dns1_sec=...&wan_hwaddr_sel=0&wan_hwaddr_def=2C%3A30%3A33%3A51%3A84%3A3F&wan_hwaddr2=function%20toUpperCase%28%29%20%7B%20%5Bnative%20code%5D%20%7D&wan_hwaddr_pc=A0%3AD3%3AC1%3A24%3A18%3A5B&lan_ipaddr=192.168.1.1%60ping%2520192.168.1.2%60&lan_netmask=255.255.255.0&parental_control=0&ipv6_proto=disable'
    if console_type == 'cable':
        data = 'apply=Apply&system_name=C7000-100NAS&domain_name=&WANAssign=dhcp&DNSAssign=0&MACAssign=0&runtest=no&wan_proto=dhcp&wan_ipaddr=10.11.1.19&wan_netmask=255.255.0.0&wan_gateway=10.11.0.1&wan_dns_sel=0&wan_dns1_pri=8.8.8.8&wan_dns1_sec=3.3.3.20&wan_dns1_thi=3.3.3.21&wan_hwaddr_sel=0&wan_hwaddr_def=00%3Acc%3Acc%3A30%3A92%3A03&wan_hwaddr2=00CCCC309203&wan_hwaddr_pc=a0%3Ad3%3Ac1%3A24%3A18%3A5b&lan_ipaddr=192.168.0.1%2560ping%252520192.168.0.10%2560&lan_netmask='
        post_url = host + 'goform/BasicSettingsBottom' + token
    else:
        post_url = host + 'ether.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    tsharkCapture(interface='LAN',packetsize='',packetcount='',duration='20',protocol='icmp',file='F:/ATE_script/PSV/Log/lan.pcap')
    time.sleep(20)
    str = tsharkRead(optionV='YES',filter='icmp',packetfile='F:/ATE_script/PSV/Log/lan.pcap')
    if str.find('Type: 0') == -1:
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "DUT should not execute the sheel  command" 
