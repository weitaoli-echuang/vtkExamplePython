__author__ = 'VDTConstructor'

import os
import sys


def vtk_env_set(vtk_home_dir):
	vtk_home_path = os.path.abspath(vtk_home_dir)
	vtk_path = list()
	vtk_path.append(os.path.join(vtk_home_path, 'bin'))
	vtk_path.append(os.path.join(vtk_path[0], 'Lib'))
	vtk_path.append(os.path.join(vtk_path[1], 'site-packages'))
	sys.path.extend(vtk_path)

	os.environ['PATH'] += ';'
	os.environ['PATH'] += ';'.join(vtk_path)


if __name__ == '__main__':
	vtk_home_dir = '''C:/Program Files (x86)/VTK 6.3.0'''
	vtk_env_set(vtk_home_dir)
