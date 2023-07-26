from timeit import default_timer as timer
from sklearn import metrics
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

from codecarbon import EmissionsTracker
import time
print('Loading The dataset')
x, y = fetch_openml(name='a9a', return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearnex import patch_sklearn
patch_sklearn()

from sklearn.svm import SVC

params = {
    'C': 100.0,
    'kernel': 'rbf',
    'gamma': 'scale'
}
tracker = EmissionsTracker(project_name="Intel_pacthed_sklearn")
tracker.start()
start = timer()
classifier = SVC(**params).fit(x_train, y_train)
train_patched = timer() - start
print('Training time for Intel patched sklearn is ',train_patched)
emissions = tracker.stop()
print(f"Emissions : {emissions} kg CO2")

predicted = classifier.predict(x_test)
report = metrics.classification_report(y_test, predicted)
print(f"Classification report for IntelÂ® extension for Scikit-learn SVC:\n{report}\n")

print('Cooling period for unpatching is 10 sec',time.sleep(10))


from sklearnex import unpatch_sklearn
unpatch_sklearn()


from sklearn.svm import SVC
tracker = EmissionsTracker(project_name="Intel_unpacthed_sklearn")
tracker.start()
start = timer()
classifier = SVC(**params).fit(x_train, y_train)
train_unpatched = timer() - start
print('Training time for unpatched sklearn is ',train_unpatched)

emissions = tracker.stop()
print(f"Emissions : {emissions} kg CO2")


predicted = classifier.predict(x_test)
report = metrics.classification_report(y_test, predicted)

print(f"Classification report for original Scikit-learn SVC:\n{report}\n")






