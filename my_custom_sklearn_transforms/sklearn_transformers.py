from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()

        data["BOM_ALUNO"] = data["NOTA_MF"].apply(lambda x: 1 if  x > 8 else 0)
        data["PESSIMO_ALUNO"] = data["NOTA_MF"].apply(lambda x: 1 if  x < 3 else 0)
        data["MUITO_BOM_GUYS"] = data["NOTA_MF"].apply(lambda x: 1 if x >= 7 and x <= 12 else 0)

        data = data.dropna(inplace=False)
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
