class Base(object):
	def test(self):
		print("----Base----")

class A(Base):
	def test(self):
		print("----test1----")
class B(Base):
	def test(self):
		print("----test2----")
class C(A,B):
	def test(self):
		print("----test3----")

c = C()
c.test()
print(C.__mro__)
