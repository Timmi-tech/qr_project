from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import QRCode

def scan_code(request):
    return render(request, 'scan_code.html')

def admit_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', None)
        if code:
            qr_code, created = QRCode.objects.get_or_create(code=code)
            if created:
                return JsonResponse({'message': f'Code {code} has been admitted.'})
            else:
                return JsonResponse({'message': f'Code {code} has already been admitted.'})
    return JsonResponse({'message': 'Invalid request'}, status=400)
