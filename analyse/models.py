from django.db import models
# Create your models here.


class Technology(models.Model):
    Tid = models.IntegerField(primary_key=True, verbose_name='ID')
    Tname = models.CharField(max_length=255, verbose_name='名称')

    class Meta:
        managed = False
        db_table = 'Technology'
        verbose_name = verbose_name_plural = "技术方向"


class Direction(models.Model):
    Did = models.IntegerField(primary_key=True, verbose_name='ID')
    Tid_id = models.ForeignKey(Technology, models.DO_NOTHING, verbose_name='技术方向ID')
    Ddirection = models.CharField(max_length=255, verbose_name='职业方向')

    class Meta:
        managed = False
        db_table = 'Direction'
        verbose_name = verbose_name_plural = "职业方向"


class City(models.Model):
    Cid = models.IntegerField(primary_key=True, verbose_name='城市ID')
    Cname = models.CharField(max_length=255, verbose_name='城市名称')

    class Meta:
        managed = False
        db_table = 'City'
        verbose_name = verbose_name_plural = "城市"


class Area(models.Model):
    Aid = models.IntegerField(primary_key=True, verbose_name='ID')
    Aname = models.CharField(max_length=255, verbose_name='地区名称')
    Cid_id = models.ForeignKey(City, models.DO_NOTHING, verbose_name='城市ID')

    class Meta:
        managed = False
        db_table = 'Area'
        verbose_name = verbose_name_plural = "行政区"


class Recruit(models.Model):
    Rid = models.IntegerField(primary_key=True, verbose_name='ID')
    Did_id = models.ForeignKey(Direction, models.DO_NOTHING, verbose_name='职业方向ID')
    Rex_l = models.CharField(max_length=255, verbose_name='经验min')
    Rex_r = models.CharField(max_length=255, verbose_name='经验max')
    Rdegree = models.CharField(max_length=255, verbose_name='学历')
    Rsalary_l = models.CharField(max_length=255, verbose_name='薪资min')
    Rsalary_r = models.CharField(max_length=255, verbose_name='薪资max')
    Rwelfare = models.CharField(max_length=5000, verbose_name='福利')
    Rwork = models.CharField(max_length=500, verbose_name='工作范畴')
    Rscale_l = models.CharField(max_length=255, verbose_name='公司规模min')
    Rscale_r = models.CharField(max_length=255, verbose_name='公司规模max')
    Cid_id = models.ForeignKey(City,models.DO_NOTHING, verbose_name='城市ID')
    Aid_id = models.ForeignKey(Area,models.DO_NOTHING, verbose_name='行政区ID')
    Rfinancing = models.CharField(max_length=255, verbose_name='公司融资情况')
    Rjob = models.CharField(max_length=255, verbose_name='岗位')
    Rdate = models.CharField(max_length=255, verbose_name='上新日期')
    Rcompany = models.CharField(max_length=255, verbose_name='公司名称')

    class Meta:
        managed = False
        db_table = 'Recruit'
        ordering = ['-Rdate']
        verbose_name = verbose_name_plural = "招聘信息"


class Learning(models.Model):
    Lid = models.IntegerField(primary_key=True, verbose_name='课程ID')
    Ltype = models.CharField(max_length=255, verbose_name='课程类型')
    Lname = models.CharField(max_length=255, verbose_name='课程名称')
    Ldetail = models.CharField(max_length=10000, verbose_name='课程详情')
    Ldirection = models.ForeignKey(Direction, models.DO_NOTHING, verbose_name='技术方向')
    Lpic = models.CharField(max_length=255)
    Lurl = models.CharField(max_length=500, verbose_name='课程连接')

    class Meta:
        managed = False
        db_table = 'Learning'
        verbose_name = verbose_name_plural = "学习路径"

    def __str__(self):
        return self.Lname


