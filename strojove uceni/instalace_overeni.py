
# INSTALUJ v prikazove radce 
"""
pip3 install numpy
pip3 install pandas
pip3 install sklearn
pip3 install matplotlib
pip3 install seaborn
pip3 install notebook
"""

# TESTUJ 
# NumPy 
try:
    import numpy as np 
    print('Numpy verze: {}'.format(np.__version__)) 
except:
    print('Numpy knihovna  nelze nacist!')
    print('Instaluj napr.: pip3 install numpy ')
    print('nebo s vyuzitim conda')
    
# Pandas
try:
    import pandas as pd 
    print('Pandas verze: {}'.format(pd.__version__)) 
except:
    print('Pandas knihovna  nelze nacist!')
    print('Instaluj napr.: pip3 install pandas')

# Sklearn 
try:
    import sklearn  
    print('Sklearn verze: {}'.format(sklearn.show_versions()))
except:
    print('Sklearn knihovna nelze nacist!')
    print('Instaluj napr.: pip3 install sklearn')

# Matplolib 
try:
    import matplotlib 
    # %matplotlib inline 
    print('Matplotlib verze: {}'.format(matplotlib.__version__)) 
except:
    print('Matplotlib knihovna nelze nacist!')
    print('Instaluj napr.: pip3 install matplotlib')

# Seaborn 
try:
    import seaborn as sns 
    print('Seaborn verze: {}'.format(sns.__version__)) 
except:
    print('Seaborn knihovna nelze nacist!')
    print('Instaluj napr.: pip3 install seaborn')

