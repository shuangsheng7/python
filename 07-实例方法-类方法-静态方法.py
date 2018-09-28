class Game(object):
	num = 0 #类属性
	def __init__(self):#实例方法
		self.name = "laowang"#实例属性
	#类方法
	@classmethod
	def add_num(cls):
		cls.num = 100
	#静态方法
	@staticmethod
	def print_menu():
		print("静态方法被调用")

game = Game()
#Game.add_num()#类方法可以通过类名调用
game.add_num()#类方法也可以通过这个类创建的实例对象去调用
print(Game.num)

#Game.print_menu()#静态方法可以通过类名调用
game.print_menu()#静态方法也可以通过这个类创建的实例对象去调用		
