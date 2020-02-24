import pygame
import numpy

#Display settings and pygame initialization
WIDTH = 1200
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Mandelbrot Set')

#This is the maximum amount of iterations the algorithm will run before moving on to the next n value
max_iter = 80

def mandelbrot(c):

  '''
  This function is based off of the mathematical formula for the mandelbrot set
  '''

    n = 0
    z = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return(n)
    
#Runs 2000 y values through the mandelbrot function for every x value
for x in arange(-2,1,0.001):
    for y in arange(-1,1,0.001):
        c = complex(x,y)
        m = mandelbrot(c)
        
#The color scheme can be changed but this prints a grayscaled image with bands
        hue = int(255 * (m/max_iter))
        saturation = int(255 * (m/max_iter))
        value = int(255 * (m/max_iter))
        
# Converts the points to specific pixels
        x_plot = (x+2) * 400
        y_plot = (y+1) * 300

#This makes the pixels integers and not floats
        screen.set_at((int(x_plot//1),int(y_plot//1)),(hue,saturation,value))

#Position of this step will change the speed of the imaging 
  pygame.display.flip()

#This is necessary to keep the pygame window open
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
