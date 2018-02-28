'''
Megan Karbowski

MazeClause.py

Specifies a Propositional Logic Clause formatted specifically
for Grid Maze Pathfinding problems. Clauses are a disjunction of
GridPropositions (2-tuples of (symbol, location)) mapped to
their negated status in the sentence.
'''
import unittest
import itertools

class MazeClause:

    def __init__ (self, props):
        self.props = {}
        self.valid = False

        mazeProps = None
        negationStatus = None
        for p in props:
            # mazeProps is the first element in the tuple given by the props argument
            mazeProps = p[0]
            # second element in the props tuple
            negationStatus = p[1]
            self.props[mazeProps] = negationStatus
        # deal with validity
        same1 = None
        same2 = None
        # for each two keys in dict, compare them
        itertools.combinations(self.props, 2):
            # check if coordinates are same
            if a[1] == b[1]:
                # check if vars are the same
                if a[0] == b[0]:
                    # save keys and negation status's
                    same1 = a
                    same2 = b
        if same1 is not None:
            checkSame1 = self.props.get(same1)
            checkSame2 = self.props.get(same2)
            if checkSame1 != checkSame2:
                self.valid = True
                self.props = {}

    def getProp (self, prop):
        valueOfProp = None
        for m in self.props:
            if m == prop:
                answer = self.props.get(m)
                valueOfProp = answer
        return valueOfProp

    def isValid (self):
        return self.valid

    def isEmpty (self):
        empty = True
        if self.props:
            empty = False
        return empty

    def __eq__ (self, other):
        return self.props == other.props and self.valid == other.valid

    def __hash__ (self):
        # Hashes an immutable set of the stored props for ease of
        # lookup in a set
        return hash(frozenset(self.props.items()))

    def __str__ (self):
        return ""

    @staticmethod
    def resolve (c1, c2):
        results = set()
        ansDict = {}
        for firstKey in c1.props:
            if firstKey in c2.props:
                value1 = c1.getProp(firstKey)
                value2 = c2.getProp(firstKey)
                if value1 != value2:
                    # del c1.props[key1]
                    # del c2.props[key1]
                    # combine c1 and c2 into new dictionary
                    ansDict.update(c1.props)
                    ansDict.update(c2.props)
                    newMazeC = MazeClause(ansDict)
                    results.add(newMazeC)
        return results


class MazeClauseTests(unittest.TestCase):
    def test_mazeprops1(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (2, 1)), True), (("Y", (1, 2)), False)])
        self.assertTrue(mc.getProp(("X", (1, 1))))
        self.assertTrue(mc.getProp(("X", (2, 1))))
        self.assertFalse(mc.getProp(("Y", (1, 2))))
        self.assertTrue(mc.getProp(("X", (2, 2))) is None)
        self.assertFalse(mc.isEmpty())

    def test_mazeprops2(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (1, 1)), True)])
        self.assertTrue(mc.getProp(("X", (1, 1))))
        self.assertFalse(mc.isEmpty())

    def test_mazeprops3(self):
        mc = MazeClause([(("X", (1, 1)), True), (("Y", (2, 1)), True), (("X", (1, 1)), False)])
        self.assertTrue(mc.isValid())
        self.assertTrue(mc.getProp(("X", (1, 1))) is None)
        self.assertFalse(mc.isEmpty())

    def test_mazeprops4(self):
        mc = MazeClause([])
        self.assertFalse(mc.isValid())
        self.assertTrue(mc.isEmpty())

    def test_mazeprops5(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops6(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([]) in res)

    def test_mazeprops7(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (2, 2)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), True), (("Y", (2, 2)), True)]) in res)

    def test_mazeprops8(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops9(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops10(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True), (("W", (1, 1)), False)]) in res)

if __name__ == "__main__":
    unittest.main()
