from scipy.stats import signaltonoise
import xlrd
import numpy as np
from os import listdir, getcwd
from os.path import isfile, join

fi = [f for f in listdir(getcwd()) if f.endswith('.xlsx')]

for f in fi:
	xl_workbook = xlrd.open_workbook(f)
	xl_sheet = xl_workbook.sheet_by_index(0)
	b = xl_sheet.col_values(1)
	a = xl_sheet.col_values(0)
	l = a.index(900)
	r = a.index(1250)
	S = max(b)
	r = b[l:r + 1]
	N = max(r) - min(r)
	SNR = (S - N) / N
	print("{}: N: {}, S: {}, SNR: {}".format(f, N, S, SNR))