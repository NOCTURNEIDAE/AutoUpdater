
import platform

# NETWORKED DEVICE
class Node:
	def __init__(self):
		self.uname = platform.uname()._asdict()


class WindowsNode(Node):
	def __init__(self):
		self.desktop = "C:\\Users\\SPS\\Desktop"

	def install_vlc(self):
		pass

	def update_handbrake(self):
		pass

