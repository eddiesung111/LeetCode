import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs[(logs.num == logs.num.shift(1)) &
                (logs.num == logs.num.shift(2)) &
                (logs.id == logs.id.shift(1) + 1) &
                (logs.id == logs.id.shift(2) + 2)].drop_duplicates('num')
    result_df = logs.loc[:, ['num']].rename(columns = {'num' : 'ConsecutiveNums'})
    return result_df


def consecutive_numbers2(logs: pd.DataFrame) -> pd.DataFrame:
    logs['var'] = logs.num.rolling(window = 3).var()
    result_df = pd.DataFrame({'ConsecutiveNums': logs.query('var == 0').num.unique()})
    return result_df
