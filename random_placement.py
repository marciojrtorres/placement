#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import numpy
import random
import math

def generate_random_netlist(gates, wires):
  netlist = []
  for g in range(gates):
    # gate[x, y, conlist]
    netlist.append([0, 0, []])
  for i in range(wires):
    b_gate = a_gate = random.randrange(gates)
    while b_gate == a_gate: b_gate = random.randrange(gates)
    netlist[a_gate][2].append(b_gate)
    # netlist[b_gate][2].append(a_gate) # no bidirectional nav
  return netlist

def random_initial_placement(netlist, w, h):
  grid = list(range(w * h))
  random.shuffle(grid)
  for gate in netlist:
    g = grid.pop()
    gate[0], gate[1] = g % w, g / w

gates     = 10
wires     = 10

height    = 10
width     = 10

netlist = generate_random_netlist(gates, wires)

random_initial_placement(netlist, width, height)

print netlist

def half_perimeter_wirelength(a_gate, b_gate):
  return abs(a_gate[0] - b_gate[0]) + abs(a_gate[1] - b_gate[1])

length = 0
for i, gate in enumerate(netlist):
  for net in gate[2]:
    # length = length + half_perimeter_wirelength(netlist[i][0, 1], netlist[net][0, 1])
    length = length + half_perimeter_wirelength((netlist[i][0], netlist[i][1]), 
                                              (netlist[net][0], netlist[net][1]))
    # print (netlist[i][0], netlist[i][1])
    # print (netlist[net][0], netlist[net][1])

print length