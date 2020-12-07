# load pandas for data analysis
import pandas as pd
import numpy as np

from utils import display_scores

features = ['LATITUDE', 'LONGITUDE', 'DAY_OF_MONTH', 'HOUR']

# establish data for classification
X = parking_violations[features]
y = parking_violations['DISPOSITION_RESULT']

from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =\
    train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression(penalty='none', random_state=42)
log_reg.fit(X_train, y_train)

print('Score - Training: {:f}'.format(log_reg.score(X_train, y_train)))
print('Score - Test: {:f}'.format(log_reg.score(X_test, y_test)))

from sklearn.linear_model import PassiveAggressiveClassifier

passive_aggressive_clf = PassiveAggressiveClassifier(random_state=42)
passive_aggressive_clf.fit(X_train, y_train)

print('Score - Training: {:f}'.format(passive_aggressive_clf.score(
    X_train, y_train)))
print('Score - Test: {:f}'.format(passive_aggressive_clf.score(
    X_test, y_test)))

from sklearn.tree import DecisionTreeClassifier

tree_clf = DecisionTreeClassifier(random_state=42)
tree_clf.fit(X_train, y_train)

print('Score - Training: {:f}'.format(tree_clf.score(X_train, y_train)))
print('Score - Test: {:f}'.format(tree_clf.score(X_test, y_test)))

from sklearn.linear_model import RidgeClassifier

ridge_clf = RidgeClassifier().fit(X_train, y_train)

print('Score - Training: {:f}'.format(ridge_clf.score(X_train, y_train)))
print('Score - Test: {:f}'.format(ridge_clf.score(X_test, y_test)))

from sklearn.ensemble import RandomForestClassifier

forest_clf = RandomForestClassifier(random_state=42)
forest_clf.fit(X_test, y_test)

print('Score - Training: {:f}'.format(forest_clf.score(X_train, y_train)))
print('Score - Test: {:f}'.format(forest_clf.score(X_test, y_test)))

from sklearn.ensemble import AdaBoostClassifier

ada_clf = AdaBoostClassifier(random_state=42)
ada_clf.fit(X_test, y_test)

print('Score - Training: {:f}'.format(ada_clf.score(X_train, y_train)))
print('Score - Test: {:f}'.format(ada_clf.score(X_test, y_test)))

from sklearn.neural_network import MLPClassifier

mlp_clf = MLPClassifier(random_state=42)
mlp_clf.fit(X_test, y_test)

print('Score - Training: {:f}'.format(mlp_clf.score(X_train, y_train)))
print('Score - Test: {:f}'.format(mlp_clf.score(X_test, y_test)))


from sklearn.model_selection import cross_val_score

log_reg_scores = cross_val_score(log_reg, X, y,
                                 scoring="neg_mean_squared_error", cv=10)
log_reg_rmse_scores = np.sqrt(-log_reg_scores)
display_scores('Logistic Regression', log_reg_rmse_scores)

passive_aggressive_clf_scores =\
    cross_val_score(passive_aggressive_clf, X, y, cv=10,
                    scoring="neg_mean_squared_error")
passive_aggressive_clf_rmse_scores = np.sqrt(-passive_aggressive_clf_scores)
display_scores('Passive Aggressive', passive_aggressive_clf_rmse_scores)

tree_clf_scores = cross_val_score(tree_clf, X, y,
                                  scoring="neg_mean_squared_error", cv=10)
tree_clf_rmse_scores = np.sqrt(-tree_clf_scores)
display_scores('Decision Tree', tree_clf_rmse_scores)

ridge_clf_scores = cross_val_score(ridge_clf, X, y,
                                   scoring="neg_mean_squared_error", cv=10)
ridge_clf_rmse_scores = np.sqrt(-ridge_clf_scores)
display_scores('Ridge', ridge_clf_rmse_scores)

forest_clf_scores = cross_val_score(forest_clf, X, y,
                                    scoring="neg_mean_squared_error", cv=10)
forest_clf_rmse_scores = np.sqrt(-forest_clf_scores)
display_scores('Forest', forest_clf_rmse_scores)

ada_clf_scores = cross_val_score(ada_clf, X, y,
                                 scoring="neg_mean_squared_error", cv=10)
ada_clf_rmse_scores = np.sqrt(-ada_clf_scores)
display_scores('AdaBoost', ada_clf_rmse_scores)

mlp_clf_scores = cross_val_score(mlp_clf, X, y,
                                 scoring="neg_mean_squared_error", cv=10)
mpl_clf_rmse_scores = np.sqrt(-mlp_clf_scores)
display_scores('MLP', mpl_clf_rmse_scores)


from sklearn.model_selection import GridSearchCV

param_grid = {'C': np.logspace(-3, 3, 7),
              'penalty': ['l1', 'l2', 'elasticnet', 'none'],
              'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']}

grid_search = GridSearchCV(LogisticRegression(),
                           param_grid, cv=5,
                           scoring='neg_mean_squared_error',
                           return_train_score=True)
grid_search.fit(X_train, y_train)

print('best parameters', grid_search.best_params_)
print('best score', grid_search.best_score_)

from sklearn.metrics import mean_squared_error

final_model = grid_search.best_estimator_

final_predictions = final_model.predict(X_test)

final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
print(final_rmse)