import os
import sys
import pandas as pd
import numpy as np
import dill
from src.exception import CustomException

def save_object(file_path, obj):
    """
    Saves any Python object (model, preprocessor, pipeline, etc) using dill.
    """
    try:
        # Create directory if not exists
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Dump object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Loads Python object saved using dill.
    Very useful for prediction during deployment.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
