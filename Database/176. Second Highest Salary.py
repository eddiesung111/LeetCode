import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False, ignore_index = True)
    if len(distinct_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        second_highest = distinct_salaries.iloc[1]
        return pd.DataFrame({'SecondHighestSalary': [second_highest]})

def second_highest_salary2(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    second_highest = unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None
    if second_highest == None:
        result_df = pd.DataFrame({'SecondHighestSalary': [None] })
    else:
        result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})
    return result_df
