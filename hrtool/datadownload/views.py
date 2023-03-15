from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from openpyxl import load_workbook
import secrets
import pandas as pd
from . import surcalc, contcalc
from .models import PlotFile



# Create your views here.
@login_required
def download_view(request, chart_type):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            # print(data)
            random_string = secrets.token_hex(4)
            filename = f'{request.user.username}_{random_string}'
            user = request.user
            if chart_type == 'survival':
                chartdata = surcalc.dataStructure(data, filename, user)
                return render(request, 'chart.html', chartdata)
            elif chart_type == 'control':
                columname = data.columns[0]
                chartdata = contcalc.read_file(data, filename, user, columname)
                print('Hi from view', chartdata)
                return render(request, 'chart.html', chartdata)
    else:
        form = UploadFileForm()

    return render(request, 'dl.html', {'form': form})
