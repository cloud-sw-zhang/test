''' [PSV-2017-0317] Unauthenticated RCE through /cgi-bin/ urls '''
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
    log.info('step-1 Unauthenticated RCE through /cgi-bin/ urls')
    if console_type == 'cable':
        print 'This case NA'
        str = 'NA'
        assert str == 'pass', "The function should not work." 
    else:
        url = host + urlLogs
        token = getIDToken(url)
        if hostip == '192.168.0.1':
            data = 'ping 192.168.0.2'
        elif hostip == '192.168.100.1':
            data = 'ping 192.168.100.2'
        else:
            data = 'ping 192.168.1.2'
        post_url = host + 'cgi-bin/moo.cgi;sh'
        r = ''
        try:
            r = requests.post(post_url, data=data,auth=(user, passwd),timeout=5)
        except:
            time.sleep(1)
        if r != '': 
            log.info(r.text)
        tsharkCapture(interface='LAN',packetsize='',packetcount='',duration='30',protocol='icmp',file='F:/ATE_script/PSV/Log/pcap.cap')
        time.sleep(30)
        str = tsharkRead(optionV='YES',filter='icmp',packetfile='F:/ATE_script/PSV/Log/pcap.cap')
        assert str.find('Type: 0') == -1, "The function should not work." 
