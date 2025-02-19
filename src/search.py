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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    
    visited = {} #Dictionary of coords we have already been to and what direction we arrived from
    solution = [] #List of directions in order to reach the goal
    stack = util.Stack() #Last in, first out stack of fringe nodes to still explore
    route = {} #Dictionary of coords we are adding to the fringe and what coord we got there from
    
    start = problem.getStartState() #Retrieve the starting coords
    stack.push((start, '', 0)) #Push the starting tuple to the stack. (Start coords, direction arrived from, cost)
    visited[start] = '' #Set the start coordinate as having been travelled to, no arrival direction since we spawned here
    
    if problem.isGoalState(start): #If our spawn is the goal, return an empty set of solution directions
        return solution #Return our solution
    
    while not (stack.isEmpty()): #While we have not run out of nodes to try exploring
        node = stack.pop() #Retrieve the most recently added node from the LIFO stack. (Coords, direction arrived from, cost)
        visited[node[0]] = node[1] #Sets the current coords as having been travelled to, and that we got here from the direction retrieved from our current node
        
        if problem.isGoalState(node[0]): #If the current node is our goal
            child = node[0] #Set the child node to the coords of our goal node
            break #Break out of the loop
        
        for i in problem.getSuccessors(node[0]): #Loop through each of the possible children of our node
            if i[0] not in visited.keys(): #Only count the child node if it hasn't been visited before
                route[i[0]] = node[0] #Track how we got to this node. Child coords are matched to parent coords
                stack.push(i) #Add the new node to our LIFO stack
                
    while (child in route.keys()): #Cycle through our discovered route starting with the goal node
        parent = route[child] #Retrieve the location of the parent node from the route using child as the key
        solution.insert(0, visited[child]) #Add the direction that we arrived at the child node from the parent node to the solution
        child = parent #Set the parent as the new child, stepping backwards through the route until we arrive at the starting point
        
    return solution #Return the solution


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    visited = {} #Dictionary of coords we have already been to and what direction we arrived from
    solution = [] #List of directions in order to reach the goal
    queue = util.Queue() #First in, first out queue of fringe nodes to still explore
    route = {} #Dictionary of coords we are adding to the fringe and what coord we got there from
    
    start = problem.getStartState() #Retrieve the starting coords
    queue.push((start, '', 0)) #Push the starting tuple to the queue. (Start coords, direction arrived from, cost)
    visited[start] = '' #Set the start coordinate as having been travelled to, no arrival direction since we spawned here
    
    if problem.isGoalState(start): #If our spawn is the goal, return an empty set of solution directions
        return solution #Return our solution
    
    while not (queue.isEmpty()): #While we have not run out of nodes to try exploring
        node = queue.pop() #Retrieve the most recently added node from the FIFO queue. (Coords, direction arrived from, cost)
        visited[node[0]] = node[1] #Sets the current coords as having been travelled to, and that we got here from the direction retrieved from our current node
        
        if problem.isGoalState(node[0]): #If the current node is our goal
            child = node[0] #Set the child node to the coords of our goal node
            break #Break out of the loop
        
        for i in problem.getSuccessors(node[0]): #Loop through each of the possible children of our node
            if i[0] not in visited.keys(): #Only count the child node if it hasn't been visited before
                route[i[0]] = node[0] #Track how we got to this node. Child coords are matched to parent coords
                queue.push(i) #Add the new node to our FIFO queue
                
    while (child in route.keys()): #Cycle through our discovered route starting with the goal node
        parent = route[child] #Retrieve the location of the parent node from the route using child as the key
        solution.insert(0, visited[child]) #Add the direction that we arrived at the child node from the parent node to the solution
        child = parent #Set the parent as the new child, stepping backwards through the route until we arrive at the starting point
        
    return solution #Return the solution


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
