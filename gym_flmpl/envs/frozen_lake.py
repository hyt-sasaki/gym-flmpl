# -*- coding:utf-8 -*-
from gym.envs.toy_text import frozen_lake
from gym_flmpl.envs.rendering import Viewer


class FrozenLakeEnv(frozen_lake.FrozenLakeEnv):
    metadata = {
        'render.modes': ['human', 'ansi', 'rgb_array', 'mpl']
    }

    def __init__(self, desc=None, map_name="4x4", is_slippery=True):
        super(FrozenLakeEnv, self).__init__(desc, map_name, is_slippery)
        self.shape = self.desc.shape

    def _render(self, mode='mpl', close=False):
        if mode in ['rgb_array', 'mpl']:
            if close:
                return
            if not hasattr(self, 'viewer'):
                self.viewer = Viewer(self.desc)
            r = self.viewer.render(self.s, self.lastaction, mode)
            return r
        else:
            return super(FrozenLakeEnv, self)._render(mode, close)
