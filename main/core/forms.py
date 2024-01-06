from django import forms
from django.contrib.auth.models import User
from .models import Profile

#combine ProfileForm and UserForm into one form

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'  # This includes all fields in the form

class CombinedForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'address')

    def save(self, commit=True):
        user = super(CombinedForm, self).save(commit=False)
        profile = ProfileForm(self.data)
        if commit:
            user.save()
            profile_data = profile.save(commit=False)
            profile_data.user = user
            profile_data.save()
        return user        