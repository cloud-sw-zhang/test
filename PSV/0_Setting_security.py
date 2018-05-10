''' This script can burn dut ether mac'''
''' anthor Cloud 2017-11-24'''
'''v1.0 '''
from API._API import *
print hostip
print console_type
print TimeLoad
print ProjectName


print 'step-1: DUT loaddefault  && Genie_overleap'
aploaddefault()
#time.sleep(TimeLoad)
for i in range(1,TimeLoad):
	time.sleep(1)
	print i

Genie_overleap('com1',consoletype)
print 'step-1: DUT loaddefault done'

print 'step-2: burn dut ether mac'
sendCommandListAndGetReturnUntil('com1', ['burnsku 9', 'burnethermac 00D0591A2B3B','reboot'],'#')
#time.sleep(TimeLoad)
for i in range(1,TimeLoad):
	time.sleep(1)
	print i

print 'step-2: burn dut ethernet mac done'

print 'test done'