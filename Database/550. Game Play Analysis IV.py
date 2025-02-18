import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first"] = activity.groupby("player_id").event_date.transform(min)
    activity_sec_day = activity.loc[activity["first"] + pd.DateOffset(1) == activity["event_date"]]
    return pd.DataFrame({"fraction": [round(len(activity_sec_day)/activity.player_id.nunique(), 2)]}) 

def gameplay_analysis2(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(['player_id', 'event_date'])
    first_login = activity.groupby(by = 'player_id')[['event_date']].min().reset_index()
    first_login.rename(columns = {'event_date': 'first_login_date'}, inplace = True)

    activity = activity.merge(first_login, on = 'player_id', how = 'inner')

    activity["is_next_day"] = ((activity['event_date'] - activity['first_login_date']).dt.days == 1)
    players_next_day_login = activity.groupby('player_id')['is_next_day'].max()
    fraction = round(sum(players_next_day_login)/len(players_next_day_login), 2)
    df_result = pd.DataFrame({'fraction': [fraction]})
    return df_result
