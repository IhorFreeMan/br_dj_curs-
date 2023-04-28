# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from index import models



class NotesForm(ModelForm):

    class Meta:
        model = models.Notes
        fields = '__all__'