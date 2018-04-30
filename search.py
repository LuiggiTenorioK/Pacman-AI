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
                return path
        explored.append(node)
        for succ in problem.getSuccessors(node):
            child, direction, cost = succ
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
            child, direction, cost = succ
            path = actions + [direction]
            nodeFrontier = [x for x,_ in frontier.list]
            if ((child not in explored) and (child not in nodeFrontier)):
                if problem.isGoalState(child):
                    return path
                frontier.push((child,path))
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def iDeepeningSearch(problem): 
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def bidirectionalSearch(problem):
    "*** YOUR CODE HERE ***"
    from game import Directions
    nodeStart = problem.getStartState()
    actionsStart = []
    nodeGoal = problem.goal
    actionsGoal = []

    if nodeStart == nodeGoal:
        return []

    #Inicializar las fronteras partiendo del inicio
    frontierStart = util.Queue()
    frontierStart.push((nodeStart,actionsStart))
    exploredStart = []
    #Inicializar las fronteras partiendo de la meta
    frontierGoal = util.Queue()
    frontierGoal.push((nodeGoal,actionsGoal))
    exploredGoal = []

    while 1:
        if frontierGoal.isEmpty() | frontierStart.isEmpty():
            return []

        node_S,actions_S = frontierStart.pop()
        exploredStart.append(node_S)
        node_G,actions_G = frontierGoal.pop()
        exploredGoal.append(node_G)

        #BFS para el inicio
        for succ in problem.getSuccessors(node_S):
            child,direction,cost = succ
            path = actions_S + [direction]
            nodeFrontier = [x for x,_ in frontierStart.list]
            if (child not in exploredStart) and (child not in nodeFrontier):
                if (child,Diretcions.REVERSE[direction]) in frontierGoal.list:
                    print "Encontrado en start"
                    for node,actions in frontierGoal.list:
                        if (child == node):
                            route = [Directions.REVERSE[x] for x in actions]
                            return actions_S + route
                frontierStart.push((child,path))

        #BFS para el goal 
        for succ in problem.getSuccessors(node_G):
            child,direction,cost = succ
            path = actions_G + [direction]
            nodeFrontier = [x for x,_ in frontierGoal.list]
            if (child not in exploredGoal) and (child not in nodeFrontier):
                if (child,Directions.REVERSE[direction]) in frontierStart.list:
                    print "Encontrado en goal"
                    for node,actions in frontierStart.list:
                        if (child == node):
                            route = [Directions.REVERSE[x] for x in path]
                            return actions + route
                frontierGoal.push((child,path))



    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iDeepeningSearch
bs = bidirectionalSearch
