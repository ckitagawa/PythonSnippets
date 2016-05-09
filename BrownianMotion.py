import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import colors, ticker, cm
from mpl_toolkits.mplot3d import Axes3D


def gen_particles(n,dims,rng):
  particles = []
  for i in range(n):
    particles.append([])
    for j in range(dims):
      particles[i].append(random.randint(0,rng))
    particles[i].append(0)
  return particles

def motion(prev_state):
  new_state = []
  for i in range(len(prev_state)-1):
    new_state.append(prev_state[i]+np.random.normal())
  new_state.append(prev_state[len(prev_state)-1]+1)
  #print(prev_state)
  return new_state

def BrownianMotion(n, dims, rng, timesteps):
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.legend()
  particles = gen_particles(n,dims,rng)
  t = []
  for p in particles:
    t = [0]
    pos = [p]
    for i in range(timesteps):
      t.append(i+1)
      pos.append(list(motion(pos[i])))
    plotter = []
    for j in range(len(p)):
      plotter.append([])
      for k in range(timesteps+1):
        plotter[j].append(pos[k][j])
    plt.plot(t,plotter[0],plotter[1])
  mpl.rcParams['legend.fontsize'] = 10
  plt.show()

def gen_state(prev_state, particles):
  new_state = prev_state
  for i in range(particles):
    new_state[i] = motion(prev_state[i])
  return new_state

def valid(state, threshold):
  i = 0
  for position in state:
    j = 0
    for pos_check in state:
      if i != j:
        for k in range(len(position)-1):
          if (position[k] < pos_check[k]+threshold) and (position[k] > pos_check[k]-threshold):
            return False
      j +=1
    i += 1
  return True

def BrownianMotion2(n, dims, rng, timesteps, threshold=0.005):
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  #ax.legend()
  particles = gen_particles(n,dims,rng)
  states = [particles[:]]
  #prev_state = particles
  for i in range(timesteps):
    prev_state = states[i][:]
    flag = 0
    while flag == 0:
      proposed_state = gen_state(prev_state, len(particles))
      if valid(proposed_state[:], threshold):
        states.append(proposed_state[:])
        flag = 1
      else:
         print('Retrying')
  particlen = 0
  for particle in states[0]:
    particlepath = []
    for j in range(len(particle)):
      particlepath.append([])
      for i in range(len(states)):
        particlepath[j].append(states[i][particlen][j])
    #print(particlepath[0])
    plt.plot(particlepath[0], particlepath[1], particlepath[2])
    print(len(particlepath[0]))
    particlen+=1

  #x = np.arange(-timesteps**(1/2),timesteps**(1/2), 1)
  #y = np.arange(-timesteps**(1/2),timesteps**(1/2), 1)
  #X,Y = np.meshgrid(x,y)
  #zs = np.array([0.5*x**2 + 0.5*y**2 for x,y in zip(np.ravel(X), np.ravel(Y))])
  #Z = zs.reshape(X.shape)
  #ax.plot_surface(X, Y, Z)
  plt.show()



BrownianMotion2(4,2,0,1000)
