#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import numpy
import random
import math
import copy

def generate_random_netlist(gates, wires):
  netlist = []
  for g in range(gates):
    # gate[x, y, conlist]
    netlist.append([0, 0, []])
  for i in range(wires):
    b_gate = a_gate = random.randrange(gates)
    while b_gate == a_gate and b_gate not in netlist[a_gate][2]: 
      b_gate = random.randrange(gates)
    netlist[a_gate][2].append(b_gate)
    # netlist[b_gate][2].append(a_gate) # no bidirectional nav
  return netlist

def random_initial_placement(netlist, w, h):
  grid = list(range(w * h))
  random.shuffle(grid)
  for gate in netlist:
    g = grid.pop()
    gate[0], gate[1] = g % w, g / w

def half_perimeter_wirelength(a_gate, b_gate):
  return abs(a_gate[0] - b_gate[0]) + abs(a_gate[1] - b_gate[1])

def whole_list_wirelength(netlist):
  length = 0
  for i, gate in enumerate(netlist):
    for net in gate[2]:
      length = length + half_perimeter_wirelength((netlist[i][0], netlist[i][1]), 
                                 (netlist[net][0], netlist[net][1]))
  return length

def swap_gates(a_gate, b_gate):
  a_gate[0], b_gate[0] = b_gate[0], a_gate[0]
  a_gate[1], b_gate[1] = b_gate[1], a_gate[1]

def wirelength_shorten(netlist, wirelength_shorten_attempt = 10):
  current_netlist_length = whole_list_wirelength(netlist)
  while wirelength_shorten_attempt > 0:
    # TODO: an initial particular random swap can affect the entirely
    # sequence where more attempts couldn't improve the wire length.
    # Perhaps is that a reason for using a stochastic optimization 
    # (maybe genetic) algorithm? http://ieeexplore.ieee.org/document/4408630/
    a_gate, b_gate = random.sample(netlist, 2)
    swap_gates(a_gate, b_gate)
    new_netlist_length = whole_list_wirelength(netlist)
    if new_netlist_length < current_netlist_length:
      current_netlist_length = new_netlist_length    
    else:
      wirelength_shorten_attempt = wirelength_shorten_attempt - 1
      swap_gates(a_gate, b_gate) # undo swap
  return current_netlist_length

gates     = 10
wires     = 10

chip_height    = 10
chip_width     = 10

netlist = generate_random_netlist(gates, wires)
random_initial_placement(netlist, chip_width, chip_height)

print '10 attempts'
cobaia = copy.deepcopy(netlist)
print whole_list_wirelength(cobaia)
wirelength_shorten(cobaia, 10)
print whole_list_wirelength(cobaia)
print '50 attempts'
cobaia = copy.deepcopy(netlist)
print whole_list_wirelength(cobaia)
wirelength_shorten(cobaia, 50)
print whole_list_wirelength(cobaia)
print '100 attempts'
cobaia = copy.deepcopy(netlist)
print whole_list_wirelength(cobaia)
wirelength_shorten(cobaia, 100)
print whole_list_wirelength(cobaia)
print '500 attempts'
cobaia = copy.deepcopy(netlist)
print whole_list_wirelength(cobaia)
wirelength_shorten(cobaia, 500)
print whole_list_wirelength(cobaia)
print '1k attempts'
cobaia = copy.deepcopy(netlist)
print whole_list_wirelength(cobaia)
wirelength_shorten(cobaia, 1000)
print whole_list_wirelength(cobaia)
print '10k attempts'
cobaia = copy.deepcopy(netlist)
print whole_list_wirelength(cobaia)
wirelength_shorten(cobaia, 10000)
print whole_list_wirelength(cobaia)
print '100k attempts'
cobaia = copy.deepcopy(netlist)
print whole_list_wirelength(cobaia)
wirelength_shorten(cobaia, 100000)
print whole_list_wirelength(cobaia)
print '1M attempts'
cobaia = copy.deepcopy(netlist)
print whole_list_wirelength(cobaia)
wirelength_shorten(cobaia, 1000000)
print whole_list_wirelength(cobaia)