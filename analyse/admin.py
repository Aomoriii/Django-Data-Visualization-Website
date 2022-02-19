from django.contrib import admin
from .models import Recruit, Direction, Learning, Area, Technology, City
# Register your models here.

admin.site.site_header = 'Aomori的后台'
admin.site.site_title = 'Aomori的后台'
admin.site.index_title = 'Aomori的后台'


class RecruitAdmin(admin.ModelAdmin):
    list_display = ['Rid', 'Rdegree', 'Rwelfare', 'Rwork', 'Rfinancing', 'Rdate', 'Rcompany']
    fields = ['Rid', 'Rex_l', 'Rex_r', 'Rdegree', 'Rsalary_l', 'Rsalary_r', 'Rwelfare', 'Rwork',
                    'Rscale_l', 'Rscale_r', 'Cid_id', 'Aid_id', 'Rfinancing', 'Rjob', 'Rdate', 'Rcompany']


class DirectionAdmin(admin.ModelAdmin):
    list_display = ['Did', 'Ddirection']
    fields = ['Did', 'Tid_id', 'Ddirection']


class LearningAdmin(admin.ModelAdmin):
    list_display = ['Lid', 'Ltype', 'Lname', 'Ldetail', 'Lurl']
    fields = ['Lid', 'Ltype', 'Lname', 'Ldetail', 'Lpic', 'Lurl']

class AreaAdmin(admin.ModelAdmin):
    list_display = ['Aid', 'Aname', 'Cid_id']
    fields = ['Aid', 'Aname', 'Cid_id']


class CityAdmin(admin.ModelAdmin):
    list_display = ['Cid', 'Cname']
    fields = ['Cid', 'Cname']


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['Tid', 'Tname']
    fields = ['Tid', 'Tname']


admin.site.register(Recruit, RecruitAdmin)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(Learning, LearningAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(City, CityAdmin)
