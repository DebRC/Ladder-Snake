#importing modules
import pygame
import sys
import random
import time
from pygame import mixer
from pygame.locals import *

#initializing pygame
pygame.init()

#cursor
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

#resolution of the screen
WIDTH=700
HEIGHT=650
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#caption and icon
pygame.display.set_caption("Ladder & Snake")
icon=pygame.image.load("Images\\icon.png")
pygame.display.set_icon(icon)

red=pygame.image.load("Images\\red.png")
blue=pygame.image.load("Images\\blue.png")
yellow=pygame.image.load("Images\\yellow.png")
green=pygame.image.load("Images\\green.png")
blue_yellow=pygame.image.load("Images\\blue-yellow.png")
red_green=pygame.image.load("Images\\red-green.png")
red_blue=pygame.image.load("Images\\red-blue.png")
green_blue=pygame.image.load("Images\\green-blue.png")
yellow_red=pygame.image.load("Images\\yellow-red.png")

mixer.music.load("Sounds\\start_music.ogg")
mixer.music.play(-1)

background = pygame.image.load("Images\\game_mode.jpg")
screen.blit(background,(0,0))
player_number=0
game_mode=True
while game_mode:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			click=pygame.mouse.get_pos()
			if (click[0]>=158 and click[0]<=302 and click[1]>=221 and click[1]<=291):
				button_sound=mixer.Sound("Sounds\\button.wav")
				button_sound.play()
				player_number=1
				game_mode=False
			elif (click[0]>=394 and click[0]<=532 and click[1]>=221 and click[1]<=291):
				button_sound=mixer.Sound("Sounds\\button.wav")
				button_sound.play()
				player_number=2
				game_mode=False
	pygame.display.update()

