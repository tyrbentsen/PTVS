import time

class C:
	def f(self):
			for i in range(10000):
				time.sleep(0)

a = C()
a.f()
