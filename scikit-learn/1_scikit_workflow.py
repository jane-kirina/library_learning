'''Problem Definition:
Predict whether or not patient have heart disease

Evaluation:
Reach 95% accuracy at predicting whether or not patient have heart disease

Features

Create data dictionary
age - in years
sex
    1: male;
    0: female
cp - chest pain type
    0: Typical angina: chest pain related decrease blood supply to the heart
    1: Atypical angina: chest pain not related to heart
    2: Non-anginal pain: typically esophageal spasms (non heart related)
    3: Asymptomatic: chest pain not showing signs of disease
trestbps - Resting Blood Pressure (in mmHg on admission to the hospital) anything above 130-140 is typically cause for concern
chol - Serum Cholestrol in mg/dl
    serum = LDL + HDL + .2 * triglycerides
    above 200 is cause for concern
fbs - Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)
    '>126' mg/dL signals diabetes
restecg - resting electrocardiographic results
    0: Nothing to note
    1: ST-T Wave abnormality
    can range from mild symptoms to severe problems
    signals non-normal heart beat
    2: Possible or definite left ventricular hypertrophy
    Enlarged heart's main pumping chamber
thalach - maximum heart rate achieved
exang - exercise induced angina
    1: yes
    0: no
oldpeak - ST depression induced by exercise relative to rest looks at stress of heart during excercise unhealthy heart will stress more
slope - the slope of the peak exercise ST segment
    0: Upsloping, better heart rate with excercise (uncommon)
    1: Flatsloping, minimal change (typical healthy heart)
    2: Downslopins, signs of unhealthy heart
ca - number of major vessels (0-3) colored by flourosopy
colored vessel means the doctor can see the blood passing through
the more blood movement the better (no clots)
thal - thalium stress result
    1,3: normal
    6: fixed defect: used to be defect but ok now
    7: reversable defect: no proper blood movement when excercising
target - have disease or not (1=yes, 0=no) (= the predicted attribute)
'''

'''1 - Get the data ready'''
# EDA and plotting libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scikit-Learn
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Model Evaluations
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
#Before sklearn 1.2: from sklearn.metrics import plot_roc_curve
from sklearn.metrics import RocCurveDisplay

np.random.seed(42)
heart_disease = pd.read_csv('heart-disease.csv')

# feature matrix
x = heart_disease.drop('target', axis=1)
# labels
y = heart_disease['target']
# test data
n_estimators = 100


''' 2 - Choose the right algorithm'''

clf = RandomForestClassifier(n_estimators=n_estimators)

# get default hyperparameters
clf.get_params()

'''# 3 - Fit the model'''

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

clf.fit(x_train, y_train)

# make a prediction
y_predictions = clf.predict(X=x_test)

'''# 4 - Evaluating the model on train and test data'''
train_accuracy = clf.score(x_train, y_train)
print('Train score: ', train_accuracy)
test_accuracy = clf.score(x_test, y_test)
print('Test score: ', test_accuracy)

print('Classification report:')
print(classification_report(y_test, y_predictions))

print('Accuracy report:')
print(accuracy_score(y_test, y_predictions))

print('Confusion report:')
print(confusion_matrix(y_test, y_predictions))

'''# 5 - Improve a model'''
# Trying different amount of n_estimators
best_estimator = 0
best_percent = 0
for i in range(10, 100, 10):
    print(f'Trying model with {i} estimators')
    model = RandomForestClassifier(n_estimators=i).fit(x_train, y_train)
    percent = round(model.score(x_test, y_test) * 100, 2)
    if best_percent < percent:
        best_percent = percent
        best_estimator = i
    print(f"Model accuracy on test set: {percent}%")

print(f'The best accuracy is obtained by a model with {best_estimator} estimators.')
print(f'Model accuracy: {best_percent}%')

'''# 6 - Save and load a trained model'''

pickle.dump(clf, open('random_forest_model_1.pkl', 'wb'))
load_model = pickle.load(open('random_forest_model_1.pkl', 'rb'))
score = load_model.score(x_test, y_test)
print(score)

'''
 The end-to-end Scikit-learn workflow
1. Getting the data ready
2. Choose the right estimator/algorithm for our problems
3. Fit the model/algorithm and use it to make predictions on our data
4. Evaluating a model
5. Improve a model
6. Save and load a trained model
7. Putting it all together
'''
