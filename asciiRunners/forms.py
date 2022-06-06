from django import forms

class RunnerForm(forms.Form):
    runner_id = forms.CharField(label='Runner ID', max_length=5)
    contrast_mode = forms.CharField(label='Contrast Mode', max_length=1)
    character_type = forms.CharField(label='Character Type', max_length=20)