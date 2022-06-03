# Railway simulation

## Project description
This is a simple simulation of a randomly-generated railway network with trains, stations, accidents and all that could happen in real life.

## Classes and fields description
Currently project consists of next parts:
  1. Simulation - class that represents the whole simulation.
  2. SimulationUI - for now it is a class, that can print routes and distances between stations. Further it's going to be a class, that draws and updates interface .
  3. Station - class that represents station. Station has it own ID and contains list of nearby(adjacent) stations.
  4. Route - class that represents list of stations.
  5. Distances - adjacency matrix in Simulation class that contains distances between each pair of stations (if corresponding stations are connected with a road).

## Implementation features
  - For now, railway network is a rooted tree and route is a path from leaf to root.
  - Tree is generated randomly, similarly to BFS algorithm.
  - Distances generated with DFS algorithm run from root.
  - Later generating algorithms will be changed to more difficult ones, that want break other project logic.

