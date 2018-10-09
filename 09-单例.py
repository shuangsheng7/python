class Dog(object):
	#创建一个类属性初始值为空用来判断是否为第一次创建
	#并用此类属性接收第一次创建出来的对象的引用
	__instance = None

	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)	
		return cls.__instance


a = Dog()
print(id(a))
b = Dog()
print(id(b))

