
# IMPORTS
import platform
import shutil
import os


# NETWORK
installers = "\\\\SPS-MTL-JUPITER\\sps-mtl-bank\\SPS Bank Installers"

exe_dict = {

	'CrossFTP': 		installers+r"\CrossFTP\Windows\crossftp-full-setup-1.99.9.exe",
	'CyberDuck': 		installers+r"\Cyberduck\Windows\Cyberduck-Installer-8.4.3.38269.exe",
	'FreeFileSync': 	installers+r"\FreeFileSync\Windows\FreeFileSync_11.29_Windows_Setup.exe",
	'HandBrake': 		None,
	'MountainDuck': 	installers+r"\MountainDuck\Windows\Mountain Duck Installer-4.12.2.20039.exe",
	'Maxon': 			None,
	'Notch': 			None,
	'Nvidia': 			installers+r"\Nvidia\Windows\527.56-desktop-win10-win11-64bit-international-nsd-dch-whql.exe",
	'Parsec': 			None,
	'Pulseway': 		None,
	'TouchDesigner':	None,
	'TeamViewer': 		installers+r"\TeamViewer\Windows\TeamViewer_Setup_x64.exe",
	'VLC': 				None,
}



# NETWORKED DEVICE
class Node:
	def __init__(self):
		self.uname = platform.uname()._asdict()


class WindowsNode(Node):
	def __init__(self):
		self.desktop = "C:\\Users\\SPS\\Desktop"

	def install_vlc(self):
		pass




class InstallCtxt:
	def __init__(self, node):
		self.node = node

	def __enter__(self):
		print('InstallCtxt -- ENTER')
		pass

	def __exit__(self, exc_type, exc_value, exc_tb):
		print('InstallCtxt -- EXIT')
		pass

me = Node()

with InstallCtxt(me):
	print(me.uname)





