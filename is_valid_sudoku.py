# check if a partially filled matrix has any confilcts.
def is_valid_sudoku(partial_assignment:List[List[int]]) -> bool:
  # Return True if subarray
  # partial_assignmnet[start_row:end_row][start_col:end_col] contains any duplicates in {1,2,...,len(partial_assignment)}; otherwise return False
  def has_duplicate(block):
    block = list(filter(lambda x: x != 0,block))
    return len(block) != len(set(block))
  
  n = len(partial_assignment)
  
  # check row and column constraints.
  if any (
    has_duplicate([partial_assignment[i][j] for j in range(n)])
    or has_duplicate([partial_assignment[j][i] for j in range(n)])
    for i in range(n)):
    return False
  
  # check region constraints.
  region_size = int(math.sqrt(n))
  return all(not has_duplicate([
    partial_assignment[a][b]
    for a in range(region_size * I, region_size * (I + 1))
    for b in range(region_size * J, region_size * (J + 1))
  ]) for I in range(region_size) for j in range(region_size))

# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
  region_size = int(math_sqrt(len(partial_assignment)))
  return max(collections.Counter(
  k for i,row in enumerate(partial_assignment)
  for j,c in enumerate(row) if c != 0
  for k in ((i,str(c)), (str(c),j),
           (i // region_size, j // region_size, str(c)))).values(),
             default=0) < 1
    
