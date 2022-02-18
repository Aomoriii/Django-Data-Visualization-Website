# *-* coding=utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Recruit, Direction, Area, Learning
from django.core.paginator import Paginator
from pure_pagination.mixins import PaginationMixin
from django.views.generic import ListView
from django.db.models import Avg
from decimal import Decimal
# Create your views here.


class IndexView(TemplateView):
    template_name = "recruit/index.html"


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "信息无法匹配"
        return render(request, 'recruit/result.html', {'error_msg': error_msg})

    result = Recruit.objects.filter(Rwork__icontains=q)
    paginator = Paginator(result,15)


    contacts = paginator.get_page(result)

    return render(request, 'recruit/result.html', {
        'error_msg': error_msg,
        'contacts': contacts
    })


class TableView(PaginationMixin, ListView):
    model = Recruit
    template_name = 'recruit/table.html'
    context_object_name = 'recruit_list'
    paginate_by = 15


def company(request):
    # 金字塔x轴参数：a,b,c,d
    a = Recruit.objects.filter(Rscale_l__range=(0, 100))
    b = Recruit.objects.filter(Rscale_l__range=(150, 300))
    c = Recruit.objects.filter(Rscale_l__range=(350, 500))
    d = Recruit.objects.filter(Rscale_l__range=(1000, 1200))
    e = Recruit.objects.filter(Rscale_l__gte=(1500))

    # 2学历扇形图
    Junior_college = Recruit.objects.filter(Rdegree__contains='大专')
    Undergraduate = Recruit.objects.filter(Rdegree__contains='本科')
    master = Recruit.objects.filter(Rdegree__contains='硕士')
    high_school = Recruit.objects.filter(Rdegree__contains='高中')
    ts_school = Recruit.objects.filter(Rdegree__contains='中专/中技')
    no_exp = Recruit.objects.filter(Rdegree__contains='学历不限')

    #地区岗位供求图 Area
    area = {}
    for i in range(1, 12):
        area[i] = Area.objects.get(Aid=i).recruit_set.all()

    return render(request,'recruit/Company.html',
                  {
                      'a': len(a), 'b': len(b), 'c': len(c), 'd':len(d),'e': len(e),
                      'Junior_college': len(Junior_college), 'Undergraduate': len(Undergraduate), 'master': len(master),
                      'high_school': len(high_school), 'ts_school': len(ts_school), 'no_exp': len(no_exp),
                      'area1': len(area[1]), 'area2': len(area[2]), 'area3': len(area[3]), 'area4': len(area[4]),
                      'area5': len(area[5]), 'area6': len(area[6]), 'area7': len(area[7]), 'area8': len(area[8]),
                      'area9': len(area[9]), 'area10': len(area[10]), 'area11': len(area[11]),

                  }
                  )


def welfare(request):
    welfare_list = Recruit.objects.values('Rwelfare')
    list = ''
    for i in range(200):
        list = list + str(welfare_list[i]['Rwelfare']) + ','

    job_list = Recruit.objects.values('Rwork')
    jobs = ''
    for i in range(200):
        jobs = jobs + str(job_list[i]['Rwork']) + ','

    return render(request, 'recruit/Welfare.html', {
        'welfare_list': list, 'jobs': jobs,
    })


