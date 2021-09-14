## Inject multiple arguments behind a single parameter
(lambda dataframe, col: (dataframe.count(), len(col)))(*(lambda dataframe: (dataframe, dataframe.columns))(df))
