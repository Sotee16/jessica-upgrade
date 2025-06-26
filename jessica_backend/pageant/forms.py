from django import forms
from .models import Photo

 

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError("Image file too large ( > 5MB )")
            if not image.content_type.startswith("image"):
                raise forms.ValidationError("Only image files are allowed.")
        return image


widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
}
