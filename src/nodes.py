
import platform
import shutil

import network

# NETWORKED DEVICE
class Node:
	def __init__(self):
		self.uname = platform.uname()._asdict()


class WindowsNode(Node):
	def __init__(self):
		self.desktop = "C:\\Users\\SPS\\Desktop"

	def copy_desktop(self, exe_name):
		shutil.copy(self.desktop, network.exe_dict)
