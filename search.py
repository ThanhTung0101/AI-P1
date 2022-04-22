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
    iStart = problem.getStartState()
    if problem.isGoalState(iStart): return []
    DFSStack = util.Stack()
    daThamDFS = []
    DFSStack.push((iStart, []))

    while not DFSStack.isEmpty():
        i, actions = DFSStack.pop()
        if i not in daThamDFS:
            daThamDFS.append(i)
            if problem.isGoalState(i): return actions
            for viTriMoi, action, cost in problem.getSuccessors(i):
                buocNhayMoi = actions + [action]
                DFSStack.push((viTriMoi, buocNhayMoi))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    duyetBFS = Queue()
    daThamBFS = []
    viTri = []

    if problem.isGoalState(problem.getStartState()):
        return []
    duyetBFS.push((problem.getStartState(),[]))
    while not duyetBFS.isEmpty():
        i, viTri = duyetBFS.pop()
        daThamBFS.append(i)
        if problem.isGoalState(i):
            return viTri
        iProblem = problem.getSuccessors(i)
        if iProblem:
            for item in iProblem:
                if item[0] not in daThamBFS and item[0] not in (state[0] for state in duyetBFS.list):
                    viTriMoi = viTri + [item[1]]
                    duyetBFS.push((item[0],viTriMoi))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue
    duyetUCS = PriorityQueue()
    daThamUCS = []
    viTri = []
    if problem.isGoalState(problem.getStartState()):
        return []
    duyetUCS.push((problem.getStartState(),[]),0)

    while not duyetUCS.isEmpty():
        i, viTri = duyetUCS.pop()
        daThamUCS.append(i)
        if problem.isGoalState(i):
            return viTri
        iProblem = problem.getSuccessors(i)
        if iProblem:
            for item in iProblem:
                if item[0] not in daThamUCS and (item[0] not in (state[2][0] for state in duyetUCS.heap)):
                    viTriMoi = viTri + [item[1]]
                    pri = problem.getCostOfActions(viTriMoi)
                    duyetUCS.push((item[0],viTriMoi),pri)
                elif item[0] not in daThamUCS and (item[0] in (state[2][0] for state in duyetUCS.heap)):
                    for state in duyetUCS.heap:
                        if state[2][0] == item[0]:
                            viTriProblemCu = problem.getCostOfActions(state[2][1])
                    viTriProblemMoi = problem.getCostOfActions(viTri + [item[1]])
                    if viTriProblemCu > viTriProblemMoi:
                        viTriMoi = viTri + [item[1]]
                        duyetUCS.update((item[0],viTriMoi),viTriProblemMoi)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    iStart = problem.getStartState()
    if problem.isGoalState(iStart):
        return []
    daThamAStart = []
    duyetAStart = util.PriorityQueue()
    duyetAStart.push((iStart, [], 0), 0)
    while not duyetAStart.isEmpty():
        i, actions, prevCost = duyetAStart.pop()
        if i not in daThamAStart:
            daThamAStart.append(i)
            if problem.isGoalState(i):
                return actions
            for viTriMoi, action, cost in problem.getSuccessors(i):
                buocNhayMoi = actions + [action]
                newCostToNode = prevCost + cost
                heuristicCost = newCostToNode + heuristic(viTriMoi,problem)
                duyetAStart.push((viTriMoi, buocNhayMoi, newCostToNode),heuristicCost)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
