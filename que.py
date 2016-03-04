#Python Thread Que

from collections import deque
from operator import itemgetter

class priority_dequeue:
	
	def __init__(self, initlist):
		self.curr_queue = initlist
		self.order_queue()

	def order_queue(self):
		print(self.curr_queue)
		self.curr_queue = deque(sorted(self.curr_queue, key=itemgetter(1)))

	def nextitem(self):
		return self.curr_queue.popleft()[0];

	def additem(self, item, priority=False):
		assert isinstance(item, (tuple, list))
		if len(item) != 2:
			raise IndexError ('expecting list or tuple of length 2')
		else:
			assert isinstance(item[1], int)
			if not priority:
				self.curr_queue.append(list(item))
			else:
				self.curr_queue.appendleft(list(item))
			self.order_queue()

x = priority_dequeue([['hello', 1], ['the', 3], ['world', 2]])
print(x.curr_queue)
print(x.nextitem())
x.additem(['hello', 2])
while x.curr_queue:
	print(x.next())

