"""
The MIT License (MIT)

Copyright (c) 2024 Vincent Laffargue

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pyvisigraph as vg
import networkx as nx
import math

#define used distance
distance = lambda x, y: math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

polys = [[(1.0, 0.0),(0.0, 1.0),(-1, 0.0),(0, -1.0)],[(2.0, 2.0),(-2,2),(-0.51, 1.9),(-0.4,1.8),(0, 1.2),(0.5, 1.7),(1.5, 0),(0.5,-1.7),(0, -1.2),(-0.5,-1.8),(-0.51,-1.9),(-2,-2),(2, -2.0)]]
cadre = (-2.0, -2.0,2.0, 2.0)
g = vg.VisiGraph()
g.build(polys, precision=7, opti=True, cadre=cadre, weight=distance)

#Update with new points if needed
g.update([(0.7,-0.5),(-1.5,0)], weight=distance)
g.update([(-1,1.35)], weight=distance)

#Shortest path
path = nx.astar_path(g.visigraph, source=(-1,1.35), target=(0.7,-0.5), heuristic=distance, weight='weight')

#Plot it!
g.plotGraphAndOrSave(polys,path)

