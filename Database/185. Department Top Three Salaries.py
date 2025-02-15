import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby('departmentId')['salary'].rank(method = 'dense', ascending = False)
    employee_filtered = employee.query("rank <= 3").sort_values(by = 'salary')[['departmentId', 'name', 'salary']]
    df_result = employee_filtered.merge(department, how = 'inner', left_on = 'departmentId', right_on = 'id')
    df_result = df_result[['name_y', 'name_x', 'salary']].rename(columns = {'name_y': "Department", 'name_x': 'Employee', 'salary':'Salary'})
    return df_result
