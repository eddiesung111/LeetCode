import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df_merged = employee.merge(department, how = "inner", left_on = "departmentId", right_on = "id", suffixes = ('_employee', '_department'))
    df_highest_salary = df_merged.groupby('departmentId').apply(lambda x: x[x.salary == x.salary.max()])
    df_result = df_highest_salary[['name_department', 'name_employee', 'salary']]
    df_result.columns = ['Department', 'Employee', 'Salary']
    return df_result
