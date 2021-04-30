#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  genetic rockets.py
#  
#  Copyright 2021 culpd <culpd@PERTTL075>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import random, pygame, math
from pvector import *

	
class DNA():
	def __init__(self, num_genes):
		self.genes = []

		gene = PVector.random2D()
		#print(num_genes)
		#print (gene.x, gene.y)
		gene.mult(5)
		#print(gene.x,gene.y)
		self.genes.append(gene)
		for j in range(1, num_genes):
			if random.randint(1,100) < 70:
				dx = self.genes[j-1].x
				dy = self.genes[j-1].y
				gene = PVector(dx,dy)
				self.genes.append(gene)
			else:
				gene = PVector.random2D()
				gene.mult(5)
				self.genes.append(gene)
			
	
class Rocket():
	def __init__(self, x,y, num_genes):
		self.speed = PVector(0,0)
		self.location = PVector(x,y)
		self.accel = PVector(0, 0)
		self.radius = 2
		self.color = (0,0,255)
		self.stopped = False
		self.rect = 0
		self.dna = DNA(num_genes)
		self.accel = PVector(random.uniform(-1,1) , random.uniform(-1,1))
		self.fitness = 0

	def find_fitness(self, target):
		distance = math.hypot(self.location.x - target.x, self.location.y-target.y)
		print(distance)
		self.fitness = (1/distance)**2
		if self.stopped:
			self.fitness = self.fitness/10
		
	def update(self, position):
		if not self.stopped:
			self.location.add(self.dna.genes[position])
		
	def draw(self):
		x = self.location.x
		y = self.location.y
		self.rect = pygame.draw.circle( screen, self.color, ( int(x),int(y) ), self.radius)
	
	def detect_collision(self, obstacle):
		if not self.stopped:
			if self.rect.colliderect(obstacle):
				print("collison")
				self.stopped = True
				
	def check_bounds(self):
		if self.location.x < 0 or self.location.x > 799:
			self.stopped = True
		if self.location.y < 0 or self.location.y > 799:
			self.stopped = True
			
class Population():
	def __init__(self, mutation_rate, num_individuals, num_genes):
		self.mutation_rate = mutation_rate
		self.rocket_population = []
		self.generations = 0
		self.populate(num_individuals, num_genes)
	
	def populate(self, num_individuals, num_genes):
		for i in range(num_individuals):
			x = 800//2
			y = SCREEN_HEIGHT-1
			rocket = Rocket(x,y, num_genes)

			self.rocket_population.append(rocket)
		

SCREEN_WIDTH = SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode( [SCREEN_WIDTH, SCREEN_HEIGHT] )
fps_clock = pygame.time.Clock()
obstacle = pygame.Rect(250,350,200,100)
target = PVector(400,20)
num_genes = 300


def main(args):
	rockets = Population(.1, 200, num_genes)
	running = True

	while running:
		
		for j in range(num_genes):
			    # Did the user click the window close button?
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					
			screen.fill( (255,255,255) )
			pygame.draw.rect(screen, (255,0,0), obstacle)
			pygame.draw.circle(screen, (0,255,255), (target.x, target.y), 20)
			
			for rocket in rockets.rocket_population:			
				rocket.draw()
				rocket.detect_collision(obstacle)
				rocket.check_bounds()
				rocket.update(j)
			print (j)

			pygame.display.flip()
			fps_clock.tick(30)
		running = False
	print("Done running")
	
	for rocket in rockets.rocket_population:
		rocket.find_fitness(target)
		print(rocket.fitness)
	
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
	pygame.quit()
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
