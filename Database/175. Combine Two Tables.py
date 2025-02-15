import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    pd_merged = pd.merge(person, address, how = 'left', on = 'personId')
    df_result = pd_merged[['firstName', 'lastName', 'city', 'state']]
    return df_result
    
