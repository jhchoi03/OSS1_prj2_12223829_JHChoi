import pandas as pd
from pandas import Series, DataFrame
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.pipeline import Pipeline, make_pipeline
import numpy as np


def sort_dataset(dataset_df):
	return dataset_df.sort_values(by='year', ascending=True)

def split_dataset(dataset_df):
    dataset_df['salary'] = dataset_df['salary'] / 1000

    train_df = dataset_df.iloc[:1718]
    test_df = dataset_df.iloc[1718:]

    return train_df.drop(['salary'], axis=1), test_df.drop(['salary'], axis=1), train_df['salary'], test_df['salary']

def extract_numerical_cols(dataset_df):
	return dataset_df[['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']]

#
def train_predict_decision_tree(X_train, Y_train, X_test):
    rf_cls = DecisionTreeRegressor()
    rf_cls.fit(X_train, Y_train)
    return rf_cls.predict(X_test)
#
def train_predict_random_forest(X_train, Y_train, X_test):
    rf_cls = RandomForestRegressor()
    rf_cls.fit(X_train, Y_train)
    return rf_cls.predict(X_test)
#
def train_predict_svm(X_train, Y_train, X_test):
    rf_cls = make_pipeline(StandardScaler(), SVR())
    rf_cls.fit(X_train, Y_train)
    return rf_cls.predict(X_test)

def calculate_RMSE(labels, predictions):
    return np.sqrt(np.mean((predictions-labels)**2))



if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
    data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

    sorted_df = sort_dataset(data_df)
    X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

    X_train = extract_numerical_cols(X_train)
    X_test = extract_numerical_cols(X_test)

    dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
    rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
    svm_predictions = train_predict_svm(X_train, Y_train, X_test)

    print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
    print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
    print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))