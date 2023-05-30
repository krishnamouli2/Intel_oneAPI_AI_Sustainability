from codecarbon import EmissionsTracker

from timeit import default_timer as timer
from sklearn import metrics
import time

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

print('Loading The dataset')
x, y = fetch_openml(name='Yolanda', return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=72)
x_train.shape, x_test.shape, y_train.shape, y_test.shape


from sklearnex import patch_sklearn
patch_sklearn()

from sklearn.ensemble import RandomForestRegressor

params = {
    'n_estimators': 150,
    'random_state': 44,
    'n_jobs': -1
}
tracker = EmissionsTracker(project_name="Intel_pacthed_sklearn")
tracker.start()
start = timer()
rf = RandomForestRegressor(**params).fit(x_train, y_train)
train_patched = timer() - start
print('Training time for Intel patched sklearn is ',train_patched)
emissions = tracker.stop()
print(f"Emissions : {emissions} kg CO2")

y_pred = rf.predict(x_test)
mse_opt = metrics.mean_squared_error(y_test, y_pred)
print('The error for the Model in Intel patched sklearn is', mse_opt)


print('Cooling period for unpatching is 10 sec',time.sleep(10))
from codecarbon import EmissionsTracker

from sklearnex import unpatch_sklearn
unpatch_sklearn()


from sklearn.ensemble import RandomForestRegressor

tracker = EmissionsTracker(project_name="Intel_unpacthed_sklearn")
tracker.start()
start = timer()
rf = RandomForestRegressor(**params).fit(x_train, y_train)
train_unpatched = timer() - start
print('Training time for unpatched sklearn is ',train_unpatched)

emissions = tracker.stop()
print(f"Emissions : {emissions} kg CO2")

y_pred = rf.predict(x_test)
mse_original = metrics.mean_squared_error(y_test, y_pred)
print('The error for the Model in unpatched sklearn is', mse_original)




