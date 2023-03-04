from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from openpyxl import load_workbook

# Create your views here.
def download_view(request):
    # if not request.user.is_authenticated:
    #     context = {'message': 'Please login to receive an access to dashboards',}
    #     return render(request, 'login.html', context)
    # else:
    #     return render(request, 'dl.html')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            wb = load_workbook(filename=request.FILES['file'])
            sheet_ranges = wb['Sheet1']
            print(sheet_ranges['A2'].value)
            # print(request.FILES['file'].read())
            # form.save()
            return redirect('index')
    else:
        form = UploadFileForm()

    return render(request, 'dl.html', {'form': form})
