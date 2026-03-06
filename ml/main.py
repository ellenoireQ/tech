# ------------
# Unit Testing
# ------------

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ml.utils.load_data import load_data

# load_data()
# utils/load_data.py
d = load_data()
print(d)  # returning all sales_data (in load_data() function returning 50)
