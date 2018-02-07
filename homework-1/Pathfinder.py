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
import heapq

class Pathfinder:
    def createPath(prQ, problem):
        node = heapq.heappop(priorityQ)
        transitions = problem.transitions(node.state)
        for t in transitions:
            if parent is undefined:
                parent.totalCost = 0
            gOfN = problem.cost(node) + parent.totalCost
            child = SearchTreeNode(t[2], t[0], node, gOfN, problem.heuristic(problem.state))

    @staticmethod
    def solve(problem):
        # TODO: Implement A* graph search!
        # priority que :
        # start at root node -> get f(n) -> push to queue
        # pop off root -> add to resultpath -> push transitions & cooresponding costs to queue
        # pop off node w min cost -> add to resultpath
        # expand node to get transitions -> push transitions to queue
        # continue until goal reached
        resultPath = []
        rootNode = SearchTreeNode(problem.inital, None, None, 0, problem.heuristic(problem.inital))

        priorityQ = []
        heapq.heappush(priorityQ, rootNode)
        # add our path found with createPath to resultPath to be returned
        # need to add in param for createPath
        resultPath.append(Pathfinder.createPath(priorityQ, problem))
        return resultPath


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
