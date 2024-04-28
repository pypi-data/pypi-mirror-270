
from typing import Protocol
from .Point import Point
from ._common import np, List



def dominance_ranking(L: List[Point]):
  rank = 1
  matrix_bool = np.zeros((len(L), len(L)))
  for i in range(len(L)):
    for j in range(len(L)):
      if i != j:
        if L[i] > L[j]:
          matrix_bool[i][j] = 1
        else:
          matrix_bool[i][j] = 0
  
  return np.add(np.sum(matrix_bool, axis=1), 1)

class performanceIndicator(Protocol):

  def compute(self):
    ...

  def weaklyDominates(self):
    ...
  
  def stronglyDominates(self):
    ...

  def hvRecursive(self):
    ...

  def preProcess(self):
    ...

  def sortByDimension(self):
    ...
  

    
if __name__ == "__main__":
  pass