# -*- coding:utf-8 -*-
import gym
import gym_flmpl


if __name__ == '__main__':
    env = gym.make("FrozenLakeMpl-v0")
    env.reset()
    env.verbose = True
    for _ in range(10):
        env.render(mode='mpl')
        env.step(env.action_space.sample())
