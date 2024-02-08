import math

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_width_btree(root):
	# Verifica a quantidade de niveis de uma arvore binaria
	treeSize = len(root)
	treeDepth = math.log2(treeSize)
    treeDepthCeil = math.ceil(treeDepth)

    isTreeComplete = treeDepth < treeDepthCeil

	return treeDepth