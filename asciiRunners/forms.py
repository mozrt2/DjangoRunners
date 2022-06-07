from django import forms

class RunnerForm(forms.Form):
    runner_id = forms.CharField(label='Runner ID', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contrast_mode = forms.CharField(label='Contrast Mode', max_length=1, widget=forms.TextInput(attrs={'class': 'form-control'}))
    character_type = forms.CharField(label='Character Type', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))