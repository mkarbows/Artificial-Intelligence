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

class Pathfinder:

    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]
    def findGoal(queue, problem):
        node = queue[0]
        print("state",node.state)
        transitions = problem.transitions(node.state)
        print("transitions", transitions)

        # generate children
        for t in transitions:
            newNode = SearchTreeNode(t[1], t[0], node)
            if problem.goalTest(newNode.state):
                print("goal", newNode.state)
                return newNode
            queue.append(newNode)
            node.children.append(newNode)
        queue.pop(0)

        # expand children
        return Pathfinder.findGoal(queue, problem)

    def createPath(node):
        solution = []
        currentNode = node
        while currentNode.parent:
            solution.insert(0, currentNode.action)
            currentNode = currentNode.parent
        print("solution", solution)
        return solution

    def solve(problem):
        # TODO: Implement breadth first tree search!
        queue = []
        rootNode = SearchTreeNode(problem.initial, None, None)
        queue.append(rootNode)
        return Pathfinder.createPath(Pathfinder.findGoal(queue, problem))

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
        print("should be true", solnTest[1])
        print("should be 4", solnTest[0])
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    # TODO: Add more unit tests!

if __name__ == '__main__':
    unittest.main()
