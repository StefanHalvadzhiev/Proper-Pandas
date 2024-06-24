import pandas as pd
import pytz

import config


def localize_and_convert_apply(df: pd.DataFrame) -> pd.DataFrame:
    zone = pytz.timezone('Europe/Sofia')
    
    def localize_and_convert(column):
        # Check if the column is already timezone-aware
        if column.dt.tz is None:
            # Localize the naive datetime to the given timezone
            column = column.dt.tz_localize(zone)
        # Convert to UTC
        return column.dt.tz_convert(pytz.utc)
    
    columns_to_convert = ['reference_date', 'delivery_begin', 'delivery_end', 'created_at']
    
    for column in columns_to_convert:
        df[column] = pd.to_datetime(df[column], format=config.DATETIME_FORMAT)
    
    df[columns_to_convert] = df[columns_to_convert].apply(localize_and_convert)
    
    return df


def localize_and_convert_loop(df: pd.DataFrame) -> pd.DataFrame:
    zone = pytz.timezone('Europe/Sofia')
    
    columns_to_convert = ['reference_date', 'delivery_begin', 'delivery_end', 'created_at']

    for column in columns_to_convert:
        df[column] = pd.to_datetime(df[column], format=config.DATETIME_FORMAT)
    
    for col in columns_to_convert:
        if df[col].dt.tz is None:
            df[col] = df[col].dt.tz_localize(zone)
        df[col] = df[col].dt.tz_convert(pytz.utc)
    
    return df
