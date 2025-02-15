import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person.duplicated('email') == True][['email']].drop_duplicates()
