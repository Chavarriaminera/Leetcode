import pandas as pd
def selectFirstRows(employees):
    df=pd.DataFrame(employees.head(3))
    return df