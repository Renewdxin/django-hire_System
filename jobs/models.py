from _datetime import datetime
from django.utils.translation import gettext_lazy as _
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

DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))



class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name='Job Type')
    job_name = models.CharField(max_length=100, blank=False, verbose_name='Job Name')
    job_city = models.SmallIntegerField(choices=JobCities, verbose_name='Job City')
    job_responsibility = models.TextField(max_length=1024, verbose_name='Job Responsibility')
    job_requirements = models.TextField(max_length=1024, blank=False, verbose_name='Job Requirements')
    creator = models.ForeignKey(User,verbose_name='Creator', on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='Create Date', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='Last Modified Date', default=datetime.now)

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Joblist')

    def __str__(self):
        return self.job_name

class Resume(models.Model):
    # Translators: 简历实体的翻译
    username = models.CharField(max_length=135, verbose_name=_('姓名'))
    applicant = models.ForeignKey(User, verbose_name=_("申请人"), null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name=_('城市'))
    phone = models.CharField(max_length=135, verbose_name=_('手机号码'))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_('邮箱'))
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=_('应聘职位'))
    born_address = models.CharField(max_length=135, blank=True, verbose_name=_('生源地'))
    gender = models.CharField(max_length=135, blank=True, verbose_name=_('性别'))
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=_('个人照片'))
    attachment = models.FileField(upload_to='file/', blank=True, verbose_name=_('简历附件'))

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=_('本科学校'))
    master_school = models.CharField(max_length=135, blank=True, verbose_name=_('研究生学校'))
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'博士生学校')
    major = models.CharField(max_length=135, blank=True, verbose_name=_('专业'))
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=_('学历'))
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=u'自我介绍')
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'工作经历')
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'项目经历')

    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历列表')

    def __str__(self):
        return self.username