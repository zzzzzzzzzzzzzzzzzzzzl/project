import torch
import random
import numpy as np
from collections import deque
from game import test
from model import Linear_QNet, QTrainer

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # randomness
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.model = Linear_QNet(8, 256, 8)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)
        self.model.load()



    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done)) # popleft if MAX_MEMORY is reached

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
        #for state, action, reward, nexrt_state, done in mini_sample:
        #    self.trainer.train_step(state, action, reward, next_state, done)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        # random moves: tradeoff exploration / exploitation
        # if self.n_games<100:
        #     self.epsilon=150-self.n_games

        self.epsilon = random.randint(-20,40)
        final_move = [0,0,0,0,0,0,0,0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 7)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move


def train():
    
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = test()
    while True:

            state_old=np.array(game.adjcon, dtype=int)
            final_move =game.adjcon.index(min(game.adjcon))# agent.get_action(state_old)
            done,reward, score = game.play_step(final_move)
            state_new = np.array(game.adjcon, dtype=int)
            agent.train_short_memory(state_old, final_move, reward, state_new, done)
            agent.remember(state_old, final_move, reward, state_new, done)
            game.getstateNEAT()

            if done:
                if score > record:
                    record = score
                    agent.model.save()
                while record==game.max:
                    game._update_ui()
                    game.events()
                game.reset()
                agent.n_games += 1
                agent.train_long_memory()


                print('Game', agent.n_games, 'Score', score, 'Record:', record)



if __name__ == '__main__':
    train()
    