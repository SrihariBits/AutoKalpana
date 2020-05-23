from RagaGraph import constructRagaGraph
from ConstructGrams import constructGrams
#import winsound
import matplotlib.pyplot as plt
import csv
#import sounddevice as sd
import struct
import numpy as np
from scipy import signal as sg


twoGrams = []
fourGrams = []
eightGrams = []
sixteenGrams = []
twoGramGraph = {}
fourGramGraph = {}
eightGramGraph = {}
sixteenGramGraph = {}
RagaGraph = {}


if __name__ == '__main__':
	print("Program Begins")
	twoGrams, twoGramGraph, fourGrams, fourGramGraph, eightGrams, eightGramGraph, sixteenGrams, sixteenGramGraph = constructGrams(
	"1212342345676543456788")
	print(sixteenGrams)
	print(sixteenGramGraph)
	#winsound.Beep(260, 2000)

	x = []
	y = []

	with open('02-Mahaganapate-Nattai.pit.txt', 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
		    x.append(float(row[0]))
		    y.append(float(row[1]))

		f=open('test.wav','wb')

		for i in y:
			f.write(struct.pack('f',int(i)))
		f.close()

		'''
		plt.plot(x, y, label='Loaded from file!')
		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Interesting Graph\nCheck it out')
		plt.legend()
		plt.show()
		'''
