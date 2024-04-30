from django.conf import settings
from django.db import models
from graphql import ResolveInfo

# Create your models here.
class Control(models.Model):
    class Adjustability(models.TextChoices):
        OPTIONAL = 'O', 'Optional'
        MANDATORY = 'M', 'Mandatory'
        HIDDEN = 'N', 'Hidden'
        REQUIRED = 'R', 'Required'

    name = models.CharField(db_column='FieldName', primary_key=True, max_length=50)
    adjustability = models.CharField(\
        db_column='Adjustibility', \
        choices=Adjustability.choices, \
        default=Adjustability.OPTIONAL, \
        max_length=1)
    usage = models.CharField(db_column='Usage', max_length=200)

    def __str__(self):
        return f'Field {self.name} ({self.get_adjustability_display()}) for forms {self.usage}'

    @classmethod
    def filter_queryset(cls, queryset=None):
        if queryset is None:
            queryset = cls.objects.all()
        return queryset

    @classmethod
    def get_queryset(cls, queryset, user):
        queryset = Control.filter_queryset(queryset)

        return queryset

    class Meta:
        managed = False
        db_table = 'tblControls'
