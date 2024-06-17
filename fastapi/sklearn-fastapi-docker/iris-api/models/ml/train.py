from joblib import dump
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier

print("Data Loading ...")
iris = datasets.load_iris(return_X_y=True)
X = iris[0]
y = iris[1]


print("Creating simple model ...")
clf_pipeline = [('scaling', MinMaxScaler()), 
                ('clf', DecisionTreeClassifier(random_state=42))]
pipeline = Pipeline(clf_pipeline)

pipeline.fit(X, y)


print("Saving model ...")
dump(pipeline, './iris_dt_v1.joblib')