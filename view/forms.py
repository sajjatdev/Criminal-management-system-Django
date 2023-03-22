from django import forms

from view.models import ReportModel


class reportForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = ['name', 'phone', 'email', 'title', 'description', 'document']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['phone'].label = ''
        self.fields['title'].label = ''
        self.fields['email'].label = ''
        self.fields['description'].label = ''
        self.fields['document'].label = ''

        self.fields['name'].widget.attrs.update(
            {' placeholder': 'Name', 'class': 'border-none w-full h-[35px] rounded-lg px-2 focus:outline-none ring-2 ring-blue-300 focus:hover:ring-3 focus:hover:ring-blue-400'})

        self.fields['email'].widget.attrs.update(
            {' placeholder': 'Email', 'class': 'border-none w-full h-[35px] rounded-lg px-2 focus:outline-none ring-2 ring-blue-300 focus:hover:ring-3 focus:hover:ring-blue-400'})

        self.fields['phone'].widget.attrs.update(
            {' placeholder': 'Phone', 'class': 'border-none w-full h-[35px] rounded-lg px-2 focus:outline-none ring-2 ring-blue-300 focus:hover:ring-3 focus:hover:ring-blue-400'})
        self.fields['title'].widget.attrs.update(
            {' placeholder': 'Title', 'class': 'border-none w-full h-[35px] rounded-lg px-2 focus:outline-none ring-2 ring-blue-300 focus:hover:ring-3 focus:hover:ring-blue-400'})
        self.fields['description'].widget.attrs.update(
            {' placeholder': 'Describe about the incident...', 'class': 'border-none w-full  rounded-lg px-2 focus:outline-none ring-2 ring-blue-300 focus:hover:ring-3 focus:hover:ring-blue-400'})
