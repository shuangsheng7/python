import pygame
import time
def main():
#1.创建一个窗口，用来显示内容
	screen = pygame.display.set_mode((480,852),0,32)
#2.创建一个和窗口大小相同的图片，用来充当背景
	background = pygame.image.load("./feiji/background.png")
#3.创建一个飞机图片
	hero = pygame.image.load("./feiji/hero1.png")
#3.把背景图片放到窗口中显示
	while True:
		screen.blit(background,(0,0))
		screen.blit(hero,(210,700))
		pygame.display.update()
		time.sleep(0.05)
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
if __name__ == "__main__":
	main()
