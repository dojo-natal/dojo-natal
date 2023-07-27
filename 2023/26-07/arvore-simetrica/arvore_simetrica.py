def walk(node, auxcount=None):
  if node is None:
    return node, []
  return node, [n for n in [node.val, walk(node.left), walk(node.right)] if n is int]


def isSymetric(root) -> bool:
  seq_left = walk(root.left, auxcount=[])[1]
  seq_right = walk(root.right, auxcount=[])[1]
  print(seq_left, '+++', seq_right)
  print('----')

  if seq_left == seq_right:
    return True
  return False
  