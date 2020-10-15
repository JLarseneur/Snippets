from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([("scale", StandardScaler()),
                 ("reduce_dims", PCA()),
                 ("ridge", Ridge())
                ])


param_grid = dict(reduce_dims__n_components = [0.5, 0.75, 0.95],
                  ridge__alpha = np.logspace(-5, 5, 10),
                  ridge__fit_intercept = [True, False],
                 )

grid = GridSearchCV(pipe, param_grid=param_grid, cv=10)
grid.fit(X, y)
