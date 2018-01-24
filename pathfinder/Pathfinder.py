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
        # Pop the next node in the queue and then find its possible transitions.
        node = queue.pop(0)
        transitions = problem.transitions(node.state)

        for t in transitions:
            # Create a node from the transition.
            newNode = SearchTreeNode(t[1], t[0], node)
            if problem.goalTest(newNode.state):
                # Congrats! You found a node whose state is a goal.
                return newNode
            # If it is not a goal state, add it to the queue.
            queue.append(newNode)

        # Continue the search with the updated queue.
        return Pathfinder.findGoal(queue, problem)

    def createPath(node):
        # Working from the goal node to the initial node, build the
        # path.
        solution = []
        currentNode = node

        # The inital node has no parent.
        while currentNode.parent:
            # Add the action to the beginning of the list since we are starting
            # from the end of the path.
            solution.insert(0, currentNode.action)
            currentNode = currentNode.parent

        # Return the solution once you get to the initial node.
        return solution

    def solve(problem):
        # The root node has no action or parent.
        rootNode = SearchTreeNode(problem.initial, None, None)

        # The search tree (implemented in a queue) begins by only containing
        # the root node.
        queue = [rootNode]

        # Find a node that is a goal.
        goalNode = Pathfinder.findGoal(queue, problem)

        # Return the path that gets you to that node.
        return Pathfinder.createPath(goalNode)

class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = [
            "XXXXX",
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
        maze = [
            "XXXXX",
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
        maze = [
            "XXXXX",
            "XX..X",
            "XX.GX",
            "X*..X",
            "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 3)

    def test_maze4(self):
        maze = [
            "XXXGX",
            "XG..X",
            "XX..X",
            "X*..X",
            "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze5(self):
        maze = [
            "XXXXX",
            "XGXGX",
            "XX..X",
            "X*..X",
            "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze6(self):
        maze = [
            "XXXXX",
            "X*.XX",
            "XX..X",
            "XG..X",
            "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

if __name__ == '__main__':
    unittest.main()
