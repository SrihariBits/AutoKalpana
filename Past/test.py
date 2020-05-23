import struct
import numpy as np
from scipy import signal as sg

sampling_rate= 44100 #freq changes
'''
freq=440
samples=144100
x=np.arange(samples)

y=100*np.sin(2*np.pi*freq*x/sampling_rate)
'''



f=open('test.wav','wb')

for i in y:
	f.write(struct.pack('b',int(i)))
f.close()
