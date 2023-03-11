import csv
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import controlchart

from .models import PlotFile


def read_file(data, filename, user, columname):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(data[columname])
    counted_c = Counter(df['date'].dt.month)
    x = sorted(dict(counted_c, ).items())
    build_plot(x, filename, user)


def build_plot(x, filename, user):
    count_month = []
    for i in x:
        count_month.append(i[1])
    s = controlchart.Spc(count_month, controlchart.CHART_X_MR_X)
    b = s.get_chart(title='Control Chart')

    plotadress = f"{filename}.png"
    b.get_figure().savefig(plotadress)
    p = PlotFile(plot=plotadress, plot_user=user)
    p.save()

    data = {
        "chart": plotadress
    }

    return data


if __name__ == "__main__":
    read_file(df, filename, user)