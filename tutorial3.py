import gym
from matplotlib import pyplot as plt
from matplotlib import animation
import time

env = gym.make("ALE/Pacman-v5")
env.reset()

fig = plt.figure()
im = plt.imshow(env.render(mode='rgb_array'))

def init():
    im.set_data(env.render(mode='rgb_array'))

def constant_strategy(i):
    new_space, reward, is_done, info = env.step(2) # Always move right
    im.set_data(env.render(mode='rgb_array'))
    if is_done:
        anim.event_source.stop()
    return im

# TODO Find out the following
# Actions
# 0:  
# 1: 
# 2: Right
# 3: 
# 4: 

def random_strategy(i):
    # TODO Implement Random Action
    raise NotImplementedError

    im.set_data(env.render(mode='rgb_array'))
    if is_done:
        anim.event_source.stop()
    return im

print("Constant Strategy")
anim = animation.FuncAnimation(fig, constant_strategy, init_func=init, frames=60,
                               interval=5)
# print("Random Strategy")
# anim = animation.FuncAnimation(fig, random_strategy, init_func=init, frames=60,
#                                interval=5)
fig.show()

# TODO (Dont need implement) Describe how you can smartly solve this problem