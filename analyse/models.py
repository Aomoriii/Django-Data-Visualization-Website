from django.db import models

# Create your models here.
class Technology(models.Model):
    Tid = models.IntegerField(primary_key=True)
    Tname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Technology'

class Direction(models.Model):
    Did = models.IntegerField(primary_key=True)
    Tid_id = models.ForeignKey(Technology,models.DO_NOTHING)
    Ddirection = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Direction'
        verbose_name = verbose_name_plural = "职业方向"


class City(models.Model):
    Cid = models.IntegerField(primary_key=True)
    Cname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'City'


class Area(models.Model):
    Aid = models.IntegerField(primary_key=True)
    Aname = models.CharField(max_length=255)
    Cid_id = models.ForeignKey(City,models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Area'
        verbose_name = verbose_name_plural = "行政区"


class Recruit(models.Model):
    Rid = models.IntegerField(primary_key=True)
    Did_id = models.ForeignKey(Direction,models.DO_NOTHING)
    Rex_l = models.CharField(max_length=255)
    Rex_r = models.CharField(max_length=255)
    Rdegree = models.CharField(max_length=255)
    Rsalary_l = models.CharField(max_length=255)
    Rsalary_r = models.CharField(max_length=255)
    Rwelfare = models.CharField(max_length=5000)
    Rwork = models.CharField(max_length=500)
    Rscale_l = models.CharField(max_length=255)
    Rscale_r = models.CharField(max_length=255)
    Cid_id = models.ForeignKey(City,models.DO_NOTHING)
    Aid_id = models.ForeignKey(Area,models.DO_NOTHING)
    Rfinancing = models.CharField(max_length=255)
    Rjob = models.CharField(max_length=255)
    Rdate = models.CharField(max_length=255)
    Rcompany = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Recruit'
        ordering = ['-Rdate']
        verbose_name = verbose_name_plural = "招聘信息"

class Learning(models.Model):
    Lid = models.IntegerField(primary_key=True)
    Ltype = models.CharField(max_length=255)
    Lname = models.CharField(max_length=255)
    Ldetail = models.CharField(max_length=10000)
    Ldirection = models.ForeignKey(Direction,models.DO_NOTHING)
    Lpic = models.CharField(max_length=255)
    Lurl =  models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'Learning'
        verbose_name = verbose_name_plural = "学习路径"


