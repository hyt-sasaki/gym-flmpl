# -*- coding:utf-8 -*-
from gym.envs.toy_text import frozen_lake
from gym_flmpl.envs.rendering import Viewer


class FrozenLakeEnv(frozen_lake.FrozenLakeEnv):
    metadata = {
        'render.modes': ['human', 'ansi', 'rgb_array', 'mpl']
    }

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
