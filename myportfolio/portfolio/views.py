from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, ContactMessage, Certificate
from .forms import ContactForm

def index(request):
    projects = Project.objects.all().order_by('-created')
    certificates = Certificate.objects.all().order_by('-date')   # получаем сертификаты

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Сообщение успешно отправлено!'})
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('home')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()

    context = {
        'projects': projects,
        'certificates': certificates,   # теперь определена
        'form': form
    }
    return render(request, 'portfolio/index.html', context)