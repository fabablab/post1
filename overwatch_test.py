import unittest
import overwatch

class TestOverwatch(unittest.TestCase):
  def test_is_interaction(self):
    # d = 1.0, v = 2.0
    g = overwatch.Game([ overwatch.Player(0.0, 0.0, 1.0, 1.0) ], [ overwatch.Player(1.0, 1.0, 0.0, 1.0) ])
    g.updates(0.6)
    assert(g.num_interactions == 1)

    # d = 0.5, v = 1.1
    g = overwatch.Game([ overwatch.Player(0.5, 0.5, 0.0, 0.1) ], [ overwatch.Player(0.0, 0.0, 1.0, 1.0) ])
    g.updates(0.455)
    assert(g.num_interactions == 1)

    # d = 0.1, v = 0.05
    g = overwatch.Game([ overwatch.Player(0.0, -100.0, 1.0, 1.05) ], [ overwatch.Player(0.1, 100.0, 1.0, 1.0) ])
    g.updates(2.1)
    assert(g.num_interactions == 1)

    # no interaction
    g = overwatch.Game([ overwatch.Player(0.0, 0.0, -1.0) ], [ overwatch.Player(1.0, 1.0, 2.0) ])
    g.updates(1.0)
    assert(g.num_interactions == 0)

if __name__ == '__main__':
    unittest.main()
