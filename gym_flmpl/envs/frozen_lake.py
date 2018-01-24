# -*- coding:utf-8 -*-
from gym.envs.toy_text import frozen_lake


class FrozenLakeEnv(frozen_lake.FrozenLakeEnv):
    metadata = {'render.modes': ['human', 'ansi', 'rgb_array']}

    def _render(self, mode='human', close=False):
        if mode != 'rgb_array':
            return super(FrozenLakeEnv, self)._render(mode, close)
        else:
            raise NotImplementedError
