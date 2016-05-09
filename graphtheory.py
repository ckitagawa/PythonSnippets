import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import random
from numpy import ma
from matplotlib import colors, ticker, cm
from scipy import integrate as itg
from mpl_toolkits.mplot3d import Axes3D

def gen_verticies(n, dims, rng):
  random.seed('djskfhewh5712jsdhakj')
  out = []
  for i in range(n):
    out.append([])
    for j in range(dims):
      out[i].append(random.randint(rng[0],rng[1]))
  keys = [str(e) for e in list(range(n))]
  return dict(zip(keys, out))

def gen_edges(vecs):
  random.seed('djskfhewh5712jsdhakj')
  out = []
  used_edges = set()
  joins = []
  while len(used_edges) < len(vecs):
    a = random.randint(0,len(vecs)-1)
    b = random.randint(0,len(vecs)-1)
    if (a,b) not in joins and (b,a) not in joins:
      out.append([str(a),vecs[str(a)],str(b),vecs[str(b)], (0,0,random.random())])
      joins.append((a,b))
      used_edges.add(a)
      used_edges.add(b)
  return out

def euclidian_dist(vec1, vec2):
  vec3 = [abs(a_i - b_i) for a_i, b_i in zip(vec1, vec2)]
  return (np.dot(vec3, vec3))**(1/2)

def define_edge(vec1, vec2):
  return list(zip(vec1,vec2))

def main1(n, dims, rng):
  verticies = gen_verticies(n,dims,rng)
  #print(verticies)
  k = 0
  segments = []
  adjacency = np.zeros((n,n))
  mainbranch = ['0']
  while k < n-1:
    min_acc = rng[1]*(dims)
    key = None
    for i in mainbranch:
      for j in range(n):
        if i != str(j) and str(j) not in mainbranch:
          dist = euclidian_dist(verticies[i],verticies[str(j)])
          if dist < min_acc:
            min_acc = dist
            key = [i,str(j)]
    if key != None:
      segments.append(define_edge(verticies[key[0]],verticies[key[1]]))
      mainbranch.append(key[1])
      adjacency[int(key[0])][int(key[1])] = 1
      adjacency[int(key[1])][int(key[0])] = 1
      k = k + 1
  return segments, adjacency, verticies

# def main2(n, dims, rng, origin, end):
#   verticies = gen_verticies(n,dims,rng)
#   edges = gen_edges(verticies)
#   k = 0
#   segments = []
#   dist = []
#   edgelen = []
#   overt = verticies[str(origin)]
#   evert = verticies[str(end)]
#   for key1, vec1, key2, vec2, length in edges:
#     dist.append(((100*length[0])**2 + (100*length[1])**2 + (100*length[2])**2)**(1/2))
#     edgelen.append([key1,vec1,key2,vec2,dist[k],(length)])
#     k += 1
#   #print(sum(dist))
#   j = 0
#   total_length = 0
#   while j < n-1:
#     min_acc = rng[1]*(dims)
#     min_acc2 = rng[1]*(dims)
#     i = 0
#     for key, value in verticies.items():
#       keys = ['0','0']
#       for key1, vec1, key2, vec2, length, rgb in edgelen:
#         #print(key1, vec1, key2, vec2, length, rgb)
#         if key1 == key or key2 == key and length < min_acc:
#           if key1 == key:
#             lkey = key2
#           else:
#             lkey = key1

#           for key3, vec3, key4, vec4, length2, rgb2 in edgelen:
#             if key3 == lkey or lkey4 == key and length2 < min_acc2:

#           min_acc = length
#           keys = [key1, key2]
#           color = rgb
#           slength = length
#           #print(keys,color)
#       #print(define_edge(verticies[keys[0]],verticies[keys[1]]))
#       total_length = total_length+ slength
#       segments.append([define_edge(verticies[keys[0]], verticies[keys[1]]),color])
#       j = j+1
#       i = i+1
#     print(j)
#   return segments, verticies, total_length

# edges, verts, tlen = main2(100, 3, [0,100])
# print(tlen)
# #print(edges)
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.color = 'b'
# for i in range(len(edges)-1):
#   plt.plot(edges[i][0][0],edges[i][0][1],edges[i][0][2],color =edges[i][1])
# x = []
# y = []
# z = []
# for key,values in verts.items():
#   x.append(values[0])
#   y.append(values[1])
#   z.append(values[2])
# plt.plot(x,y,z,'r.')
# plt.show()

lc, adj, verts = main1(250, 3, [0,100])
#print(verts)
#print(adj)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.color = 'b'
#print(lc[1][0])
for i in range(len(lc)):
  try:
    plt.plot(lc[i][0],lc[i][1],lc[i][2],'b')
  except IndexError:
    plt.plot(lc[i][0],lc[i][1],'b')
x = []
y = []
z = []
for key,values in verts.items():
  x.append(values[0])
  y.append(values[1])
  z.append(values[2])
plt.plot(x,y,z,'r.')

plt.show()


#Main2 test


