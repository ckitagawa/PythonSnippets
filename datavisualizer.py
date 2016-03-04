import csv
import numpy as np
import matplotlib.pyplot as plt

class data_vis:

	def __init__(self):
		return 

	def load(self, file, delim):
		self.file = file
		with open(file, 'r') as csvf:
			reader = csv.reader(csvf, delimiter=delim)
			self.data = list(reader)
		return

	def headers(self):
		for header in zip(self.data[0], range(len(self.data[0]))):
			print(header)
		self.hrow = self.data[0]
		return

	def selectrows(self, x, y, r=None):
		self.x = [elem[x] for elem in self.data[1:100]]
		self.y = [elem[y] for elem in self.data[1:100]]
		self.xlabel = self.hrow[x]
		self.ylabel = self.hrow[y]
		if r != None:
			self.r = [elem[r] for elem in self.data]
		return 

	def plot(self):
		plt.scatter(self.x, self.y)
		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)
		plt.title(self.file)
		plt.legend()
		plt.show()

if __name__ == '__main__':
	d = data_vis()
	d.load("D:\\Downloads\\CALGIS.ADDRESS.csv", ',')
	d.headers()
	x = int(input("x> "))
	y = int(input("y> "))
	d.selectrows(x, y)
	d.plot()
