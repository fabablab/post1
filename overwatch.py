"""TODO
"""

import numpy as np

class Player(object):
  def __init__(self, x, x_spawn, x_target, speed=1.0):
    self.x = x
    self.x_spawn = x_spawn
    self.x_target = x_target
    self.x_prev = self.x
    self.speed = speed
    assert(self.speed >= 0.0)

  def move_towards_target(self, dt):
    self.x_prev = self.x
    self.x = self.x + np.sign(self.x_target - self.x) * self.speed * dt

  def update(self, dt):
    # Set x_target here later
    pass

  def die(self):
    self.x = self.x_spawn
    self.x_prev = self.x_spawn

class Game(object):
  def __init__(self, attackers, defenders):
    self.attackers = attackers
    self.defenders = defenders
    self.dt = 0.01
    self.t = 0.0
    self.num_interactions = 0

  def update(self):
    for p in self.attackers + self.defenders:
      p.update(self.dt)

    for p in self.attackers + self.defenders:
      p.move_towards_target(self.dt)

    for a in self.attackers:
      for b in self.defenders:
        if self.is_interaction(a, b):
          if np.random.uniform() < 0.5:
            a.die()
          else:
            b.die()

    self.t = self.t + self.dt

  def updates(self, DT):
    ti = self.t
    tf = self.t + DT
    for tau in np.arange(ti, tf, step=self.dt):
      self.update()

  def is_interaction(self, a, b):
    if np.sign(a.x - b.x) * np.sign(a.x_prev - b.x_prev) == -1:
      self.num_interactions = self.num_interactions + 1
      return True
    return False

class Scenario1(Game):
  def __init__(self):
    Game.__init__(self, [Player(1.0, 1.0, 0.0)], [Player(0.0, 0.0, 1.0)])

  def update(self):
    Game.update(self)
    print ",".join(str(x) for x in [self.t, self.attackers[0].x, self.defenders[0].x])

def main():
  scenario = Scenario1()
  scenario.updates(5.0)

if __name__ == '__main__':
  main()
