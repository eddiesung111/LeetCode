import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    notbanned_user_id = users[users["banned"] == "No"]["users_id"]
    filtered_trips = trips[('2013-10-01'<= trips['request_at']) &
                            (trips['request_at'] <= '2013-10-03') &
                           (trips['client_id'].isin(notbanned_user_id)) &
                           (trips['driver_id'].isin(notbanned_user_id))]

    filtered_trips = filtered_trips.groupby('request_at')\
    .agg(
        total_orders = ('status', 'count'), 
        cancelled_orders = ('status', lambda x: (x != 'completed').sum())
        ).reset_index()
    filtered_trips['Cancellation Rate'] = (filtered_trips['cancelled_orders'] / filtered_trips['total_orders']).round(2)
    result_df = filtered_trips[["request_at", "Cancellation Rate"]].rename(columns = {'request_at': 'Day'})
    return result_df
