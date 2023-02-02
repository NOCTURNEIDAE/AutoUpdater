
import argparse

import nodes


class InstallCtxt:
	def __init__(self, node):
		self.node = node

	def __enter__(self):
		print('InstallCtxt -- ENTER')
		pass

	def __exit__(self, exc_type, exc_value, exc_tb):
		print('InstallCtxt -- EXIT')
		pass


with InstallCtxt(nodes.WindowsNode()):
	print(me.uname)





