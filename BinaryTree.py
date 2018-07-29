class TreeNode(object):
	def __init__(self,value=None):
		self.value = value
		self.left = None
		self.right = None

class Solutuon(object):

	def preorder_traverse(self,node):
		if node is None:
			return None
		print(node.value,end=' ')
		self.preorder_traverse(node.left)
		self.preorder_traverse(node.right)

	def midorder_traverse(self,node):
		if node is None:
			return
		self.midorder_traverse(node.left)
		print(node.value,end=' ')
		self.midorder_traverse(node.right)

	def reConstructBinaryTree(self,pre,tin):
		if len(pre) == 0:
			return None
		if len(pre) == 1:
			return TreeNode(pre[0])
		else:
			res = TreeNode(pre[0])
			res.left = self.reConstructBinaryTree(pre[1: tin.index(pre[0]) + 1], tin[: tin.index(pre[0])])
			res.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:],tin[tin.index(pre[0]) + 1 :])
		return res
if __name__ == '__main__':
	#创建结点
	a1 = TreeNode(1)
	a2 = TreeNode(2)
	a3 = TreeNode(3)
	a4 = TreeNode(4)
	a5 = TreeNode(5)
	a6 = TreeNode(6)
	a7 = TreeNode(7)
	a8 = TreeNode(8)
    # 形成二叉树
	a1.left = a2
	a2.left = a4
	a4.left = a7
	a1.right = a3
	a3.left = a5
	a3.right = a6
	a6.left = a8

	s = Solutuon()
	s.preorder_traverse(a1)
	s.midorder_traverse(a1)

