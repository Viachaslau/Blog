from django import forms
from .models import Enter


class PostForm(forms.ModelForm):
   class Meta:
      model = Enter
      fields = "__all__"
 
      
