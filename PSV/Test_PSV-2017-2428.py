'''[PSV-2017-2428] Post-Auth RCE via apmode)netmask paramter in WLG_ap_dual_band.htm '''
''' anthor Cloud 2018-01-04'''
'''v1.0 '''
from API._API import *

# #def test_step_0():
    # #log.info( 'step-0-0 dut loaddrfault wait 160s')
    # #aploaddefault()
    # #log.info( "step-0-1 AP Genie over leap done")
    # #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 Post-Auth RCE via apmode)netmask paramter in WLG_ap_dual_band.htm')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        page = 'WLG_ap_dual_band.htm'
        cgi = 'ap_mode.cgi'
        netmask = '255.255.255.0\n'
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {'Authorization': Authorization}
        payload = netmask.ljust(0x84, 'a')
        payload += 'dead' # R4
        payload += 'dead' # R5
        payload += 'dead' # R6
        payload += 'dead' # R7
        payload += 'dead' # R8
        payload += 'dead' # R9
        payload += 'dead' # R10
        payload += 'dead'
        payload += struct.pack("I", 0x94dc0)
        data = {
            'Apply':'ok',
            'enable_ap_mode':'enable_ap_mode',
            'enable_fixed_ip_setting':'enable_fixed_ip_setting',
            'WPethr1':'0',
            'WPethr2':'0',
            'WPethr3':'0',
            'WPethr4':'0',
            'WMask1':'0',
            'WMask2':'0',
            'WMask3':'0',
            'WMask4':'0',
            'WGateway1':'0',
            'WGateway2':'0',
            'WGateway3':'0',
            'WGateway4':'0',
            'DAddr1':'0',
            'DAddr2':'0',
            'DAddr3':'0',
            'DAddr4':'0',
            'PDAddr1':'',
            'PDAddr2':'',
            'PDAddr3':'',
            'PDAddr4':'',
            'apmode_ipaddr':'192.168.2.1',
            'apmode_netmask':payload,
            'apmode_gateway':'192.168.2.100',
            'apmode_dns_sel':'',
            'apmode_dns1_pri':'0.0.0.0',
            'apmode_dns1_sec':'...',
            'apmode_page':'1'
        }
        post_url = host + '%s' % cgi + token
        log.info(payload)
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.status_code)
        if r.status_code == 401 or r.status_code == 404:
            case1 = 'pass'
        else:
            case1 = 'fail'
        time.sleep(2)
        r1 = requests.get('http://' + hostip + '/%s' % (page), headers=headers)
        log.info(r1.status_code)
        if r1.status_code == 401 or r1.status_code == 404:
            case2 = 'pass'
        else:
            case2 = 'fail'
        if case1 == 'pass' and case2 == 'pass':
            case = 'pass'
        else:
            case = 'fail'
    assert case == 'pass', "The function should work." 
