from _datetime import datetime

from django.db import models
from django.contrib.auth.models import User


JobTypes = [
    (0, "Backend"),
    (1, "Frontend"),
    (2, "Android"),
    (3, "iOS"),
]

JobCities = [
    (0, "Beijing"),
    (1, "Shanghai"),
    (2, "Guangzhou"),
    (3, "Shenzhen"),
]



class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name='Job Type')
    job_name = models.CharField(max_length=100, blank=False, verbose_name='Job Name')
    job_city = models.SmallIntegerField(choices=JobCities, verbose_name='Job City')
    job_responsibility = models.TextField(max_length=1024, verbose_name='Job Responsibility')
    job_requirements = models.TextField(max_length=1024, blank=False, verbose_name='Job Requirements')
    creator = models.ForeignKey(User,verbose_name='Creator', on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='Create Date', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='Last Modified Date', default=datetime.now)



