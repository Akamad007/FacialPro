'''
Created on Jul 18, 2015

@author: akash
'''


from django import forms 
from home.models import HomeImages


class HomeImagesForm(forms.ModelForm):
    class Meta:
        model = HomeImages
        fields = ["image","title"]
        





    