#!/usr/bin/env python3
# 📚 Review With Students:
    # Introduction to Object Oriented programming, classes, instances, methods
import ipdb
# Importing the pet class 
from lib.pet import *
from lib.cat import *
from lib.decorator import *
# Instances of the pet classes
rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)
cookie = Pet('cookie', 1, 'Dachshund', 'hyper', 'cookie.jpg')
princess_grace = Pet('princess grace', 7, 'domestic longhair', 'affectionate', 'gracy.png')



ipdb.set_trace()