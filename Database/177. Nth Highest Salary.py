import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending = False, ignore_index = True)
    if N <= 0 or len(sorted_salaries) < N:
        result_df = pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        nth_highest = sorted_salaries.iloc[N-1]
        result_df = pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})
    return result_df
