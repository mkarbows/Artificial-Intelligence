'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
import queue

# import queue instead and then you can make a priorityq from that

class Pathfinder:
    def generateChildren(problem, prQ, parent, vistedNodes):
        print(parent.state)
        parent.children = MazeProblem.transitions(problem, parent.state)
        for child in parent.children:
            gOfN = parent.totalCost + child[1]
            if not(child[2] in vistedNodes):
                vistedNodes.append(child[2])
                prQ.put(SearchTreeNode(child[2], child[0], parent, gOfN, problem.heuristic(problem, child[2])))

    def createPath(goalNode):
        resultPath = []
        currentNode = goalNode
        while currentNode.parent:
            resultPath.append(currentNode.action)
            currentNode = currentNode.parentCost
        resultPath.reverse()
        return resultPath

    # createPath:
    # node = heapq.heappop(prQ)
    # transitions = problem.transitions(node.state)
    # # print(state)
    # parentCost = None
    # for t in transitions:
    #     if problem.parent.totalCost is None:
    #         parentCost = 0
    #     else:
    #         parentCost = problem.parent.totalCost
    #     gOfN = problem.cost(node) + parentCost
    #     child = SearchTreeNode(t[2], t[0], node, gOfN, problem.heuristic(problem))

    # @staticmethod ???????????
    def solve(problem):
        # TODO: Implement A* graph search!
        # priority que :
        # start at root node -> get f(n) -> push to queue
        # pop off root -> add to resultpath -> push transitions & cooresponding costs to queue
        # pop off node w min cost -> add to resultpath
        # expand node to get transitions -> push transitions to queue
        # continue until goal reached
        pQ = queue.PriorityQueue()
        rootNode = SearchTreeNode(problem.initial, None, None, 0, problem.heuristic(problem.initial))        # if we have explored a child already then we don't need ot explore in the future
        nodesVisited = [problem.initial]
        pQ.put(rootNode)
        while pQ.qsize():
            nextNode = pQ.get()
            if problem.goalTest(nextNode.state):
                return Pathfinder.makePath(nextNode)
            Pathfinder.generateChildren(problem, pQ, nextNode, nodesVisited)
        return []

        # priorityQ = []
        # heapq.heappush(priorityQ, rootNode)
        # # add our path found with createPath to resultPath to be returned
        # # need to add in param for createPath
        # resultPath.append(Pathfinder.createPath(priorityQ, problem))
        # return resultPath


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXX", "X..GX", "X.MMX", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze4(self):
        maze = ["XXXXXX", "X....X", "X*.XXX", "X..XGX", "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertFalse(soln)


if __name__ == '__main__':
    unittest.main()
