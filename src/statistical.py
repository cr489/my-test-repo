from crypt import methods
import numpy as np
import pandas as pd


class stat:
    def __init__(self,file_ex,thr_val) -> None:
        self.file = file_ex
        self.thrv = thr_val

    def exp_drop(self):
        """Function to drop columns with values below set threshold."""
        f_col = self.file.columns[self.file.var() < self.thrv]
        self.file = self.file.drop(f_col, axis=1)
        return self.file

    def corr_fc(self.file):
        """Function to calculate correlation in data file using Pearson's method."""
        corr1 = self.file.corr(method="pearson")
        corr2 = corr1.drop(index="time", columns="time") 
        up_tri = corr2.where(np.triu(np.ones(corr2.shape), k=1).astype(bool))
        up_tri2 = up_tri.drop("MO3", axis=1)
        stack = up_tri2.unstack()  # unstacks up_tri2 matrix
        ab_vals = stack[abs(stack) >= 0.9]
        return ab_vals

    def eclud(self.file):
        """Function to calculate Euclidean distance for vectors."""
        self.file = self.file.fillna(0)   # Replace NaN with zeros
        
        file1 = np.zeros((self.file.shape[1], len(self.file[1]))) #Reading it numpy array
        for i in range(self.file.shape[1]):
            file1[i] = self.file[i].values
        
        return file1



