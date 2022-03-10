import numpy as np
import pandas as pd

class stat:

    def exp_drop(file_ex, thr_val):
        """Function to drop columns with values below set threshold."""
        f_col =  file_ex.columns[file_ex.var()< thr_val ]
        file_drp = file_ex.drop(f_col, axis=1)

        return file_drp