from django.db import models

# Create your models here.
from rest_framework import serializers


class Resolver(models.Model):
    ident = models.CharField(max_length=2084, db_index=True)
    to = models.CharField(max_length=2084, db_index=True)
    created_ip = models.CharField(max_length=128, db_index=True)
    last_accessed = models.DateTimeField()

class ResolverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resolver
        fields = ('ident', 'to')

