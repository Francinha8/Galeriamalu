
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Photo, Upload
from .forms import UploadForm

def home(request):
    return render(request, 'photos/home.html')

def galeria(request):
    uploads = Upload.objects.filter(approved=True).order_by('-upload_date')
    form = UploadForm
    return render(request, 'photos/galeria.html', {
        'uploads': uploads, 
        'form': form
    })

def upload_photo(request):
    if request.method == 'POST':
        files = request.FILES.getlist('photos')


        upload = Upload.objects.create()  # Aqui você pode criar um upload se precisar associar às fotos
        
        # Processar cada arquivo enviado
        for file in files:
            # Crie o objeto Photo para cada arquivo e associe ao modelo
            photo = Photo.objects.create(image=file, uploaded_by=request.user)
            # Adiciona a foto ao upload (caso queira associar o upload às fotos)
            upload.approved = True
            upload.photos.add(photo)  # Isso assume que você tem um campo ManyToMany no seu modelo Upload
        
        upload.save()

    return redirect('galeria')