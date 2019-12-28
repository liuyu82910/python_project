from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *arg, **kwargs):
        email = self.cleaned_data.get('email')
        if email.endswith(('edo','gos','io')):
            raise forms.ValidationError('this is an invalid email')
        print(email)
        return email