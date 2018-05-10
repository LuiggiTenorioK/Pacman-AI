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

def graphSearch(problem, frontier):
    explored = []
    frontier.push((problem.getStartState(),[]))

    while 1:
        if frontier.isEmpty():
            return []
        node, actions = frontier.pop()
        explored.append(node)
        for successor in problem.getSuccessors(node):
            path = actions + [successor[1]]
            if (successor[0] not in explored) and (successor not in [x for x,_ in frontier.list]):
                if problem.isGoalState(successor[0]):
                    print('Search nodes in memory: %d' % len(frontier.list))
                    return path
                frontier.push((successor[0], path))

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
    frontier = util.Stack()
    return graphSearch(problem, frontier)
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return []

    frontier = util.Queue()
    frontier.push((problem.getStartState(),[]))
    explored = []

    while 1:
        if frontier.isEmpty():
            return []
        node,actions = frontier.pop()
        explored.append(node)

        for successor in problem.getSuccessors(node):
            path = actions + [successor[1]]
            if ((successor[0] not in explored) and (successor[0] not in [x for x,_ in frontier.list])):
                if problem.isGoalState(successor[0]):
                    print('Search nodes in memory: %d' % len(frontier.list))
                    return path
                frontier.push((successor[0],path))

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

    incon=0

    while not frontier.isEmpty():
        path = frontier.pop()

        s = path[len(path) - 1]
        s = s[0]

        if problem.isGoalState(s):
            print('Search nodes in memory: %d' % len(frontier.heap)) #[x[1] for x in path][1:]
            print('Nro de inconsistencias: ' + str(incon))
            return [x[1] for x in path][1:]

        if s not in explored:
            explored.append(s)

            for successor in problem.getSuccessors(s):

                if successor[0] not in explored:
                    successorPath = path[:]
                    successorPath.append(successor)

                    frontier.push(successorPath)

                    if (heuristic(path[-1][0], problem) > problem.getCostOfActions(
                            [x[1] for x in successorPath]) + heuristic(successorPath[-1][0], problem)):
                        print(heuristic(path[-1][0], problem),
                              problem.getCostOfActions([x[1] for x in successorPath]) + heuristic(successorPath[-1][0],
                                                                                                  problem))
                        incon+=1

    print('Nro de inconsistencias: ' + str(incon))
    return []
    #util.raiseNotDefined()

def depthLimitedSearch(problem, limit):
    frontier = util.Stack()
    frontier.push((problem.getStartState(),[],0))
    explored = []
    
    while 1:
        if frontier.isEmpty():
            return []
        node,actions,depth = frontier.pop()
        if depth > limit: continue
        explored.append(node)
        for successor in problem.getSuccessors(node):
            path = actions + [successor[1]]
            if ((successor[0] not in explored) and (successor[0] not in [x for x,_,_ in frontier.list])):
                if problem.isGoalState(successor[0]):
                    print('Search nodes in memory: %d' % len(frontier.list))
                    return path
                frontier.push((successor[0],path,depth+1))
    #util.raiseNotDefined()           

def iDeepeningSearch(problem): 
    "*** YOUR CODE HERE ***"
    for depth in range(500):
        result = depthLimitedSearch(problem,depth)
        if result != []:
            return result
    return []
    
    #util.raiseNotDefined()

def bidirectionalSearch(problem):
    "*** YOUR CODE HERE ***"
    from game import Directions

    node_ini = problem.getStartState()
    node_fin = problem.goal
    if node_ini == node_fin:
        return []

    #Start: Start 
    frontier_ini = util.Queue()
    frontier_ini.push((node_ini,[]))
    explored_ini = []

    #Start: Goal
    frontier_fin = util.Queue()
    frontier_fin.push((node_fin,[]))
    explored_fin = []


    while 1:
        if frontier_ini.isEmpty() | frontier_fin.isEmpty():
            break
        node_ini,actions_ini = frontier_ini.pop()
        explored_ini.append(node_ini)

        for successor in problem.getSuccessors(node_ini):
            path = actions_ini + [successor[1]]
            if ((successor[0] not in explored_ini) and (successor[0] not in [x for x,_ in frontier_ini.list])):
                #Verify if child is already visited in goal path
                if (successor[0] in [x for x,_ in frontier_fin.list]):
                    for node,action in frontier_fin.list:
                        if (node == successor[0]):
                            route = [Directions.REVERSE[x] for x in action]
                            route.reverse()
                            print('Search nodes in memory: %d' % len(frontier_ini.list + frontier_fin.list)) #path + route
                            return path + route
                frontier_ini.push((successor[0],path))

        node_fin,actions_fin = frontier_fin.pop()
        explored_fin.append(node_fin)

        for successor in problem.getSuccessorsReverse(node_fin):
            path = actions_fin + [successor[1]]
            if ((successor[0] not in explored_fin) and (successor[0] not in [x for x,_ in frontier_fin.list])):
                #Verify if child is already visited in start path
                if (successor[0] in [x for x,_ in frontier_ini.list]):
                    for node,action in frontier_ini.list:
                        if (node == successor[0]):
                            route = [Directions.REVERSE[x] for x in path]
                            route.reverse()
                            print('Search nodes in memory: %d' % len(frontier_ini.list + frontier_fin.list)) #action + route
                            return action + route
                frontier_fin.push((successor[0],path))

    #util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iDeepeningSearch
bs = bidirectionalSearch