def salary(request):
    # 薪资统计图 salary
    salary = {}
    for i in range(1, 16):
        j = i + 1
        salary[i] = Recruit.objects.filter(Rsalary_l__contains='{}k'.format(j))

    # 6折线图
    dates = {}
    company_list = ['民营', '上市公司', '国企', '合资', '外商独资', '股份制企业', '港澳台公司']
    for i in range(len(company_list)):
        dates['{}1'.format(company_list[i])] = Recruit.objects. \
            filter(Rfinancing__contains=company_list[i]).filter(Rsalary_l__contains='4k')
        dates['{}2'.format(company_list[i])] = Recruit.objects. \
            filter(Rfinancing__contains=company_list[i]).filter(Rsalary_l__range=('4k', '6k'))
        dates['{}3'.format(company_list[i])] = Recruit.objects. \
            filter(Rfinancing__contains=company_list[i]).filter(Rsalary_l__range=('7k', '9k'))
        dates['{}4'.format(company_list[i])] = Recruit.objects. \
            filter(Rfinancing__contains=company_list[i]).filter(Rsalary_l__range=('10k', '15k'))

    #热门语言与薪资统计图
    Did_list = [4, 1, 3]
    hot_data = {}
    for j in range(len(Did_list)):
        hot_data['Did_{}_1'.format(Did_list[j])] = Direction.objects.\
            get(Did=Did_list[j]).recruit_set.filter(Rsalary_l__range=('2k', '6k'))
        hot_data['Did_{}_2'.format(Did_list[j])] = Direction.objects. \
            get(Did=Did_list[j]).recruit_set.filter(Rsalary_l__range=('7k', '9k'))
        hot_data['Did_{}_3'.format(Did_list[j])] = Direction.objects. \
            get(Did=Did_list[j]).recruit_set.filter(Rsalary_l__range=('10k', '15k'))

    # 各地区平均薪资空心饼图
    area_list = {}
    for i in range(1, 12):
        area_list[i] = Area.objects.get(Aid=i).recruit_set.aggregate(Avg('Rsalary_r'))
        area_list[i] = area_list[i]['Rsalary_r__avg']
        if area_list[i] == None:
            area_list[i] = 0
        area_list[i] = Decimal(area_list[i]).quantize(Decimal("0.00"))

    return render(request, 'recruit/Salary.html',{
        # 薪资统计图
        'sa1': len(salary[1]), 'sa2': len(salary[2]), 'sa3': len(salary[3]), 'sa4': len(salary[4]),
        'sa5': len(salary[5]), 'sa6': len(salary[6]),
        'sa7': len(salary[7]), 'sa8': len(salary[8]), 'sa9': len(salary[9]), 'sa10': len(salary[10]),
        'sa11': len(salary[11]), 'sa12': len(salary[12]),
        'sa13': len(salary[13]), 'sa14': len(salary[14]), 'sa15': len(salary[15]),
        #企业类型与薪资关系图
        'p1': len(dates['民营1']), 'p2': len(dates['民营2']), 'p3': len(dates['民营3']), 'p4': len(dates['民营4']),
        'l1': len(dates['上市公司1']), 'l2': len(dates['上市公司2']), 'l3': len(dates['上市公司3']), 'l4': len(dates['上市公司4']),
        's1': len(dates['国企1']), 's2': len(dates['国企2']), 's3': len(dates['国企3']), 's4': len(dates['国企4']),
        'j1': len(dates['合资1']), 'j2': len(dates['合资2']), 'j3': len(dates['合资3']), 'j4': len(dates['合资4']),
        'f1': len(dates['外商独资1']), 'f2': len(dates['外商独资2']), 'f3': len(dates['外商独资3']), 'f4': len(dates['外商独资4']),
        'sh1': len(dates['股份制企业1']), 'sh2': len(dates['股份制企业2']), 'sh3': len(dates['股份制企业3']),
        'sh4': len(dates['股份制企业4']),
        'hmt1': len(dates['港澳台公司1']), 'hmt2': len(dates['港澳台公司2']), 'hmt3': len(dates['港澳台公司3']),
        'hmt4': len(dates['港澳台公司4']),
        #热门语言与薪资关系图
        'py1': len(hot_data['Did_4_1']), 'py2': len(hot_data['Did_4_2']), 'py3': len(hot_data['Did_4_3']),
        'java1': len(hot_data['Did_1_1']), 'java2': len(hot_data['Did_1_2']), 'java3': len(hot_data['Did_1_3']),
        'php1': len(hot_data['Did_3_1']), 'php2': len(hot_data['Did_3_2']), 'php3': len(hot_data['Did_3_3']),
        #各地区平均薪资
        'a1': area_list[1], 'a2': area_list[2], 'a3': area_list[3], 'a4': area_list[4],
        'a5': area_list[5], 'a7': area_list[7], 'a8': area_list[8], 'a9': area_list[9],
        'a10': area_list[10], 'a11': area_list[11],
    })


def degree(request):
    #学历与薪资统计图
    dates = {}
    degree_list = ['本科', '大专', '硕士', '学历不限', '中专/中技']
    for i in range(len(degree_list)):
        dates['{}1'.format(degree_list[i])] = Recruit.objects.\
            filter(Rdegree__contains=degree_list[i]).filter(Rsalary_l__range=('2k', '4k'))
        dates['{}2'.format(degree_list[i])] = Recruit.objects. \
            filter(Rdegree__contains=degree_list[i]).filter(Rsalary_l__range=('5k', '8k'))
        dates['{}3'.format(degree_list[i])] = Recruit.objects. \
            filter(Rdegree__contains=degree_list[i]).filter(Rsalary_l__range=('10k', '13k'))

    #学历与经验统计图
    degree_lists = ['本科', '大专', '学历不限']
    for j in range(len(degree_lists)):
        dates['{}4'.format(degree_lists[j])] = Recruit.objects.\
            filter(Rdegree__contains=degree_lists[j]).filter(Rex_l__contains=0)
        dates['{}5'.format(degree_lists[j])] = Recruit.objects. \
            filter(Rdegree__contains=degree_lists[j]).filter(Rex_l__contains=3)
        dates['{}6'.format(degree_lists[j])] = Recruit.objects. \
            filter(Rdegree__contains=degree_lists[j]).filter(Rex_l__contains=5)

    return render(request, 'recruit/Degree.html', {
                                'u1': len(dates['本科1']), 'u2': len(dates['本科2']), 'u3': len(dates['本科3']),
                                'j1': len(dates['大专1']), 'j2': len(dates['大专2']), 'j3': len(dates['大专3']),
                                'm1': len(dates['硕士1']), 'm2': len(dates['硕士2']), 'm3': len(dates['硕士3']),
                                'n1': len(dates['学历不限1']), 'n2': len(dates['学历不限2']), 'n3': len(dates['学历不限3']),
                                'ts1': len(dates['中专/中技1']), 'ts2': len(dates['中专/中技2']), 'ts3': len(dates['中专/中技3']),
                                'u4': len(dates['本科4']), 'u5': len(dates['本科5']), 'u6': len(dates['本科6']),
                                'j4': len(dates['大专4']), 'j5': len(dates['大专5']), 'j6': len(dates['大专6']),
                                'n4': len(dates['学历不限4']), 'n5': len(dates['学历不限5']), 'n6': len(dates['学历不限6']),

    })


class LearningRecommendView(TemplateView):
    template_name = 'recruit/learning.html'


class LearningView(PaginationMixin, ListView):
    model = Learning
    template_name = 'recruit/resource.html'
    context_object_name = 'resource_list'
    paginate_by = 6

