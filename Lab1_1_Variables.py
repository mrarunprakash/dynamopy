# Copyright 2017 Autodesk, Inc. All rights reserved.
"""Variables.
"""

__author__ = 'Paolo Emilio Serra - paolo.serra@autodesk.com'
__copyright__ = 'Autodesk 2017'
__version__ = '1.0.0'

# Import modules and namespaces to add references to the code
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import MessageBox


# Unmutable objects
x = 1  # 'Hello'
y = x
MessageBox.Show('Unmutuable Objects - Step 1\nx: {0}\ny: {1}'.format(x, y))

y += 10 # ' World!'
# What is the value of x?
MessageBox.Show('Unmutuable Objects - Step 2\nx: {0}\ny: {1}'.format(x, y))


# Mutable objects
x = []
y = x
MessageBox.Show('Mutuable Objects - Step 3\nx: {0}\ny: {1}'.format(x, y))

y.append(3)
# What is the value of x?
MessageBox.Show('Mutuable Objects - Step 4\nx: {0}\ny: {1}'.format(x, y))
