# Pyvisigraph - Python Visibility Graph

![MIT License](https://img.shields.io/github/license/pingou2712/pyvisigraph.svg?style=flat)
![PyPI](https://img.shields.io/pypi/v/pyvisigraph.svg?style=flat)

Given a set of simple obstacle polygons, build a visibility graph and find
the shortest path between two points.

![Figure 1](docs/images/graph.png)

Pyvisigraph is a MIT-licensed Python package for building visibility graphs from
a list of simple obstacle polygons. The visibility graph algorithm (D.T. Lee)
runs in O(n^2 log n) time. The shortest path is found using Djikstra's
algorithm.

# Why a New Project?

First and foremost, this project is structurally based on Christian Reksten-Monsen's Pyvisgraph project (https://github.com/TaipanRex/pyvisgraph). Special thanks to him.

Furthermore, in reviewing projects such as pivisgraph and extremitypathfinder, the main issue I encountered was that these programs operate with approximate values, whether it involves calculations like acos, atan, or even divisions. Besides potentially causing bugs, this also takes more time! The vision for this project is different: it allows for choosing the desired precision (number of decimal place), and all efforts to determine the visibility graph are made using exact values. D.T. Lee's algorithm does not require calculating angles but only comparing them! A simple calculation of the orientation of points is necessary. In the same way, we don't really need to know the coordinates of the intersection points but only need to understand their relative positions to each other!

Result: no bugs related to approximate values, and the work is even done much more quickly!!!

Significant modifications have been made compared to Christian Reksten-Monsen's project, which prevents me from proposing commits...

Moreover, this pivisgraph considers Property 1 from this thesis: https://cs.au.dk/~gerth/advising/thesis/anders-strand-holm-vinther_magnus-strand-holm-vinther.pdf, which significantly reduces the time taken and the number of visibility edges. Simply use the 'opti' mode (see example).

## Installing Pyvisigraph

```
$ pip install pyvisigraph
```

Pyvisigraph supports Python 3.

## Usage VisiGraph without 'opti' mode

![Figure 2](docs/images/graphWithoutOpti.png)

Here is an example of building a visibility graph without 'opti' mode given a list of
simple polygons:

```
import pyvisigraph as vg

polys = [[(1.0, 0.0),(0.0, 1.0),(-1, 0.0),(0, -1.0)],[(2.0, 2.0),(-2,2),(-0.51, 1.9),(-0.4,1.8),(0, 1.2),(0.5, 1.7),(1.5, 0),(0.5,-1.7),(0, -1.2),(-0.5,-1.8),(-0.51,-1.9),(-2,-2),(2, -2.0)]]
g = vg.VisiGraph()
g.build(polys, precision=7)
g.update([(0.7,-0.5),(-1.5,0)])
g.update([(-1,1.35)])

print('Number of visibility edge : ' + str(len(g.visigraph.edges())))

g.plotGraphAndOrSave(polys)
```

Once the visibility graph is built, it can be saved and subsequently loaded.
This is useful for large graphs where build time is long. `pickle` is used
for saving and loading.

```
g.save('graph.pk1')
g2 = VisiGraph()
g2.load('graph.pk1')
```

For obstacles with a large number of points, Pyvisigraph can take advantage of
processors with multiple cores using the `multiprocessing` module. Simply
add the number of workers (processes) to the `build` method:

```
>>> g.build(polys, precision=7, workers=4)
```

Without the 'opti' mode enabled, the visibility graph is complete: there are then 80 edges.

## Usage VisiGraph with 'opti' mode and cadre

![Figure 3](docs/images/graphOptiAndCadre.png)

The 'opti' mode only retains the necessary visibility edges to calculate the shortest path. Consequently, the construction of the visibility graph is much faster and the file size is reduced. 
The 'cadre' option defines the area within which the polygons are located to eliminate the edges of polygons on the frame. The 'cadre' option only works with the 'opti' mode.

Here is an example of building a visibility graph with 'opti' and a 'cadre' mode given a list of
simple polygons:

```
import pyvisigraph as vg

polys = [[(1.0, 0.0),(0.0, 1.0),(-1, 0.0),(0, -1.0)],[(2.0, 2.0),(-2,2),(-0.51, 1.9),(-0.4,1.8),(0, 1.2),(0.5, 1.7),(1.5, 0),(0.5,-1.7),(0, -1.2),(-0.5,-1.8),(-0.51,-1.9),(-2,-2),(2, -2.0)]]
cadre = (-2.0, -2.0,2.0, 2.0)
g = vg.VisiGraph()
g.build(polys, precision=7, opti=True, cadre=cadre)

g.update([(0.7,-0.5),(-1.5,0)])
g.update([(-1,1.35)])

print('Number of visibility edge : ' + str(len(g.visigraph.edges())))

g.plotGraphAndOrSave(polys)
```

Once the visibility graph is built, it can be saved and subsequently loaded.
This is useful for large graphs where build time is long. `pickle` is used
for saving and loading.

```
g.save('graph.pk1')
g2 = VisiGraph()
g2.load('graph.pk1')
```

For obstacles with a large number of points, Pyvisigraph can take advantage of
processors with multiple cores using the `multiprocessing` module. Simply
add the number of workers (processes) to the `build` method:

```
>>> g.build(polys, precision=7, workers=4, opti=True, cadre=cadre)
```

With the 'opti' mode enabled, the visibility graph then contains only 18 edges!

## Use shortest_path of networkx (Dijkstra's algorithm)

![Figure 4](docs/images/ShortestPath.png)

Here is an example of using VisiGraph and networkx to find the shortest path using Euclidean distance and Dijkstra's algorithm:

```
import pyvisigraph as vg
import networkx as nx
import math

#define used distance
distance = lambda x, y: math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

polys = [[(1.0, 0.0),(0.0, 1.0),(-1, 0.0),(0, -1.0)],[(2.0, 2.0),(-2,2),(-0.51, 1.9),(-0.4,1.8),(0, 1.2),(0.5, 1.7),(1.5, 0),(0.5,-1.7),(0, -1.2),(-0.5,-1.8),(-0.51,-1.9),(-2,-2),(2, -2.0)]]
cadre = (-2.0, -2.0,2.0, 2.0)
g = vg.VisiGraph()
g.build(polys, precision=7, opti=True, cadre=cadre, weight=distance)

#Update with new point if needed
g.update([(0.7,-0.5),(-1.5,0)], weight=distance)
g.update([(-1,1.35)], weight=distance)

#Shortest path
path = nx.shortest_path(g.visigraph, source=(-1,1.35), target=(0.7,-0.5), weight='weight')

#Plot it!
g.plotGraphAndOrSave(polys,path)
```

## Use astar_path of networkx (A* algorithm)

Here is an example of using VisiGraph and networkx to find the shortest path using Euclidean distance and A* algorithm:

```
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
```

## Simple usage with shape - shortest path 

![Figure 5](docs/images/shortestPathWorld.png)

Here is an example of constructing the visibility graph on the world map in crude quality:

```
import pyvisigraph as vg

shape = vg.ShapeWork()
shape.buildGraph('gshhg-shp-2.3.7/GSHHS_shp/c/GSHHS_c_L1.shp', precision=7)
shape.plotGraph()
shape.save('worldshape')
```

Once the graph is created, it can be saved and/or used to find the shortest path:

```
import pyvisigraph as vg

shape = vg.ShapeWork()
shape.load('worldshape')

start_point = (12.568337, 55.676098) # Copenhagen
end_point = (103.851959, 1.290270) # Singapore
shape.calculer_shortest_path(start_point,end_point)

shape.plotPathAndOrSave(show=True, filename='shortestPath.png')
```

For obstacles with a large number of points, Pyvisigraph can take advantage of
processors with multiple cores using the `multiprocessing` module. Simply
add the number of workers (processes) to the `buildGraph` method:

```
shape.buildGraph('gshhg-shp-2.3.7/GSHHS_shp/c/GSHHS_c_L1.shp', precision=7, workers=4)
```



## Usage with shape, zone and buffer - shortest path

![Figure 6](docs/images/shortestPathOptiAndCadre.png)

Here is an example of constructing the visibility graph on a part of Sardinia in the Mediterranean at full resolution (we use GSHHS_f_L1.shp). To specify the area of interest, we use the zone option in the buildGraph method, which frames a specific geographic area with coordinates (9.35, 40.98, 9.68, 41.22).

Moreover, since a boat rarely passes exactly along the coast, we apply a buffer of approximately 40 meters to the coastal data. This buffer is implemented using the shpBuffer parameter, which effectively expands the coastline outward to ensure safer navigation routes are calculated.

The default projection used by many global applications is EPSG:4326, which covers almost the entire globe. However, for this specific application focusing on Sardinia, we switch to the EPSG:32632 projection. This local UTM projection is better suited for the region as it minimizes distortions and improves accuracy in local scale studies.

Be careful, it may be useful when working with a frame and a buffer to increase the precision to 12 in order to better manage possible overlapping points that may result. This is not a blocking bug, but it is always preferable to have only two edges per point, in other words, to have a geometry with only distinct polygons.

```
import pyvisigraph as vg

shape = vg.ShapeWork()
shape.buildGraph('gshhg-shp-2.3.7/GSHHS_shp/f/GSHHS_f_L1.shp', zone=(9.35, 40.98, 9.68, 41.22),shpBuffer=40,crsProj="EPSG:32632", precision=7)
shape.plotGraph()
shape.save('graphshape')
```

Once the graph is created, it can be saved and/or used to find the shortest path:

```
import pyvisigraph as vg

shape = vg.ShapeWork()
shape.load('graphshape')
coord_de_depart = (9.522130177978363, 41.0280536333291)
coord_darrivee = (9.46699448572067, 41.185838636726395)
shape.calculer_shortest_path(coord_de_depart,coord_darrivee)
shape.plotPathAndOrSave(show=True, filename='shortestPath.png')
```

For obstacles with a large number of points, Pyvisigraph can take advantage of
processors with multiple cores using the `multiprocessing` module. Simply
add the number of workers (processes) to the `buildGraph` method:

```
shape.buildGraph('gshhg-shp-2.3.7/GSHHS_shp/f/GSHHS_f_L1.shp', zone=(9.35, 40.98, 9.68, 41.22),shpBuffer=40,crsProj="EPSG:32632", precision=7, workers=4)
```


## Limitation

The polygons must all be distinct and must not share any points whatsoever.

## Credit

https://github.com/TaipanRex/pyvisgraph

https://cs.au.dk/~gerth/advising/thesis/anders-strand-holm-vinther_magnus-strand-holm-vinther.pdf
