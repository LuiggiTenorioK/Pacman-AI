# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    node = problem.getStartState()
    actions = []
    frontier = util.Stack()
    frontier.push((node,actions))
    explored = []
    while 1:
        if frontier.isEmpty():
            return []
        node,actions = frontier.pop()
        if problem.isGoalState(node):
            print('Search nodes in memory: %d' % len(path))
            return path
        explored.append(node)
        #print "sucesores:", problem.getSuccessors(node)
        for succ in problem.getSuccessors(node):
            child, direction, _ = succ
            path = actions + [direction]
            nodeFrontier = [x for x,_ in frontier.list]
            if ((child not in explored) and (child not in nodeFrontier)):
                frontier.push((child,path))       
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    node = problem.getStartState()
    actions = []

    if problem.isGoalState(node):
        return actions

    frontier = util.Queue()
    frontier.push((node,actions))
    explored = []
    while 1:
        if frontier.isEmpty():
            return []
        node,actions = frontier.pop()
        explored.append(node)

        for succ in problem.getSuccessors(node):
            child, direction, _ = succ
            path = actions + [direction]
            nodeFrontier = [x for x,_ in frontier.list]
            if ((child not in explored) and (child not in nodeFrontier)):
                if problem.isGoalState(child):
                    print('Search nodes in memory: %d' % len(path))
                    return path
                frontier.push((child,path))
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return aStarSearch(problem)
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    cost = lambda aPath: problem.getCostOfActions([x[1] for x in aPath]) + heuristic(aPath[len(aPath) - 1][0], problem)
    frontier = util.PriorityQueueWithFunction(cost)

    explored = []
    frontier.push([(problem.getStartState(), "Stop", 0)])
    while not frontier.isEmpty():
        path = frontier.pop()

        s = path[len(path) - 1]
        s = s[0]

        if problem.isGoalState(s):
            print('Search nodes in memory: %d' % len([x[1] for x in path][1:]))
            return [x[1] for x in path][1:]

        if s not in explored:
            explored.append(s)

            for successor in problem.getSuccessors(s):

                if successor[0] not in explored:
                    successorPath = path[:]
                    successorPath.append(successor)

                    frontier.push(successorPath)

    return []
    util.raiseNotDefined()

def depthLimitedSearch(problem, limit):
    node = problem.getStartState()
    actions = []

    frontier = util.Stack()
    frontier.push((node,actions,0))
    explored = []
    
    while 1:
        if frontier.isEmpty():
            return []
        node,actions,depth = frontier.pop()
        if depth > limit: continue

        if problem.isGoalState(node):
            print('Search nodes in memory: %d' % len(path))
            return path
        explored.append(node)
        for succ in problem.getSuccessors(node):
            child, direction, _ = succ
            path = actions + [direction]
            nodeFrontier = [x for x,_,_ in frontier.list]
            if ((child not in explored) and (child not in nodeFrontier)):
                frontier.push((child,path,depth+1))
    #util.raiseNotDefined()           

def iDeepeningSearch(problem): 
    "*** YOUR CODE HERE ***"
    for depth in range(500):
        result = depthLimitedSearch(problem,depth)
        if result != []:
            return result
    #return []
    
    #util.raiseNotDefined()

def bidirectionalSearch(problem):
    "*** YOUR CODE HERE ***"
    from game import Directions

    node_ini = problem.getStartState()
    actions_ini = []

    node_fin = problem.goal
    actions_fin = []
    #print "ini", node_ini
    #print "fin", node_fin
    if node_ini == node_fin:
        return []

    frontier_ini = util.Queue()
    frontier_ini.push((node_ini,actions_ini))
    explored_ini = []

    frontier_fin = util.Queue()
    frontier_fin.push((node_fin,actions_fin))
    explored_fin = []


    while 1:
        if frontier_ini.isEmpty() | frontier_fin.isEmpty():
            break
        node_ini,actions_ini = frontier_ini.pop()
        explored_ini.append(node_ini)

        for succ in problem.getSuccessors(node_ini):
            child, direction, _ = succ
            path = actions_ini + [direction]
            nodeFrontier = [x for x,_ in frontier_ini.list]
            if ((child not in explored_ini) and (child not in nodeFrontier)):
                goalList = [x for x,_ in frontier_fin.list]
                if (child in goalList) and (problem.isGoalState(child)):
                    for node,action in frontier_fin.list:
                        if (node == child):
                            route = [Directions.REVERSE[x] for x in action]
                            route.reverse()
                            print('Search nodes in memory: %d' % len(path + route))
                            return path + route
                frontier_ini.push((child,path))

        node_fin,actions_fin = frontier_fin.pop()
        explored_fin.append(node_fin)

        for succ in problem.getSuccessors(node_fin):
            child, direction, _ = succ
            path = actions_fin + [direction]
            nodeFrontier = [x for x,_ in frontier_fin.list]
            if ((child not in explored_fin) and (child not in nodeFrontier)):
                startList = [x for x,_ in frontier_ini.list]
                if (child in startList) and (problem.isGoalState(child)):
                    for node,action in frontier_ini.list:
                        if (node == child):
                            route = [Directions.REVERSE[x] for x in path]
                            route.reverse()
                            print('Search nodes in memory: %d' % len(action + route))
                            return action + route
                frontier_fin.push((child,path))

    #util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iDeepeningSearch
bs = bidirectionalSearch
