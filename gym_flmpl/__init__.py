from gym.envs.registration import register
import envs

register(
    id='FrozenLakeMpl-v0',
    entry_point='gym_flmpl.envs:FrozenLakeEnv',
    kwargs={'map_name': '4x4'},
    max_episode_steps=100,
    reward_threshold=0.78,      # optimum = .8196
)
register(
    id='FrozenLakeMpl8x8-v0',
    entry_point='gym_flmpl.envs:FrozenLakeEnv',
    kwargs={'map_name': '8x8'},
    max_episode_steps=200,
    reward_threshold=0.99,      # optimum = 1
)
