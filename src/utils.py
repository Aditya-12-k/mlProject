import os
import sys
import pandas as pd
import numpy as np
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score

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
# def evaluate_models(X_train,y_train,X_test,y_test,models):
#     try:
#         report = {}
        
#         for i in range(len(list(models))):
#             model = list(modle.values())[i]
#             model.fit(X_train,y_train)
#             y_train_pred = model.predict(X_train)
#             y_test_pred = model.predict(X_test)
#             train_model_score = r2_score(y_train,y_train_pred)
#             report[list(model.keys)[i]] = test_model_score
#         return report 
#     except Exception as e:
#         raise CustomException(e,sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for model_name, model in models.items():
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
