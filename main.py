# Data framing library
import pandas as pd
import numpy as np

# Machine Learning library
import torch 

# Query to select articles from database that have the keyword
# SELECT * FROM articles WHERE content LIKE 'keyword', %s