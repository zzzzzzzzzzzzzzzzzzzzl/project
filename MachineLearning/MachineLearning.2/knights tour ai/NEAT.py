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
        index=len(nets)
        nets.append(net)

        g.fitness = 0
        gameover=False
        
        while game.gameover==False:
            output = nets[0].activate(game.getstateNEAT())
            output=(output.index(max(output)))
            gameover,dontuse,turn=game.play_step(output)#self.gameover,self.reward,self.turn
            genomes[index][1].fitness=game.turn
        game.reset()
        knights.append(0)# we will just run 1 at a time .# this will be our knight
        


            


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
    p.run(run_tour, 1000)
    
