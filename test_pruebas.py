def suma(n, m):
  return n + m

def test_suma():
  assert suma(1, 2) == 3
  assert suma(2, 3) != 6
  assert suma(2, 3) != 10
