from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from openpyxl import load_workbook
import pandas as pd
from . import surcalc



# Create your views here.
def download_view(request, chart_type):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            # print(data)
            filename = request.user.username
            user = request.user
            if chart_type == 'survival':
                chartdata = surcalc.dataStructure(data, filename, user)
                return render(request, 'chart.html', chartdata)
            elif chart_type == 'control':
                chartdata = surcalc.dataStructure(data, filename, user)
                return render(request, 'chart.html', chartdata)
    else:
        form = UploadFileForm()

    return render(request, 'dl.html', {'form': form})
