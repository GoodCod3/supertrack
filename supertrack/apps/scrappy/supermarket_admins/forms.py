from django import forms

from supertrack.apps.scrappy.models import InternalProductCategory


class CategoryAssignmentForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    category = forms.ModelChoiceField(
        queryset=InternalProductCategory.objects.all(),
        label='Assigning category',
        widget=forms.Select(attrs={'id': 'category_select'}),
        required=True,
    )
