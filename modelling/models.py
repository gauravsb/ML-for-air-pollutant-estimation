import numpy as np
import os
import json
import math
import csv
import collections
from collections import defaultdict
import nltk
import pandas as pd
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

if __name__ == "__main__":

    df = pd.read_csv('HKLURDataset.csv')
    print(df['Long'])

