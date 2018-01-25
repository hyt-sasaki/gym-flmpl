# -*- coding: utf-8 -*-
import gym
import gym_flmpl
import matplotlib.pyplot as plt


KEY_TO_ACTION = {
    'left': 0,
    'down': 1,
    'right': 2,
    'up': 3
}


def main():
    env = gym.make("FrozenLakeMpl-v0")

    def get_action(event):
        if event.key in KEY_TO_ACTION.keys():
            act = KEY_TO_ACTION[event.key]
            ob, reward, done, info = env.step(act)
            env.render(mode='mpl')
            print("Observation: {}".format(ob))
            print("Reward: {}".format(reward))
            print("Info: {}".format(info))
            if done:
                env.reset()
                env.render(mode='mpl')
                print("Done!")

    fig = plt.figure()
    fig.canvas.mpl_connect('key_press_event', get_action)
    env.reset()
    env.render(mode='mpl')
    plt.pause(0)


if __name__ == "__main__":
    main()
