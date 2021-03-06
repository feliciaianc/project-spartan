# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.
from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from .models import Report


class CreateReportForm(forms.ModelForm):

    status = forms.ChoiceField(choices=[(x, x) for x in ['Employer',
                                                         'Spartan']])

    class Meta:
        model = Report
        exclude = ["author"]
        widgets = {'text': forms.Textarea(attrs={'required': 'required',
                                                 'placeholder': 'text'})
                   }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateReportForm, self).__init__(*args, **kwargs)

    def clean_status(self):
        username = self.cleaned_data['username']
        status = self.cleaned_data['status']
        try:
            user = User.objects.get(username=username)
            if user.username == self.user.username:
                raise ValidationError("You can't report yourself!")
            elif status == "Spartan" and not user.account.has_related_object():
                raise ValidationError("This user is not a spartan")
            elif(Report.objects.filter(author=self.user,
                                       status=status,
                                       username=username).count()):
                raise ValidationError("You already submitted a report"
                                      "for this user as a " + status)
        except User.DoesNotExist:
            raise ValidationError("This user does not exists")
        return status

    def clean_text(self):
        description = self.cleaned_data['text']
        if len(description) < 50:
            raise ValidationError("Description has to be"
                                  "at least 50 characters long")
        return description