if(player_number==1):
	background = pygame.image.load("Images\\color_choice.jpg")
	screen.blit(background,(0,0))
	color_choice=True
	while color_choice:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			if event.type==pygame.MOUSEBUTTONDOWN:
				click=pygame.mouse.get_pos()
				if (click[0]>=168 and click[0]<=229 and click[1]>=249 and click[1]<=310):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player1_choice=red
					comp_choice=blue
					merge=red_blue
					mixer.music.stop()
					color_choice=False
				elif (click[0]>=277 and click[0]<=339 and click[1]>=249 and click[1]<=312):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player1_choice=blue
					comp_choice=yellow
					merge=blue_yellow
					mixer.music.stop()
					color_choice=False
				elif (click[0]>=385 and click[0]<=445 and click[1]>=246 and click[1]<=307):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player1_choice=yellow
					comp_choice=red
					merge=yellow_red
					mixer.music.stop()
					color_choice=False
				elif (click[0]>=490 and click[0]<=552 and click[1]>=247 and click[1]<=309):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player1_choice=green
					comp_choice=red
					merge=red_green
					mixer.music.stop()
					color_choice=False
		pygame.display.update()

	#background image
	background = pygame.image.load("Images\\background.jpg")
	screen.blit(background,(0,0))

	#player
	player1_color=player1_choice
	player1_score=0
	player1_x=19
	player1_y=560
	screen.blit(player1_color,(player1_x,player1_y))

	#computer
	comp_color=comp_choice
	comp_score=0
	comp_x=19
	comp_y=600
	screen.blit(comp_color,(comp_x,comp_y))

	#pos
	guti_x=[19,89,159,229,299,369,439,509,579,649]
	guti_y=[506,451,396,341,286,231,176,121,66,11]

	#dice
	one=pygame.image.load("Images\\one.png")
	two=pygame.image.load("Images\\two.png")
	three=pygame.image.load("Images\\three.png")
	four=pygame.image.load("Images\\four.png")
	five=pygame.image.load("Images\\five.png")
	six=pygame.image.load("Images\\six.png")
	screen.blit(one,(621,581))

	#font
	font1=pygame.font.Font("Fonts\\font1.ttf",50, bold=True, italic=False)
	font2=pygame.font.Font("Fonts\\font2.otf",23, bold=True, italic=False)
	font3=pygame.font.Font("Fonts\\font3.ttf",25, bold=True, italic=True)
	player_label=font3.render("Your Score:- "+str(player1_score), 1, (153, 204, 255))
	screen.blit(player_label,(60,565))
	comp_label=font3.render("Computer's Score:- "+str(comp_score), 1, (153, 204, 255))
	screen.blit(comp_label,(60,605))
	label=font3.render("Your Turn", 1, (255, 204, 0))
	screen.blit(label,(415,610))

	#sound effects
	dice_sound=mixer.Sound("Sounds\\dice_sound.wav")
	snake_sound=mixer.Sound("Sounds\\snake.ogg")
	ladder_sound=mixer.Sound("Sounds\\ladder.wav")

	#basics
	turn=0
	clock=pygame.time.Clock()
	game_over=False

	while(1):
		pygame.mouse.set_cursor(*pygame.cursors.tri_left)
		if(turn%2==0):
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				if event.type==pygame.MOUSEBUTTONDOWN:
					click=pygame.mouse.get_pos()
					print(click)
					dice_x=click[0]
					dice_y=click[1]
					if (dice_x>=621 and dice_x<=653 and dice_y>=581 and dice_y<=613):
						pygame.mouse.set_cursor(*pygame.cursors.diamond)
						screen.blit(background,(0,0))
						dice_sound.play()
						time.sleep(2)
						number=random.randint(1,6)
						print("dice rolled:- ",number)
						if(number==1):
							screen.blit(one,(621,581))
						elif(number==2):
							screen.blit(two,(621,581))
						elif(number==3):
							screen.blit(three,(621,581))
						elif(number==4):
							screen.blit(four,(621,581))
						elif(number==5):
							screen.blit(five,(621,581))
						elif(number==6):
							screen.blit(six,(621,581))
						label=font2.render("You rolled "+str(number), 1, (255, 102, 153))
						screen.blit(label,(369,565))
						player1_score+=number
						if(player1_score==3):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=17
						elif(player1_score==6):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=8
						elif(player1_score==11):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=17
						elif(player1_score==15):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=19
						elif(player1_score==17):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=57
						elif(player1_score==22):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=15
						elif(player1_score==38):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=21
						elif(player1_score==49):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=18
						elif(player1_score==57):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=19
						elif(player1_score==61):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=17
						elif(player1_score==73):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=13
						elif(player1_score==81):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=17
						elif(player1_score==88):
							ladder_sound.play()
							label=font2.render("You found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=3
						elif(player1_score==8):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=4
						elif(player1_score==18):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=17
						elif(player1_score==26):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=16
						elif(player1_score==39):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=34
						elif(player1_score==51):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=37
						elif(player1_score==54):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=18
						elif(player1_score==56):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=55
						elif(player1_score==60):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=37
						elif(player1_score==75):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=47
						elif(player1_score==90):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=42
						elif(player1_score==85):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=26
						elif(player1_score==83):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=38
						elif(player1_score==92):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=67
						elif(player1_score==97):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=10
						elif(player1_score==99):
							snake_sound.play()
							label=font2.render("A snake ate you!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=36
						if(player1_score>100):
							player1_score-=number
						#x position
						if(player1_score==1 or player1_score==20 or player1_score==21 or player1_score==40 or player1_score==41 or player1_score==80 or player1_score==100):
							player1_x=guti_x[0]
						elif(player1_score==2 or player1_score==19 or player1_score==42 or player1_score==59 or player1_score==62 or player1_score==79 or player1_score==82):
							player1_x=guti_x[1]
						elif(player1_score==23 or player1_score==43 or player1_score==58 or player1_score==63 or player1_score==78 or player1_score==98):
							player1_x=guti_x[2]
						elif(player1_score==4 or player1_score==24 or player1_score==37 or player1_score==44 or player1_score==64 or player1_score==77 or player1_score==84):
							player1_x=guti_x[3]
						elif(player1_score==5 or player1_score==16 or player1_score==25 or player1_score==36 or player1_score==45 or player1_score==65 or player1_score==76 or player1_score==96):
							player1_x=guti_x[4]
						elif(player1_score==35 or player1_score==46 or player1_score==55 or player1_score==66 or player1_score==86 or player1_score==95):
							player1_x=guti_x[5]
						elif(player1_score==7 or player1_score==14 or player1_score==27 or player1_score==34 or player1_score==47 or player1_score==67 or player1_score==74 or player1_score==87 or player1_score==94):
							player1_x=guti_x[6]
						elif(player1_score==13 or player1_score==28 or player1_score==33 or player1_score==48 or player1_score==53 or player1_score==68 or player1_score==93):
							player1_x=guti_x[7]
						elif(player1_score==9 or player1_score==12 or player1_score==29 or player1_score==32 or player1_score==52 or player1_score==69 or player1_score==72 or player1_score==89):
							player1_x=guti_x[8]
						elif(player1_score==10 or player1_score==30 or player1_score==31 or player1_score==50 or player1_score==70 or player1_score==71 or player1_score==91):
							player1_x=guti_x[9]
						#y position
						if(player1_score==1 or player1_score==2 or player1_score==4 or player1_score==5 or player1_score==7 or player1_score==9 or player1_score==10):
							player1_y=guti_y[0]
						elif(player1_score==20 or player1_score==19 or player1_score==16 or player1_score==14 or player1_score==13 or player1_score==12):
							player1_y=guti_y[1]
						elif(player1_score==21 or player1_score==23 or player1_score==24 or player1_score==25 or player1_score==27 or player1_score==28 or player1_score==29 or player1_score==30):
							player1_y=guti_y[2]
						elif(player1_score==40 or player1_score==37 or player1_score==36 or player1_score==35 or player1_score==34 or player1_score==33 or player1_score==32 or player1_score==31):
							player1_y=guti_y[3]
						elif(player1_score==41 or player1_score==42 or player1_score==43 or player1_score==44 or player1_score==45 or player1_score==46 or player1_score==47 or player1_score==48 or player1_score==50):
							player1_y=guti_y[4]
						elif(player1_score==59 or player1_score==58 or player1_score==55 or player1_score==53 or player1_score==52):
							player1_y=guti_y[5]
						elif(player1_score==62 or player1_score==63 or player1_score==64 or player1_score==65 or player1_score==66 or player1_score==67 or player1_score==68 or player1_score==69 or player1_score==70):
							player1_y=guti_y[6]
						elif(player1_score==80 or player1_score==79 or player1_score==78 or player1_score==77 or player1_score==76 or player1_score==74 or player1_score==72 or player1_score==71):
							player1_y=guti_y[7]
						elif(player1_score==82 or player1_score==84 or player1_score==86 or player1_score==87 or player1_score==89):
							player1_y=guti_y[8]
						elif(player1_score==100 or player1_score==98 or player1_score==96 or player1_score==95 or player1_score==94 or player1_score==93 or player1_score==91):
							player1_y=guti_y[9]
						print("your score:- ",player1_score)
						if(player1_score==comp_score):
							screen.blit(merge,(player1_x,player1_y))
							screen.blit(comp_color,(19,600))
							screen.blit(player1_color,(19,560))
						else:
							screen.blit(comp_color,(comp_x,comp_y))
							screen.blit(player1_color,(player1_x,player1_y))
							screen.blit(comp_color,(19,600))
							screen.blit(player1_color,(19,560))
						turn+=1
						player_label=font3.render("Your Score:- "+str(player1_score), 1, (153, 204, 255))
						screen.blit(player_label,(60,565))
						comp_label=font3.render("Computer's Score:- "+str(comp_score), 1, (153, 204, 255))
						screen.blit(comp_label,(60,605))
						label=font3.render("Computer's Turn", 1, (255, 204, 0))
						screen.blit(label,(360,610))
			pygame.display.update()
		elif(turn%2!=0):
			time.sleep(1)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
			number=random.randint(1,6)
			screen.blit(background,(0,0))
			dice_sound.play()
			time.sleep(2)
			label=font2.render("Computer rolled "+str(number), 1, (255, 102, 153))
			screen.blit(label,(369,565))
			if(number==1):
				screen.blit(one,(621,581))
			elif(number==2):
				screen.blit(two,(621,581))
			elif(number==3):
				screen.blit(three,(621,581))
			elif(number==4):
				screen.blit(four,(621,581))
			elif(number==5):
				screen.blit(five,(621,581))
			elif(number==6):
				screen.blit(six,(621,581))
			comp_score+=number
			print("dice rolled:- ",number)
			if(comp_score==3):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=17
			elif(comp_score==6):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=8
			elif(comp_score==11):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=17
			elif(comp_score==15):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=19
			elif(comp_score==17):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=57
			elif(comp_score==22):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=15
			elif(comp_score==38):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=21
			elif(comp_score==49):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=18
			elif(comp_score==57):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=19
			elif(comp_score==61):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=17
			elif(comp_score==73):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=13
			elif(comp_score==81):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=17
			elif(comp_score==88):
				ladder_sound.play()
				label=font2.render("Computer found a ladder!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score+=3
			if(comp_score==8):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=4
			elif(comp_score==18):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=17
			elif(comp_score==26):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=16
			elif(comp_score==39):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=34
			elif(comp_score==51):
				snake_sound.play()
				ladder_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=37
			elif(comp_score==54):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=18
			elif(comp_score==56):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=55
			elif(comp_score==60):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=37
			elif(comp_score==75):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=47
			elif(comp_score==90):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=42
			elif(comp_score==85):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=26
			elif(comp_score==83):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=38
			elif(comp_score==92):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=67
			elif(comp_score==97):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=10
			elif(comp_score==99):
				snake_sound.play()
				label=font2.render("A snake ate computer!", 1, (255, 102, 153))
				screen.blit(label,(326,585))
				comp_score-=36
			if(comp_score>100):
				comp_score-=number
			if(comp_score==1 or comp_score==20 or comp_score==21 or comp_score==40 or comp_score==41 or comp_score==80 or comp_score==100):
				comp_x=guti_x[0]
			elif(comp_score==2 or comp_score==19 or comp_score==42 or comp_score==59 or comp_score==62 or comp_score==79 or comp_score==82):
				comp_x=guti_x[1]
			elif(comp_score==23 or comp_score==43 or comp_score==58 or comp_score==63 or comp_score==78 or comp_score==98):
				comp_x=guti_x[2]
			elif(comp_score==4 or comp_score==24 or comp_score==37 or comp_score==44 or comp_score==64 or comp_score==77 or comp_score==84):
				comp_x=guti_x[3]
			elif(comp_score==5 or comp_score==16 or comp_score==25 or comp_score==36 or comp_score==45 or comp_score==65 or comp_score==76 or comp_score==96):
				comp_x=guti_x[4]
			elif(comp_score==35 or comp_score==46 or comp_score==55 or comp_score==66 or comp_score==86 or comp_score==95):
				comp_x=guti_x[5]
			elif(comp_score==7 or comp_score==14 or comp_score==27 or comp_score==34 or comp_score==47 or comp_score==67 or comp_score==74 or comp_score==87 or comp_score==94):
				comp_x=guti_x[6]
			elif(comp_score==13 or comp_score==28 or comp_score==33 or comp_score==48 or comp_score==53 or comp_score==68 or comp_score==93):
				comp_x=guti_x[7]
			elif(comp_score==9 or comp_score==12 or comp_score==29 or comp_score==32 or comp_score==52 or comp_score==69 or comp_score==72 or comp_score==89):
				comp_x=guti_x[8]
			elif(comp_score==10 or comp_score==30 or comp_score==31 or comp_score==50 or comp_score==70 or comp_score==71 or comp_score==91):
				comp_x=guti_x[9]
			if(comp_score==1 or comp_score==2 or comp_score==4 or comp_score==5 or comp_score==7 or comp_score==9 or comp_score==10):
				comp_y=guti_y[0]
			elif(comp_score==20 or comp_score==19 or comp_score==16 or comp_score==14 or comp_score==13 or comp_score==12):
				comp_y=guti_y[1]
			elif(comp_score==21 or comp_score==23 or comp_score==24 or comp_score==25 or comp_score==27 or comp_score==28 or comp_score==29 or comp_score==30):
				comp_y=guti_y[2]
			elif(comp_score==40 or comp_score==37 or comp_score==36 or comp_score==35 or comp_score==34 or comp_score==33 or comp_score==32 or comp_score==31):
				comp_y=guti_y[3]
			elif(comp_score==41 or comp_score==42 or comp_score==43 or comp_score==44 or comp_score==45 or comp_score==46 or comp_score==47 or comp_score==48 or comp_score==50):
				comp_y=guti_y[4]
			elif(comp_score==59 or comp_score==58 or comp_score==55 or comp_score==53 or comp_score==52):
				comp_y=guti_y[5]
			elif(comp_score==62 or comp_score==63 or comp_score==64 or comp_score==65 or comp_score==66 or comp_score==67 or comp_score==68 or comp_score==69 or comp_score==70):
				comp_y=guti_y[6]
			elif(comp_score==80 or comp_score==79 or comp_score==78 or comp_score==77 or comp_score==76 or comp_score==74 or comp_score==72 or comp_score==71):
				comp_y=guti_y[7]
			elif(comp_score==82 or comp_score==84 or comp_score==86 or comp_score==87 or comp_score==89):
				comp_y=guti_y[8]
			elif(comp_score==100 or comp_score==98 or comp_score==96 or comp_score==95 or comp_score==94 or comp_score==93 or comp_score==91):
				comp_y=guti_y[9]
			print("Computer score",comp_score)
			if(player1_score==comp_score):
				screen.blit(merge,(player1_x,player1_y))
				screen.blit(comp_color,(19,600))
				screen.blit(player1_color,(19,560))
			else:
				screen.blit(comp_color,(comp_x,comp_y))
				screen.blit(player1_color,(player1_x,player1_y))
				screen.blit(comp_color,(19,600))
				screen.blit(player1_color,(19,560))
			player_label=font3.render("Your Score:- "+str(player1_score), 1, (153, 204, 255))
			screen.blit(player_label,(60,565))
			comp_label=font3.render("Computer's Score:- "+str(comp_score), 1, (153, 204, 255))
			screen.blit(comp_label,(60,605))
			label=font3.render("Your Turn", 1, (255, 204, 0))
			screen.blit(label,(415,610))
			turn+=1
			if(comp_score==100 or player1_score==100):
				over=mixer.Sound("Sounds\\gameover.wav")
				over.play()
				break
			pygame.display.update()
	while(1):
		background = pygame.image.load("Images\\starter.jpg")
		screen.blit(background,(0,0))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		if(comp_score==100 and player1_score==100):
				label=font1.render("It's a Draw", 1, (0, 255, 204))
				screen.blit(label,(240,300))
		elif(comp_score==100):
			label=font1.render("Game Over! Computer Won.", 1, (0, 255, 204))
			screen.blit(label,(65,274))
		elif(player1_score==100):
			label=font1.render("Congratulations! You Won.", 1, (0, 255, 204))
			screen.blit(label,(60,274))
		pygame.display.update()
elif(player_number==2):
	background = pygame.image.load("Images\\color_choice_player1.jpg")
	screen.blit(background,(0,0))
	color_choice_player1=True

	while color_choice_player1:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			if event.type==pygame.MOUSEBUTTONDOWN:
				click=pygame.mouse.get_pos()
				if (click[0]>=168 and click[0]<=229 and click[1]>=249 and click[1]<=310):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player1_choice=red
					color_choice_player1=False
				elif (click[0]>=277 and click[0]<=339 and click[1]>=249 and click[1]<=312):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player1_choice=blue
					color_choice_player1=False
				elif (click[0]>=385 and click[0]<=445 and click[1]>=246 and click[1]<=307):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player1_choice=yellow
					color_choice_player1=False
				elif (click[0]>=490 and click[0]<=552 and click[1]>=247 and click[1]<=309):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player1_choice=green
					color_choice_player1=False
		pygame.display.update()

	background = pygame.image.load("Images\\color_choice_player2.jpg")
	screen.blit(background,(0,0))
	color_choice_player2=True

	while color_choice_player2:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			if event.type==pygame.MOUSEBUTTONDOWN:
				click=pygame.mouse.get_pos()
				if (click[0]>=168 and click[0]<=229 and click[1]>=249 and click[1]<=310):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player2_choice=red
					mixer.music.stop()
					color_choice_player2=False
				elif (click[0]>=277 and click[0]<=339 and click[1]>=249 and click[1]<=312):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player2_choice=blue
					mixer.music.stop()
					color_choice_player2=False
				elif (click[0]>=385 and click[0]<=445 and click[1]>=246 and click[1]<=307):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player2_choice=yellow
					mixer.music.stop()
					color_choice_player2=False
				elif (click[0]>=490 and click[0]<=552 and click[1]>=247 and click[1]<=309):
					button_sound=mixer.Sound("Sounds\\button.wav")
					button_sound.play()
					player2_choice=green
					mixer.music.stop()
					color_choice_player2=False
		pygame.display.update()

	#background image
	background = pygame.image.load("Images\\background.jpg")
	screen.blit(background,(0,0))

	#player
	player1_color=player1_choice
	player1_score=0
	player1_x=19
	player1_y=560
	screen.blit(player1_color,(player1_x,player1_y))

	#Player 2
	player2_color=player2_choice
	player2_score=0
	player2_x=19
	player2_y=600
	screen.blit(player2_color,(player2_x,player2_y))

	if(player1_color==red and player2_color==green):
		merge=red_green
	if(player1_color==green and player2_color==red):
		merge=red_green
	if(player1_color==blue and player2_color==red):
		merge=red_blue
	if(player1_color==red and player2_color==blue):
		merge=red_blue
	if(player1_color==blue and player2_color==yellow):
		merge=blue_yellow
	if(player1_color==yellow and player2_color==blue):
		merge=blue_yellow
	if(player1_color==green and player2_color==blue):
		merge=green_blue
	if(player1_color==blue and player2_color==green):
		merge=green_blue
	if(player1_color==yellow and player2_color==red):
		merge=yellow_red
	if(player1_color==red and player2_color==yellow):
		merge=yellow_red

	#pos
	guti_x=[19,89,159,229,299,369,439,509,579,649]
	guti_y=[506,451,396,341,286,231,176,121,66,11]

	#dice
	one=pygame.image.load("Images\\one.png")
	two=pygame.image.load("Images\\two.png")
	three=pygame.image.load("Images\\three.png")
	four=pygame.image.load("Images\\four.png")
	five=pygame.image.load("Images\\five.png")
	six=pygame.image.load("Images\\six.png")
	screen.blit(one,(621,581))

	#font
	font1=pygame.font.Font("Fonts\\font1.ttf",50, bold=True, italic=False)
	font2=pygame.font.Font("Fonts\\font2.otf",23, bold=True, italic=False)
	font3=pygame.font.Font("Fonts\\font3.ttf",25, bold=True, italic=True)
	player_label=font3.render("Player 1's Score:- "+str(player1_score), 1, (153, 204, 255))
	screen.blit(player_label,(60,565))
	player2_label=font3.render("Player 2's Score:- "+str(player2_score), 1, (153, 204, 255))
	screen.blit(player2_label,(60,605))
	label=font3.render("Player 1's Turn", 1, (255, 204, 0))
	screen.blit(label,(415,610))

	#sound effects
	dice_sound=mixer.Sound("Sounds\\dice_sound.wav")
	snake_sound=mixer.Sound("Sounds\\snake.ogg")
	ladder_sound=mixer.Sound("Sounds\\ladder.wav")

	#basics
	turn=0
	clock=pygame.time.Clock()
	game_over=False

	while(1):
		pygame.mouse.set_cursor(*pygame.cursors.tri_left)
		if(turn%2==0):
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				if event.type==pygame.MOUSEBUTTONDOWN:
					click=pygame.mouse.get_pos()
					print(click)
					dice_x=click[0]
					dice_y=click[1]
					if (dice_x>=621 and dice_x<=653 and dice_y>=581 and dice_y<=613):
						pygame.mouse.set_cursor(*pygame.cursors.diamond)
						screen.blit(background,(0,0))
						dice_sound.play()
						time.sleep(2)
						number=random.randint(1,6)
						print("dice rolled:- ",number)
						if(number==1):
							screen.blit(one,(621,581))
						elif(number==2):
							screen.blit(two,(621,581))
						elif(number==3):
							screen.blit(three,(621,581))
						elif(number==4):
							screen.blit(four,(621,581))
						elif(number==5):
							screen.blit(five,(621,581))
						elif(number==6):
							screen.blit(six,(621,581))
						label=font2.render("Player 1 rolled "+str(number), 1, (255, 102, 153))
						screen.blit(label,(369,565))
						player1_score+=number
						if(player1_score==3):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=17
						elif(player1_score==6):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=8
						elif(player1_score==11):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=17
						elif(player1_score==15):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=19
						elif(player1_score==17):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=57
						elif(player1_score==22):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=15
						elif(player1_score==38):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=21
						elif(player1_score==49):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=18
						elif(player1_score==57):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=19
						elif(player1_score==61):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=17
						elif(player1_score==73):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=13
						elif(player1_score==81):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=17
						elif(player1_score==88):
							ladder_sound.play()
							label=font2.render("Player 1 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score+=3
						elif(player1_score==8):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=4
						elif(player1_score==18):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=17
						elif(player1_score==26):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=16
						elif(player1_score==39):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=34
						elif(player1_score==51):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=37
						elif(player1_score==54):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=18
						elif(player1_score==56):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=55
						elif(player1_score==60):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=37
						elif(player1_score==75):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=47
						elif(player1_score==90):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=42
						elif(player1_score==85):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=26
						elif(player1_score==83):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=38
						elif(player1_score==92):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=67
						elif(player1_score==97):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=10
						elif(player1_score==99):
							snake_sound.play()
							label=font2.render("A snake ate Player 1!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player1_score-=36
						if(player1_score>100):
							player1_score-=number
						#x position
						if(player1_score==1 or player1_score==20 or player1_score==21 or player1_score==40 or player1_score==41 or player1_score==80 or player1_score==100):
							player1_x=guti_x[0]
						elif(player1_score==2 or player1_score==19 or player1_score==42 or player1_score==59 or player1_score==62 or player1_score==79 or player1_score==82):
							player1_x=guti_x[1]
						elif(player1_score==23 or player1_score==43 or player1_score==58 or player1_score==63 or player1_score==78 or player1_score==98):
							player1_x=guti_x[2]
						elif(player1_score==4 or player1_score==24 or player1_score==37 or player1_score==44 or player1_score==64 or player1_score==77 or player1_score==84):
							player1_x=guti_x[3]
						elif(player1_score==5 or player1_score==16 or player1_score==25 or player1_score==36 or player1_score==45 or player1_score==65 or player1_score==76 or player1_score==96):
							player1_x=guti_x[4]
						elif(player1_score==35 or player1_score==46 or player1_score==55 or player1_score==66 or player1_score==86 or player1_score==95):
							player1_x=guti_x[5]
						elif(player1_score==7 or player1_score==14 or player1_score==27 or player1_score==34 or player1_score==47 or player1_score==67 or player1_score==74 or player1_score==87 or player1_score==94):
							player1_x=guti_x[6]
						elif(player1_score==13 or player1_score==28 or player1_score==33 or player1_score==48 or player1_score==53 or player1_score==68 or player1_score==93):
							player1_x=guti_x[7]
						elif(player1_score==9 or player1_score==12 or player1_score==29 or player1_score==32 or player1_score==52 or player1_score==69 or player1_score==72 or player1_score==89):
							player1_x=guti_x[8]
						elif(player1_score==10 or player1_score==30 or player1_score==31 or player1_score==50 or player1_score==70 or player1_score==71 or player1_score==91):
							player1_x=guti_x[9]
						#y position
						if(player1_score==1 or player1_score==2 or player1_score==4 or player1_score==5 or player1_score==7 or player1_score==9 or player1_score==10):
							player1_y=guti_y[0]
						elif(player1_score==20 or player1_score==19 or player1_score==16 or player1_score==14 or player1_score==13 or player1_score==12):
							player1_y=guti_y[1]
						elif(player1_score==21 or player1_score==23 or player1_score==24 or player1_score==25 or player1_score==27 or player1_score==28 or player1_score==29 or player1_score==30):
							player1_y=guti_y[2]
						elif(player1_score==40 or player1_score==37 or player1_score==36 or player1_score==35 or player1_score==34 or player1_score==33 or player1_score==32 or player1_score==31):
							player1_y=guti_y[3]
						elif(player1_score==41 or player1_score==42 or player1_score==43 or player1_score==44 or player1_score==45 or player1_score==46 or player1_score==47 or player1_score==48 or player1_score==50):
							player1_y=guti_y[4]
						elif(player1_score==59 or player1_score==58 or player1_score==55 or player1_score==53 or player1_score==52):
							player1_y=guti_y[5]
						elif(player1_score==62 or player1_score==63 or player1_score==64 or player1_score==65 or player1_score==66 or player1_score==67 or player1_score==68 or player1_score==69 or player1_score==70):
							player1_y=guti_y[6]
						elif(player1_score==80 or player1_score==79 or player1_score==78 or player1_score==77 or player1_score==76 or player1_score==74 or player1_score==72 or player1_score==71):
							player1_y=guti_y[7]
						elif(player1_score==82 or player1_score==84 or player1_score==86 or player1_score==87 or player1_score==89):
							player1_y=guti_y[8]
						elif(player1_score==100 or player1_score==98 or player1_score==96 or player1_score==95 or player1_score==94 or player1_score==93 or player1_score==91):
							player1_y=guti_y[9]
						print("Player 1's score:- ",player1_score)
						if(player1_score==player2_score):
							screen.blit(merge,(player1_x,player1_y))
							screen.blit(player2_color,(19,600))
							screen.blit(player1_color,(19,560))
						else:
							screen.blit(player2_color,(player2_x,player2_y))
							screen.blit(player1_color,(player1_x,player1_y))
							screen.blit(player2_color,(19,600))
							screen.blit(player1_color,(19,560))
						turn+=1
						player_label=font3.render("Player 1's Score:- "+str(player1_score), 1, (153, 204, 255))
						screen.blit(player_label,(60,565))
						player2_label=font3.render("Player 2's Score:- "+str(player2_score), 1, (153, 204, 255))
						screen.blit(player2_label,(60,605))
						label=font3.render("Player 2's Turn", 1, (255, 204, 0))
						screen.blit(label,(360,610))
			pygame.display.update()
		elif(turn%2!=0):
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				if event.type==pygame.MOUSEBUTTONDOWN:
					click=pygame.mouse.get_pos()
					print(click)
					dice_x=click[0]
					dice_y=click[1]
					if (dice_x>=621 and dice_x<=653 and dice_y>=581 and dice_y<=613):
						pygame.mouse.set_cursor(*pygame.cursors.diamond)
						screen.blit(background,(0,0))
						dice_sound.play()
						time.sleep(2)
						number=random.randint(1,6)
						print("dice rolled:- ",number)
						if(number==1):
							screen.blit(one,(621,581))
						elif(number==2):
							screen.blit(two,(621,581))
						elif(number==3):
							screen.blit(three,(621,581))
						elif(number==4):
							screen.blit(four,(621,581))
						elif(number==5):
							screen.blit(five,(621,581))
						elif(number==6):
							screen.blit(six,(621,581))
						label=font2.render("Player 2 rolled "+str(number), 1, (255, 102, 153))
						screen.blit(label,(369,565))
						player2_score+=number
						if(player2_score==3):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=17
						elif(player2_score==6):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=8
						elif(player2_score==11):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=17
						elif(player2_score==15):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=19
						elif(player2_score==17):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=57
						elif(player2_score==22):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=15
						elif(player2_score==38):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=21
						elif(player2_score==49):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=18
						elif(player2_score==57):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=19
						elif(player2_score==61):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=17
						elif(player2_score==73):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=13
						elif(player2_score==81):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=17
						elif(player2_score==88):
							ladder_sound.play()
							label=font2.render("Player 2 found a ladder!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score+=3
						elif(player2_score==8):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=4
						elif(player2_score==18):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=17
						elif(player2_score==26):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=16
						elif(player2_score==39):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=34
						elif(player2_score==51):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=37
						elif(player2_score==54):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=18
						elif(player2_score==56):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=55
						elif(player2_score==60):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=37
						elif(player2_score==75):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=47
						elif(player2_score==90):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=42
						elif(player2_score==85):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=26
						elif(player2_score==83):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=38
						elif(player2_score==92):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=67
						elif(player2_score==97):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=10
						elif(player2_score==99):
							snake_sound.play()
							label=font2.render("A snake ate Player 2!", 1, (255, 102, 153))
							screen.blit(label,(336,585))
							player2_score-=36
						if(player2_score>100):
							player2_score-=number
						#x position
						if(player2_score==1 or player2_score==20 or player2_score==21 or player2_score==40 or player2_score==41 or player2_score==80 or player2_score==100):
							player2_x=guti_x[0]
						elif(player2_score==2 or player2_score==19 or player2_score==42 or player2_score==59 or player2_score==62 or player2_score==79 or player2_score==82):
							player2_x=guti_x[1]
						elif(player2_score==23 or player2_score==43 or player2_score==58 or player2_score==63 or player2_score==78 or player2_score==98):
							player2_x=guti_x[2]
						elif(player2_score==4 or player2_score==24 or player2_score==37 or player2_score==44 or player2_score==64 or player2_score==77 or player2_score==84):
							player2_x=guti_x[3]
						elif(player2_score==5 or player2_score==16 or player2_score==25 or player2_score==36 or player2_score==45 or player2_score==65 or player2_score==76 or player2_score==96):
							player2_x=guti_x[4]
						elif(player2_score==35 or player2_score==46 or player2_score==55 or player2_score==66 or player2_score==86 or player2_score==95):
							player2_x=guti_x[5]
						elif(player2_score==7 or player2_score==14 or player2_score==27 or player2_score==34 or player2_score==47 or player2_score==67 or player2_score==74 or player2_score==87 or player2_score==94):
							player2_x=guti_x[6]
						elif(player2_score==13 or player2_score==28 or player2_score==33 or player2_score==48 or player2_score==53 or player2_score==68 or player2_score==93):
							player2_x=guti_x[7]
						elif(player2_score==9 or player2_score==12 or player2_score==29 or player2_score==32 or player2_score==52 or player2_score==69 or player2_score==72 or player2_score==89):
							player2_x=guti_x[8]
						elif(player2_score==10 or player2_score==30 or player2_score==31 or player2_score==50 or player2_score==70 or player2_score==71 or player2_score==91):
							player2_x=guti_x[9]
						#y position
						if(player2_score==1 or player2_score==2 or player2_score==4 or player2_score==5 or player2_score==7 or player2_score==9 or player2_score==10):
							player2_y=guti_y[0]
						elif(player2_score==20 or player2_score==19 or player2_score==16 or player2_score==14 or player2_score==13 or player2_score==12):
							player2_y=guti_y[1]
						elif(player2_score==21 or player2_score==23 or player2_score==24 or player2_score==25 or player2_score==27 or player2_score==28 or player2_score==29 or player2_score==30):
							player2_y=guti_y[2]
						elif(player2_score==40 or player2_score==37 or player2_score==36 or player2_score==35 or player2_score==34 or player2_score==33 or player2_score==32 or player2_score==31):
							player2_y=guti_y[3]
						elif(player2_score==41 or player2_score==42 or player2_score==43 or player2_score==44 or player2_score==45 or player2_score==46 or player2_score==47 or player2_score==48 or player2_score==50):
							player2_y=guti_y[4]
						elif(player2_score==59 or player2_score==58 or player2_score==55 or player2_score==53 or player2_score==52):
							player2_y=guti_y[5]
						elif(player2_score==62 or player2_score==63 or player2_score==64 or player2_score==65 or player2_score==66 or player2_score==67 or player2_score==68 or player2_score==69 or player2_score==70):
							player2_y=guti_y[6]
						elif(player2_score==80 or player2_score==79 or player2_score==78 or player2_score==77 or player2_score==76 or player2_score==74 or player2_score==72 or player2_score==71):
							player2_y=guti_y[7]
						elif(player2_score==82 or player2_score==84 or player2_score==86 or player2_score==87 or player2_score==89):
							player2_y=guti_y[8]
						elif(player2_score==100 or player2_score==98 or player2_score==96 or player2_score==95 or player2_score==94 or player2_score==93 or player2_score==91):
							player2_y=guti_y[9]
						print("Player 2's score:- ",player2_score)
						if(player1_score==player2_score):
							screen.blit(merge,(player1_x,player1_y))
							screen.blit(player2_color,(19,600))
							screen.blit(player1_color,(19,560))
						else:
							screen.blit(player2_color,(player2_x,player2_y))
							screen.blit(player1_color,(player1_x,player1_y))
							screen.blit(player2_color,(19,600))
							screen.blit(player1_color,(19,560))
						turn+=1
						player_label=font3.render("Player 1's Score:- "+str(player1_score), 1, (153, 204, 255))
						screen.blit(player_label,(60,565))
						player2_label=font3.render("Player 2's Score:- "+str(player2_score), 1, (153, 204, 255))
						screen.blit(player2_label,(60,605))
						label=font3.render("Player 2's Turn", 1, (255, 204, 0))
						screen.blit(label,(360,610))
						if(player2_score==100 or player1_score==100):
							over=mixer.Sound("Sounds\\gameover.wav")
							over.play()
							break
			pygame.display.update()
	while(1):
		background = pygame.image.load("Images\\starter.jpg")
		screen.blit(background,(0,0))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		if(player2_score==100 and player1_score==100):
				label=font1.render("It's a Draw", 1, (0, 255, 204))
				screen.blit(label,(240,300))
		elif(player2_score==100):
			label=font1.render("Game Over! Player 2 Won.", 1, (0, 255, 204))
			screen.blit(label,(65,274))
		elif(player1_score==100):
			label=font1.render("Congratulations! Player 1 Won.", 1, (0, 255, 204))
			screen.blit(label,(60,274))
		pygame.display.update()
pygame.quit()
