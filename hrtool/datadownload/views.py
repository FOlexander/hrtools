from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from openpyxl import load_workbook
import pandas as pd
from . import surcalc


# Create your views here.
def download_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            surcalc.dataStructure(data)#оновлюэмо файл
            # print(data)
            return redirect('index')
    else:
        form = UploadFileForm()

    return render(request, 'dl.html', {'form': form})
