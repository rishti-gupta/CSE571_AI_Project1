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

# function for general search in a tree
def searchTree(problem, fringe):
    fringe.push((None, problem.getStartState(), None, 0))
    visited = dict()

    # add the successor nodes in the fringe if not visited before
    def addNodes(start, cost):
        for next_state, curr_action, add_cost in problem.getSuccessors(start):
            if hash(next_state) not in visited:
                fringe.push((start, next_state, curr_action, cost + add_cost))

    # mapping the successor node to the hash map (with a hash code)
    def nextNode(end_node):
        state, curr_action = visited[hash(end_node)]
        actions_list = []

        while curr_action is not None:
            actions_list.append(curr_action)
            state, curr_action = visited[hash(state)]

        return actions_list[::-1]

    while not fringe.isEmpty():
        start, next_state, curr_action, cost = fringe.pop()

        if hash(next_state) in visited:
            continue

        visited[hash(next_state)] =  (start, curr_action)

        # comparing the current state with the goal state
        if problem.isGoalState(next_state):
            return nextNode(next_state)

        addNodes(next_state, cost)

    return []

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
    # implementation using a stack
    return searchTree(problem, util.Stack())
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # implementation using a queue
    return searchTree(problem, util.Queue())
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # defining the priority function according to which priority queue has to be implemented
    def priorityFunction(item):
        return item[-1]

    # implementation using a priority queue
    ucs_fringe = util.PriorityQueueWithFunction(priorityFunction)
    return searchTree(problem, ucs_fringe)
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # defining the priority function according to which priority queue has to be implemented
    def priorityFunction(item):
        return item[-1] + heuristic(item[1], problem = problem)

    # implementation using a priority queue
    astar_fringe = util.PriorityQueueWithFunction(priorityFunction)
    return searchTree(problem, astar_fringe)
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
