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
    # Starting Node
    startNode=problem.getStartState()
    if(problem.isGoalState(startNode)):
        return []
    stack = util.Stack()
    
    # visitedArray is to track the all the visited nodes so we dont traverse them again 
    visitedArray=[]
    
    # Node and Direction gets pushed on to Stack 
    # Direction list is maintained to keep track of the path from Start Node
    stack.push((startNode,[]))
    while not stack.isEmpty():
        currentNode,directions=stack.pop()
        if currentNode not in visitedArray:
            # Appending the Visited Node to visitedArray list
            visitedArray.append(currentNode)

            # If Current Node is Goal state we return Direction list from Start Node
            if problem.isGoalState(currentNode):
                return directions
            # Traversing the Adjacency List which is equivalent to Successors list here 
            for successorNode,direction,cost in problem.getSuccessors(currentNode):
                nextDirection=directions[:]
                nextDirection.append(direction)
                stack.push((successorNode,nextDirection))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    # Starting Node
    startNode=problem.getStartState()
    if(problem.isGoalState(startNode)):
        return []
    queue=util.Queue()

    # visitedArray is to track the all the visited nodes so we dont traverse them again 
    visitedArray=[]

    # Node and Direction List gets pushed on to Queue 
    # Direction list is maintained to keep track of the path from Start Node
    queue.push((startNode,[]))

    while not queue.isEmpty():
        currentNode,directions=queue.pop()
        if currentNode not in visitedArray:
            # Appending the Visited Node to visitedArray list
            visitedArray.append(currentNode)

            # If Current Node is Goal state we return Direction list from Start Node
            if problem.isGoalState(currentNode):
                return directions
            
            # Traversing the Adjacency List which is equivalent to Successors list here 
            for successorNode,direction,cost in problem.getSuccessors(currentNode):
                nextDirection=directions[:]
                nextDirection.append(direction)
                queue.push((successorNode,nextDirection))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    # Starting Node
    startNode=problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    priorityQueue=util.PriorityQueue()

    # visitedArray is to track the all the visited nodes so we dont traverse them again
    visitedArray=[]

    # priorityQueue implements minHeap 
    # Node,Direction List and Cost gets pushed on to PriorityQueue along with priority
    # Direction list is maintained to keep track of the path from Start Node
    # Aggregate Cost is send to succcesor Nodes
    priorityQueue.push((startNode,[],0),0)
    while not priorityQueue.isEmpty():
        currentNode,directions,cost=priorityQueue.pop()
        if currentNode not in visitedArray:
            # Appending the Visited Node to visitedArray list
            visitedArray.append(currentNode)

            # If Current Node is Goal state we return Direction list from Start Node
            if problem.isGoalState(currentNode):
                return directions
            
            # Traversing the Adjacency List which is equivalent to Successors list here
            for successorNode,direction,successorCost in problem.getSuccessors(currentNode):
                nodeCost=successorCost+cost
                nextDirection=directions[:]
                nextDirection.append(direction)
                priorityQueue.push((successorNode,nextDirection,nodeCost),nodeCost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    # Starting Node
    startNode=problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    priorityQueue=util.PriorityQueue()

    # visitedArray is to track the all the visited nodes so we dont traverse them again
    visitedArray=[]

    # priorityQueue implements minHeap 
    # Node,Direction List and Cost gets pushed on to PriorityQueue along with Heuristic value generated by Heuristic Function here
    # Direction list is maintained to keep track of the path from Start Node
    # Aggregate Cost is send to succcesor Nodes
    priorityQueue.push((startNode,[],0),heuristic(startNode,problem))
    while not priorityQueue.isEmpty():
        currentNode,directions,cost=priorityQueue.pop()
        if currentNode not in visitedArray:
            # Appending the Visited Node to visitedArray list
            visitedArray.append(currentNode)

            # If Current Node is Goal state we return Direction list from Start Node
            if problem.isGoalState(currentNode):
                return directions
            
            # Traversing the Adjacency List which is equivalent to Successors list here
            for successorNode,direction,successorCost in problem.getSuccessors(currentNode):
                nodeCost=successorCost+cost
                heuristicCost=nodeCost+heuristic(successorNode,problem)
                nextDirection=directions[:]
                nextDirection.append(direction)
                priorityQueue.push((successorNode,nextDirection,nodeCost),heuristicCost)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch