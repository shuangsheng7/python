class Dog(object):
	#创建一个类属性初始值为空用来判断是否为第一次创建
	#并用此类属性接收第一次创建出来的对象的引用
	__instance = None
	#创建一个类属性初始值为False，在init方法中用类属性判断是否为第一次初始化
	#并且在第一次初始化后将此类属性的值更改为True
	__init_flag = False

	def __new__(cls,name):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)	
		return cls.__instance
	def __init__(self,name):
		if Dog.__init_flag == False:
			self.name = name
			Dog.__init_flag = True
	
a = Dog("旺财")
print(id(a))
print(a.name)
b = Dog("啸天犬")
print(id(b))
print(b.name)
print(a.name)
