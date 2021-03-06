@echo off
echo Este batch ejecutara todos los problemas uno por uno.

echo Empecemos con medium corners.

python pacman.py -l mediumCorners -p SearchAgent -a fn=dfs,prob=CornersProblem -z 0.5
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem -z 0.5
python pacman.py -l mediumCorners -p SearchAgent -a fn=bs,prob=CornersProblem -z 0.5
python pacman.py -l mediumCorners -p SearchAgent -a fn=ids,prob=CornersProblem -z 0.5
python pacman.py -l mediumCorners -p SearchAgent -a fn=astar,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5

echo Seguimos con big corners.

python pacman.py -l bigCorners -p SearchAgent -a fn=dfs,prob=CornersProblem -z 0.5
python pacman.py -l bigCorners -p SearchAgent -a fn=bfs,prob=CornersProblem -z 0.5
python pacman.py -l bigCorners -p SearchAgent -a fn=bs,prob=CornersProblem -z 0.5

echo La siguiente busqueda demorará en ejecutarse unos 7-8 minutos.

python pacman.py -l bigCorners -p SearchAgent -a fn=ids,prob=CornersProblem -z 0.5
python pacman.py -l bigCorners -p SearchAgent -a fn=astar,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5

echo Terminamos con el agente codicioso.

python pacman.py -l tinyCorners -p CornersGreedySearchAgent -z 0.5
python pacman.py -l mediumCorners -p CornersGreedySearchAgent  -z 0.5
python pacman.py -l bigCorners -p CornersGreedySearchAgent  -z 0.5

echo Eso es todo.