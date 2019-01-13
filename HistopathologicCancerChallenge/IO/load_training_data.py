import cv2
from glob import glob 
import numpy as np
from tqdm import tqdm_notebook,trange
import pandas as pd
import os

def load_training_data(train_path = '../Data/train/',shuffle = True):
    """Reads the training data from the data folder
        train_path (str, optional): Defaults to '../data/train/'. Location of the training images
        shuffle (bool, optional): Defaults to True. Shuffle data after
    
    Returns:
        Numpy arrays: Training images (N,H,W,C) and the corresponding labels (N)
    """

    #Read the provided csv file and image filenames
    df = pd.DataFrame({'path': glob(os.path.join(train_path,'*.tif'))})
    if os.name == 'nt': #deal with windows backslashes
        df['id'] = df.path.map(lambda x: x.split('\\')[1].split(".")[0])
    else:
        df['id'] = df.path.map(lambda x: x.split('/')[3].split(".")[0])
    labels = pd.read_csv("../Data/train_labels.csv")
    df = df.merge(labels, on = "id")

    #Allocate numpy arrays for images and labels
    N = df["path"].size
    X = np.zeros([N,96,96,3],dtype=np.uint8)
    y = np.squeeze(df.as_matrix(columns=['label']))

    #Load the images
    for i, row in tqdm_notebook(df.iterrows(), total=df.shape[0]):
        X[i] = cv2.imread(row['path'])

    #Shuffle the data in case there was some sorting done
    if shuffle:
        idx = np.arange(y.shape[0])
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

    return X,y