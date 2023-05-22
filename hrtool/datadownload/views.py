from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
import secrets
import pandas as pd
from . import surcalc, contcalc


# Create your views here.
@login_required
def download_view(request, chart_type):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.POST.get('name'))
        if form.is_valid():
            print(chart_type)
            file = request.FILES['file']
            try:
                data = pd.read_excel(file)
            except ValueError:
                return render(request, 'dl.html', {'error': 'Unsupported format of document please use .xls or .xlsx'})
            print(data)
            random_string = secrets.token_hex(4)
            filename = f'{request.user.username}_{random_string}'
            user = request.user
            if chart_type == 'survival':
                chartdata = surcalc.dataStructure(data, filename, user)
                return render(request, 'chart_surv.html', chartdata)
            elif chart_type == 'control':
                columname = data.columns[0]
                chartdata = contcalc.read_file(data, filename, user, columname)
                return render(request, 'chart_surv.html', chartdata)
        else:
            print(form.errors)
    else:
        form = UploadFileForm()

    return render(request, 'dl.html', {'form': form, 'type_c':chart_type})
