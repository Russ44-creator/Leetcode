# Python code for the above approach
class Node:

# constructor
	def __init__(self, v):
		self.val = v
		self.children = []

# Post-order traversal to find
# depth of all branches of every
# node of the tree
def postOrder(root):
	sum = 0
	valid = 1
	for child in root.children:
		binTrees = postOrder(child)
		if (binTrees[1] == 0):
			valid = 0
		sum += binTrees[0]

	if (valid == 1 and len(root.children) < 3):
		sum += 1
	else:
		valid = 0
	return [ sum, valid ]

def binTreesGeneric(root):
	if (root == None):
		return 0
	return postOrder(root)[0]



