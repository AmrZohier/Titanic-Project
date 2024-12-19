# DataSet
# c:\Users\farou\Downloads\train.csv c:\Users\farou\Downloads\eval.csv
# c:\Users\farou\Downloads\train.csv c:\Users\farou\Downloads\train.csv

# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Load Data
train = pd.read_csv("C:\Amr\Titanic\\train.csv")
eval = pd.read_csv("C:\Amr\Titanic\eval.csv")

# Data Exploration
print(train.head())