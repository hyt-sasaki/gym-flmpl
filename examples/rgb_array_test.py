# -*- coding:utf-8 -*-
import gym
import gym_flmpl
import matplotlib.pyplot as plt
from matplotlib import animation


if __name__ == '__main__':
    env = gym.make("FrozenLakeMpl-v0")
    env.reset()
    env.verbose = True
    frames = []
    for _ in range(10):
        frames.append(env.render(mode='rgb_array'))
        env.step(env.action_space.sample())

    fig = plt.gcf()
    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(
        fig, animate, frames=len(frames), interval=500
    )
    anim.save('anim.gif', writer='imagemagick', dpi=200, fps=2)
