from typing import List
from dataclasses import dataclass
import numpy as np

NUMBER_OF_PEOPLE_TO_PAIR = 25
RANDOM_SEED = 33314  # change to any integer you want

@dataclass
class Pair:
  lucky_guy: int
  angel: int
  def __repr__(self):
    return f"Angel [{self.angel:3d}] shows love for lucky guy [{self.lucky_guy:3d}]"


def main() -> None:
  people_indices = np.arange(1, NUMBER_OF_PEOPLE_TO_PAIR + 1)
  pairs = draw_random_pairs(people_indices)
  for p in pairs:
    print(p)


def draw_random_pairs(indices: np.ndarray) -> List[Pair]:
  rng = np.random.default_rng(seed=RANDOM_SEED)
  to_chooose_from = indices.tolist()
  pairs = []
  DRAW_SIZE = 2
  while len(to_chooose_from) > DRAW_SIZE:
    a, b = rng.choice(to_chooose_from, DRAW_SIZE, replace=False)
    pair = Pair(a, b)
    pairs.append(pair)
    to_chooose_from.remove(a)
    to_chooose_from.remove(b)

  if to_chooose_from:
    print(to_chooose_from, "left")
  return pairs


if __name__ == "__main__":
  main()