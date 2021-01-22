from django import forms
from django.contrib.auth.models import User
from users.models import Profile
import cloudinary.uploader
from cloudinary.models import CloudinaryField
import cloudinary
from poetry.models import Love,Spiritual,Anger,Death,Family,Famous,Friendship,Holiday,Life,Nature,Sad,Christian,Coronavirus


class NewLoveForm(forms.ModelForm):
    class Meta:
        model = Love
        fields=__all__

class NewSpiritualForm(forms.ModelForm):
    class Meta:
        model = Spiritual

        fields=__all__

class NewAngerForm(forms.ModelForm):
    class Meta:
        model = Anger

        fields=__all__

class NewDeathForm(forms.ModelForm):
    class Meta:
        model = Death

        fields=__all__

class NewFamilyForm(forms.ModelForm):
    class Meta:
        model = Family

        fields=__all__

class NewFamousForm(forms.ModelForm):
    class Meta:
        model = Famous

        fields=__all__

class NewFriendshipForm(forms.ModelForm):
    class Meta:
        model = Friendship

        fields=__all__

class NewHolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday

        fields=__all__

class NewLifeForm(forms.ModelForm):
    class Meta:
        model = Life

        fields=__all__

class NewNatureForm(forms.ModelForm):
    class Meta:
        model = Nature

        fields=__all__

class NewSadForm(forms.ModelForm):
    class Meta:
        model = Sad

        fields=__all__

class NewChristianForm(forms.ModelForm):
    class Meta:
        model = Christian

        fields=__all__

class NewCoronavirusForm(forms.ModelForm):
    class Meta:
        model = Coronavirus

        fields=__all__
