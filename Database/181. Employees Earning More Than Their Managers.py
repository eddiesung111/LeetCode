import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df_merged = employee.merge(employee, how = 'inner', left_on = 'managerId', right_on = 'id')
    result_df = pd.DataFrame({'Employee': df_merged.query("salary_x > salary_y")['name_x']})
    return result_df

def find_employees2(employee: pd.DataFrame) -> pd.DataFrame:
    df_merged = employee.merge(employee, how = 'inner', left_on = 'managerId', right_on = 'id')
    df_filtered = df_merged.query("salary_x > salary_y")
    result_df = df_filtered.loc[:, ["name_x"]].rename(columns = {'name_x': 'Employee'})
    return result_df
