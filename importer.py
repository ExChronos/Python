#importer
import imp
import newImporter

error = False
alright = True
x = 10
reloading = imp.reload(newImporter)

__all__ = ['error', 'alright'] #импортируются только они с помощью from <module> import *
_X = ['x', 'reloading'] #нельзя импортировать с помощью from <module> import *
