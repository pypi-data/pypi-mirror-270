from joblib import load as loadModel
from joblib import dump as saveModel
from .datasets import loadDataset, subsetData
from sklearn.metrics import accuracy_score as accuracyScore

__version__ = '0.2.6'