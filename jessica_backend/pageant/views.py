from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404
from .forms import PhotoForm  

 

 

# Delete invalid photos (optional)
Photo.objects.filter(image='').delete()

# Get only valid photos
photos = Photo.objects.exclude(image='').exclude(pk=None)



photos = Photo.objects.exclude(image='').exclude(pk=None)
# pageant/views.py

def home(request):
    return HttpResponse("Hello from the Pageant App!")



from django.core.paginator import Paginator

def gallery(request):
    photos = Photo.objects.all().order_by('-id')
    paginator = Paginator(photos, 6)  # 6 photos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = PhotoForm()
    return render(request, 'pageant/gallery.html', {
        'form': form,
        'page_obj': page_obj
    })


def gallery(request):
    form = PhotoForm()
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('gallery')  # ✅ redirect after POST
        else:
            messages.error(request, 'Upload failed. Check the form and try again.')

    photos = Photo.objects.all().order_by('-id')
    paginator = Paginator(photos, 6)  # 6 photos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pageant/gallery.html', {
        'form': form,
        'page_obj': page_obj,
    })  # ✅ This must be returned
 

def edit_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo updated successfully!')
            return redirect('gallery')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'pageant/edit_photo.html', {'form': form})

def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    messages.success(request, 'Photo deleted successfully!')
    return redirect('gallery')

def homepage(request):
    return render(request, 'pageant/home.html')
 

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('gallery')  # or your redirect view name
    else:
        form = PhotoForm()
    ...

