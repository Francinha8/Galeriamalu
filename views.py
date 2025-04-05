from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Photo
from .forms import PhotoForm  # Assumindo que você tem um formulário para o modelo Photo

def home(request):
    # Adicione 'debug': True se estiver em desenvolvimento
    context = {'debug': False}  # ou use settings.DEBUG para detecção automática
    return render(request, 'home.html', context)

def galeria(request):
    photos = Photo.objects.filter(approved=True).order_by('-upload_date')
    form = PhotoForm()
    return render(request, 'galeria.html', {'photos': photos, 'form': form})

def upload_photo(request):
    if request.method == 'POST':
        # Verificar se foram enviados múltiplos arquivos
        if 'images' in request.FILES:
            files = request.FILES.getlist('images')
            success_count = 0
            
            # Processar cada arquivo
            for f in files:
                photo = Photo(image=f)
                # Opcional: Adicionar o usuário se autenticado
                if request.user.is_authenticated:
                    photo.uploaded_by = request.user
                photo.save()
                success_count += 1
            
            # Mensagem de sucesso com o número de fotos enviadas
            if success_count == 1:
                messages.success(request, 'Foto enviada com sucesso! Aguarde aprovação.')
            else:
                messages.success(request, f'{success_count} fotos enviadas com sucesso! Aguarde aprovação.')
        else:
            # Fallback para o caso de envio de arquivo único
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                photo = form.save(commit=False)
                if request.user.is_authenticated:
                    photo.uploaded_by = request.user
                photo.save()
                messages.success(request, 'Foto enviada com sucesso! Aguarde aprovação.')
            else:
                messages.error(request, 'Erro ao enviar foto. Verifique se o formato é válido.')
    
    return redirect('galeria')