#!/bin/bash
python pacman.py -l mediumCorners -p SearchAgent -a fn=dfs,prob=CornersProblem -z 0.5
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem -z 0.5
python pacman.py -l mediumCorners -p SearchAgent -a fn=bs,prob=CornersProblem -z 0.5
python pacman.py -l mediumCorners -p SearchAgent -a fn=ids,prob=CornersProblem -z 0.5
python pacman.py -l mediumCorners -p SearchAgent -a fn=astar,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5



python pacman.py -l bigCorners -p SearchAgent -a fn=dfs,prob=CornersProblem -z 0.5
python pacman.py -l bigCorners -p SearchAgent -a fn=bfs,prob=CornersProblem -z 0.5
python pacman.py -l bigCorners -p SearchAgent -a fn=bs,prob=CornersProblem -z 0.5
python pacman.py -l bigCorners -p SearchAgent -a fn=ids,prob=CornersProblem -z 0.5
python pacman.py -l bigCorners -p SearchAgent -a fn=astar,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5



python pacman.py -l tinyCorners -p CornersGreedySearchAgent -z 0.5
python pacman.py -l mediumCorners -p CornersGreedySearchAgent  -z 0.5
python pacman.py -l bigCorners -p CornersGreedySearchAgent  -z 0.5
