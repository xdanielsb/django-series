from django import forms

from apps.pet.models import Pet

class PetForm(forms.ModelForm):

    class Meta:
        # Points out of which  model  we are going to create this form  "What table is related"
        model = Pet

        fields = [
            'name',
            'genre',
            'age',
            'rescue_date',
            'owner',
            'vaccines',
        ]

        labels = {
            'name':'Name',
            'genre':'Genre',
            'age':'Age',
            'rescue_date':'Rescue Date',
            'owner':'Owner',
            'vaccines':'Vaccines',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'genre':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'rescue_date':forms.DateInput(attrs={'class':'form-control'}),
            'owner':forms.Select(attrs={'class':'form-control'}),
            'vaccines':forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),

        }
