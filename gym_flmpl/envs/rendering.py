# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
from gym.envs.toy_text import frozen_lake
import copy


class Viewer(object):
    FROZEN_COLOR = (0, 255, 255)    # cyan
    HOLE_COLOR = (128, 128, 128)    # gray
    NORMAL_COLOR = (255, 255, 255)    # white
    MAP_DICT = {
        'F': FROZEN_COLOR,
        'H': HOLE_COLOR,
        'N': NORMAL_COLOR
    }
    ACITON_DICT = {
        frozen_lake.LEFT: 'LEFT',
        frozen_lake.DOWN: 'DOWN',
        frozen_lake.RIGHT: 'RIGHT',
        frozen_lake.UP: 'UP'
    }

    def __init__(self, maze, convert):
        self.__maze_canvas = None
        self.__ax = None
        self.__sg_dict = {}
        self.__nrows = None
        self.__ncols = None
        self.__fig = None
        self.__canvas = None
        self.__convert = convert
        self.__initialize_map_dict()
        self.__initialize_maze_canvas(maze)

    def __initialize_map_dict(self):
        self.__map_dict = copy.deepcopy(self.MAP_DICT)
        for src, dst in self.__convert.iteritems():
            self.__map_dict[src] = self.__map_dict[dst]

    def __initialize_maze_canvas(self, maze):
        start = np.argwhere(maze == 'S')[0]
        goal = np.argwhere(maze == 'G')[0]
        self.__sg_dict['S'] = start
        self.__sg_dict['G'] = goal

        self.__nrows, self.__ncols = maze.shape
        canvas_shape = [self.__nrows, self.__ncols, 3]
        self.__maze_canvas = np.zeros(canvas_shape, dtype=np.uint8)
        self.__maze_canvas[:, :] = self.__map_dict['F']
        self.__maze_canvas[maze == 'H'] = self.__map_dict['H']
        self.__fig = Figure()
        self.__canvas = FigureCanvas(self.__fig)

    def render(self, state, lastaction, mode='mpl'):
        if lastaction is not None:
            action_str = self.ACITON_DICT[lastaction]
        else:
            action_str = 'None'
        if mode == 'mpl':
            ax = plt.gca()
        else:
            ax = self.__fig.gca()
        ax.cla()
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xticks(
            np.arange(-0.5, self.__ncols - 0.5)
        )
        ax.set_yticks(
            np.arange(-0.5, self.__nrows - 0.5)
        )
        ax.set_title('Last action: %s' % action_str, fontsize=18)
        ax.grid(linestyle='dashed')
        ax.imshow(self.__maze_canvas, interpolation='nearest')
        self.__agent_location = np.array(
            [state // self.__ncols, state % self.__ncols]
        )
        for text, location in self.__sg_dict.iteritems():
            if not np.allclose(self.__agent_location, location):
                y, x = location
                ax.text(
                    x, y, text,
                    va='center',
                    ha='center',
                    fontsize=24
                )
        y, x = self.__agent_location
        ax.text(
            x, y, 'A',
            va='center',
            ha='center',
            fontsize=24
        )
        if mode == 'rgb_array':
            self.__canvas.draw()
            width, height = self.__fig.get_size_inches() * self.__fig.get_dpi()
            img = np.fromstring(
                self.__canvas.tostring_rgb(), dtype='uint8'
            )
            img = img.reshape(int(height), int(width), 3)
            return img
        else:
            return plt.pause(1e-6)
