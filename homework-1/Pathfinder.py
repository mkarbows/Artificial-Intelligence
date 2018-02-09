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

class Pathfinder:
    def generateChildren(problem, prQ, parent, vistedNodes):
        parent.children = MazeProblem.transitions(problem, parent.state)
        for child in parent.children:
            gOfN = parent.totalCost + child[1]
            if not(child[2] in vistedNodes):
                vistedNodes.append(child[2])
                # incrementing the count
                problem.count += 1
                prQ.put(SearchTreeNode(child[2], child[0], parent, gOfN, MazeProblem.heuristic(problem, child[2])))

    def createPath(problem, goalNode):
        resultPath = []
        currentNode = goalNode
        while currentNode.parent:
            resultPath.append(currentNode.action)
            currentNode = currentNode.parent
        resultPath.reverse()
        # printing the count for the report
        print(problem.count)
        return resultPath

    @staticmethod
    def solve(problem):
        pQ = queue.PriorityQueue()
        rootNode = SearchTreeNode(problem.initial, None, None, 0, problem.heuristic(problem.initial))        # if we have explored a child already then we don't need ot explore in the future
        nodesVisited = [problem.initial]
        pQ.put(rootNode)
        while pQ.qsize():
            nextNode = pQ.get()
            if problem.goalTest(nextNode.state):
                return Pathfinder.createPath(problem, nextNode)
            Pathfinder.generateChildren(problem, pQ, nextNode, nodesVisited)
        # printing the count
        print(problem.count)
        return []

class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX",
                "X..GX",
                "X...X",
                "X*..X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX",
                "XG..X",
                "XX..X",
                "X*..X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXX",
                "X..GX",
                "X.MMX",
                "X*..X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze4(self):
        maze = ["XXXXXX",
                "X....X",
                "X*.XXX",
                "X..XGX",
                "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertFalse(soln)

    def test_maze5(self):
        maze = ["XXXXXXXX",
                "X......X",
                "X*.X..XX",
                "X..XGXXX",
                "XXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 6)

    def test_maze6(self):
        maze = ["XXXXXXXX",
                "X......X",
                "X*.XX.XX",
                "X..XGXXX",
                "XXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertFalse(soln)

    def test_maze7(self):
        maze = ["XXXXXXX",
                "X..G..X",
                "XMMM.MX",
                "X*....X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 6)

    def test_maze8(self):
        maze = ["XXXXXXXXX",
                "X.XGX...X",
                "XMXXXMMMX",
                "X*......X",
                "XXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertFalse(soln)


if __name__ == '__main__':
    unittest.main()
