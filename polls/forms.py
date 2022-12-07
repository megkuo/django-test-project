"""
REFERENCES
Used to figure out how to use forms and the HTML for it
Title: authorForm
Author: MDN contributors, Mozilla Contributors
Date: 9.22.22
URL: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#generic_editing_views
Software License: public domain

Helpful resources from a TA:
Title: manage_authors(), authorForm, ArtileForm()
Date: 9.22.22
URL: https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/

Title: ContactForm()
Author: Vitor Freitas
Date: 9.22.22
URL: https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
Software License: Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)

Title: views.py, template.html
Author: W3Schools contributors
Date: 9.22.22
URL: https://www.w3schools.com/django/django_template_variables.php

other tips: 
combine two forms, deal with input elsewhere
model for deepthought, deep thought form class (creating new models from form, specific classes to make it easier for us)
class 
artile form, 
second page
 views.py, form
DO NOT DO contact form class
author form
don't pass, save() to database
also gets called for get request, generates new form

"""

import datetime
from email.charset import Charset

from django.forms import ModelForm
from .models import DeepThought

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class DeepThoughtForm(ModelForm):
        class Meta:
            model = DeepThought
            fields = ['title', 'thoughts_text']
            # title_text = Charset(help_text="Enter a title.")
            # thoughts_text = Charset(help_text="Enter a deep thought.")
            # pub_date = forms.DateTimeField()
            help_texts = {
                'title_help': _('Enter title here!.'),
                'thought_text_help': _('Enter thoughts here!.'),
            }

            def clean_title_text(self):
                data = self.cleaned_data['title_text']

                # Check if a title is not blank.
                if len(data) == 0:
                    raise ValidationError(_('No text in submission!'))

                # # Check if a date is in the allowed range (+4 weeks from today).
                # if data > datetime.date.today() + datetime.timedelta(weeks=4):
                #     raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

                # # Remember to always return the cleaned data.
                cleaned_data = super(ContactForm, self).clean()
                title = cleaned_data.get('title')
                thought_text = cleaned_data.get('thought_text')
                
                return data


        