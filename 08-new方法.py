class Dog(object):
	def __init__(self):
		print("----init方法----")
	def __del__(self):
		print("----del方法----")
	def __str__(self):
		return "对象的描述信息"
		print("----str方法----")
	def __new__(cls):#cls此时是Dog指向的那个类对象
		print("----new方法----")
		return object.__new__(cls)#调用基类中的new方法来创建对象

xtq = Dog()

