import pygame
from pygame.locals import *
import time

class HeroPlane(object):
	def __init__(self,screen_temp):
		self.x = 210
		self.y = 700
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/hero1.png")		
		self.bullet_list = []
	
	def display(self):		
		self.screen.blit(self.image,(self.x,self.y))
	
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()
	def move_left(self):
		self.x -= 5

	def move_right(self):
		self.x += 5
	
	def move_down(self):
		self.y += 5

	def move_up(self):
		self.y -= 5
	
	def fire(self):
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))
		
class Bullet(object):
	def __init__(self,screen_temp,x,y):
		self.x = x + 40
		self.y = y - 20
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/bullet.png")
	
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
	
	def move(self):
		self.y -= 15
def key_control(hero_temp):
	for event in pygame.event.get():
		#判断是否按了退出按钮
		if event.type == pygame.QUIT:
			print("exit")
			exit()
		#判断是否按下了键
		elif event.type == KEYDOWN:
			#检测按键是否是a或者left
			if event.key == K_a or event.key == K_LEFT:
				print("left")
				hero_temp.move_left()
			#检测按键是否是d或者right
			elif event.key == K_d or event.key == K_RIGHT:
				print("right")
				hero_temp.move_right()
			#检测按键是否是s或者down
			elif event.key == K_s or event.key == K_DOWN:
				print("down")
				hero_temp.move_down()
			#检测按键是否是w或者up
			elif event.key == K_w or event.key == K_UP:
				print("up")
				hero_temp.move_up()
			#检测按键是否是空格键
			elif event.key == K_SPACE:
				print("space")
				hero_temp.fire()
def main():
#1.创建一个窗口，用来显示内容
	screen = pygame.display.set_mode((480,852),0,32)
#2.创建一个和窗口大小相同的图片，用来充当背景
	background = pygame.image.load("./feiji/background.png")
#3.创建一个飞机对象
	hero = HeroPlane(screen)
#3.把背景图片放到窗口中显示
	while True:
		screen.blit(background,(0,0))
		hero.display()
		pygame.display.update()
		#获取事件
		key_control(hero)
		time.sleep(0.01)
if __name__ == "__main__":
	main()
