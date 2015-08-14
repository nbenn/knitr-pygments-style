""" 
A knitr style for Pygments
""" 
from setuptools import setup 

setup( 
    name         = 'knitr', 
    version      = '1.2', 
    description  = __doc__, 
    author       = "Nicolas Bennett", 
    install_requires = ['pygments'],
    packages     = ['knitr'], 
    entry_points = '''
    [pygments.styles]
    knitr = knitr:KnitrStyle
    '''
) 
