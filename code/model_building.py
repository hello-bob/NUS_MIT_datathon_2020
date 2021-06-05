from tpot import TPOTClassifier, TPOTRegressor
from pygam import LinearGAM, s, f

import os
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTENC
from joblib import Parallel, delayed
from kmodes.kmodes import KModes
from kmodes.kprototypes import KPrototypes
from sklearn.compose import ColumnTransformer
from sklearn import preprocessing, metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import tree
from sklearn.utils import class_weight
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import graphviz
from sklearn.tree import export_graphviz
from sklearn.linear_model import LogisticRegression
from catboost import CatBoostClassifier
import lightgbm as lgb

import statsmodels.api as sm
import statsmodels.formula.api as smf

metrics.macro

SEED=42
np.random.seed(SEED)
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y,
                                                    train_size=0.75, test_size=0.25)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=SEED, scoring=f1_macro)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))

tpot.fitted_pipeline_

print(tpot.score(X_test, y_test))


""" GAM """



gam = LinearGAM(s(0) + s(1) + f(2)).fit(X, y)