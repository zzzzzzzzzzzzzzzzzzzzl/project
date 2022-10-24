import pygame
import os
import math
import sys
import random
import neat
from game import test



generation=0
game=test()




def run_tour(genomes, config):

    # Init NEAT
    nets = []
    knights =[]

    for id, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        gameover=False
        while gameover==False:
            
            #game.getstateNEAT()
            output = nets[index].activate(game.getstateNEAT())
            print(output)
            gameover,dontuse,turn=game.playstep()#self.gameover,self.reward,self.turn
        knights.append(0)# we will just run 1 at a time .# this will be our knight
        

    # Init my game



    # Main loop
    global generation
    generation += 1
    while True:



        # Input my data and get result from network
        for index, car in enumerate(knights):
            output = nets[index].activate(game.getstateNEAT())
            print ()
            
            i = output.index(max(output))
            if i == 0:
                car.angle += 10
            else:
                car.angle -= 10

        # Update car and fitness
        remain_cars = 0
        for i, car in enumerate(cars):
            if car.get_alive():
                remain_cars += 1
                car.update(map)
                genomes[i][1].fitness += car.get_reward()

        # check

        # Drawing

        text = generation_font.render("Generation : " + str(generation), True, (255, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (screen_width/2, 100)
        screen.blit(text, text_rect)

        text = font.render("remain cars : " + str(remain_cars), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (screen_width/2, 200)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(0)

if __name__ == "__main__":
    # Set configuration file
    config_path = "./NEAT.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create core evolution algorithm class
    p = neat.Population(config)

    # Add reporter for fancy statistical result
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run NEAT
    p.run(run_car, 1000)
    
