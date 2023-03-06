import math
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines import NelsonAalenFitter
from lifelines.statistics import logrank_test

plt.switch_backend(
    'agg')  # https://stackoverflow.com/questions/52839758/matplotlib-and-runtimeerror-main-thread-is-not-in-main-loop


def dataStructure(data, filename):
    df = data
    filename = filename
    x = datetime.today()
    df['Event'] = 1
    df.loc[df['LastDay'].isna(), 'Event'] = 0
    df.loc[df['LastDay'].isna(), 'LastDay'] = x
    df['WorkTimeM'] = (df['LastDay'] - df['StartDay']).astype('timedelta64[D]') / (365.25 / 12)
    pd.to_numeric(df['WorkTimeM'])  # convert everything to float values
    if len(df.columns) == 4:
        print("KaplanMeier")
        return KaplanMeier(df, filename)
    elif len(df.columns) == 5:
        print("LogRank")
        # return LogRank(df)
    elif len(df.columns) > 5:
        pass
        print("Sorry you add to many parameters if you want to make such research please contact us")
    else:
        print("some mistake")
    print("Hi from dataStructure")


def KaplanMeier(df, filename):
    df = df

    print("Hi from KM")

    kmf = KaplanMeierFitter()

    kmf.fit(durations=df['WorkTimeM'], event_observed=df['Event'], label='Median Survival Time')

    a = [kmf.median_survival_time_]

    px = 1 / plt.rcParams['figure.dpi']
    kmf.plot(color="#2E9FDF", figsize=(854 * px, 480 * px), ci_show=False)
    chartname = f"{filename}"

    plt.grid(alpha=0.3)  # сетка и ее прозрачность
    plt.xlabel('Months')
    plt.ylabel('Survival')
    plt.title('Employee Median Survival Time')
    plt.legend()
    plt.ylim(0, 1)
    plt.xlim(0, max(df['WorkTimeM']))
    plt.axhline(y=0.5, xmin=0, xmax=a[0] / max(df['WorkTimeM']), color="#E7B800", ls="dotted", lw=1)
    plt.axvline(x=a, ymin=0, ymax=0.5, color="#E7B800", ls="dotted", lw=1)
    y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    plt.yticks(y)  # размер градации шкалы
    plt.savefig(chartname, dpi=150)
    plt.close()
    # plotadress = '/'.join(chartname.split('\\')[-2:])
    plotadress = f"media/{filename}"

    # print('plotadress', plotadress, '\\n', 'chartname', chartname)
    # p = Plot(title='Beatles Blog', plot=plotadress)
    # p.save()
    Hazard3m = (1 - kmf.survival_function_at_times(3.0).iloc[0]) * 100
    Hazard6m = (1 - kmf.survival_function_at_times(6.0).iloc[0]) * 100
    Hazard12m = (1 - kmf.survival_function_at_times(12.0).iloc[0]) * 100

    data = {
        "Name": "KMF",
        "Hazard3m": "{:.1f}".format(Hazard3m),
        "Hazard6m": "{:.1f}".format(Hazard6m),
        "Hazard12m": "{:.1f}".format(Hazard12m),
        "AvarageSurvival": math.ceil(a[0]),
        "chart": plotadress
        # "75Survival": kmf.percentile(p="0.25"),
        # "25Survival": kmf.percentile(p="0.75")
    }

    return data

    # возвращаем какой процент сотрудников увольняется в первіе 3,6,12 месяцев работы
    # print(1-kmf.survival_function_at_times(3.0).iloc[0])#коммулятивній риск увольнения в первіе 3 месяца
    # print(1 - kmf.survival_function_at_times(6.0))#коммулятивній риск увольнения в первіе 6 месяца
    # print(1 - kmf.survival_function_at_times(12.0))#коммулятивній риск увольнения в первіе 12 месяца
    # возвращаем процентили дожития сотрудников
    # print(kmf.percentile(p="0.5"))#средняя продолжительность жизни сотрудника в компании
    # print(kmf.percentile(p="0.25"))#3 квартиль продолжительность жизни сотрудника в компании
    # print(kmf.percentile(p="0.75"))#1 квартиль продолжительность жизни сотрудника в компании
