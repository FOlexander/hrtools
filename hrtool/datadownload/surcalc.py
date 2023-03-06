import pandas as pd
from datetime import datetime, timedelta


def dataStructure(data):
    df = data
    x = datetime.today()
    df['Event'] = 1
    df.loc[df['LastDay'].isna(), 'Event'] = 0
    df.loc[df['LastDay'].isna(), 'LastDay'] = x
    df['WorkTimeM'] = (df['LastDay'] - df['StartDay']).astype('timedelta64[D]') / (365.25 / 12)
    pd.to_numeric(df['WorkTimeM'])  # convert everything to float values
    if len(df.columns) == 4:
        print("KaplanMeier")
        # return KaplanMeier(df, filename)
    elif len(df.columns) == 5:
        print("LogRank")
        # return LogRank(df, filename)
    elif len(df.columns) > 5:
        pass
        print("Sorry you add to many parameters if you want to make such research please contact us")
    else:
        print("some mistake")
    print("Hi from dataStructure")
