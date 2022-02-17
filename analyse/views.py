# *-* coding=utf-8 -*-
from django.shortcuts import render
from .models import Recruit,Technology,Direction,City,Area,Learning
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from pure_pagination.mixins import PaginationMixin
from django.views.generic import ListView
from django.db.models import Avg
# Create your views here.




def index(request):
    return render(request,'recruit/index.html')



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

class TableView(PaginationMixin,ListView):
    model = Recruit
    template_name = 'recruit/table.html'
    context_object_name = 'recruit_list'
    paginate_by = 15


def company(request):
    # 金字塔x轴参数：a,b,c,d
    a = Recruit.objects.filter(Rscale_l__range=(0,100))
    b = Recruit.objects.filter(Rscale_l__range=(150,300))
    c = Recruit.objects.filter(Rscale_l__range=(350,500))
    d = Recruit.objects.filter(Rscale_l__range=(1000,1200))
    e = Recruit.objects.filter(Rscale_l__gte=(1500))


    # 2学历扇形图
    Junior_college = Recruit.objects.filter(Rdegree__contains='大专')
    Undergraduate = Recruit.objects.filter(Rdegree__contains='本科')
    master = Recruit.objects.filter(Rdegree__contains='硕士')
    high_school = Recruit.objects.filter(Rdegree__contains='高中')
    ts_school = Recruit.objects.filter(Rdegree__contains='中专/中技')
    no_exp = Recruit.objects.filter(Rdegree__contains='学历不限')

    #地区岗位供求图 Aear
    a1 = Area.objects.get(Aid=1).recruit_set.all()
    a2 = Area.objects.get(Aid=2).recruit_set.all()
    a3 = Area.objects.get(Aid=3).recruit_set.all()
    a4 = Area.objects.get(Aid=4).recruit_set.all()
    a5 = Area.objects.get(Aid=5).recruit_set.all()
    a6 = Area.objects.get(Aid=6).recruit_set.all()
    a7 = Area.objects.get(Aid=7).recruit_set.all()
    a8 = Area.objects.get(Aid=8).recruit_set.all()
    a9 = Area.objects.get(Aid=9).recruit_set.all()
    a10 = Area.objects.get(Aid=10).recruit_set.all()
    a11 = Area.objects.get(Aid=11).recruit_set.all()


    return render(request,'recruit/Company.html',
                  {
                      'a': len(a), 'b': len(b), 'c': len(c), 'd':len(d),'e': len(e),
                      'Junior_college': len(Junior_college), 'Undergraduate': len(Undergraduate), 'master': len(master), 'high_school': len(high_school), 'ts_school': len(ts_school), 'no_exp': len(no_exp),
                      'a1': len(a1), 'a2': len(a2), 'a3': len(a3), 'a4': len(a4), 'a5': len(a5), 'a6': len(a6), 'a7': len(a7), 'a8': len(a8), 'a9': len(a9), 'a10': len(a10), 'a11': len(a11),

                  }
                  )

def financing(request):
    welfare_list = Recruit.objects.values('Rwelfare')
    print(welfare_list)
    return render(request,'recruit/Welfare.html')

def district(request):
    return render(request,'recruit/District.html')

def welfare(request):
    welfare_list = Recruit.objects.values('Rwelfare')
    # print(welfare_list)
    list = ''
    for i in range(200):
        list = list + str(welfare_list[i]['Rwelfare']) +','

    #
    job_list = Recruit.objects.values('Rwork')
    jobs = ''
    for i in range(200):
        jobs = jobs + str(job_list[i]['Rwork']) + ','



    return render(request,'recruit/Welfare.html',{
        'welfare_list':list,'jobs':jobs,
    })

def posts(request):
    return render(request,'recruit/Posts.html')

def salsry(request):
    # 薪资统计图 salary
    sa1 = Recruit.objects.filter(Rsalary_l__contains='2k')
    sa2 = Recruit.objects.filter(Rsalary_l__contains='3k')
    sa3 = Recruit.objects.filter(Rsalary_l__contains='4k')
    sa4 = Recruit.objects.filter(Rsalary_l__contains='5k')
    sa5 = Recruit.objects.filter(Rsalary_l__contains='6k')
    sa6 = Recruit.objects.filter(Rsalary_l__contains='7k')
    sa7 = Recruit.objects.filter(Rsalary_l__contains='8k')
    sa8 = Recruit.objects.filter(Rsalary_l__contains='9k')
    sa9 = Recruit.objects.filter(Rsalary_l__contains='10k')
    sa10 = Recruit.objects.filter(Rsalary_l__contains='11k')
    sa11 = Recruit.objects.filter(Rsalary_l__contains='12k')
    sa12 = Recruit.objects.filter(Rsalary_l__contains='13k')
    sa13 = Recruit.objects.filter(Rsalary_l__contains='14k')
    sa14 = Recruit.objects.filter(Rsalary_l__contains='15k')
    sa15 = Recruit.objects.filter(Rsalary_l__contains='16k')

    # 6折线图
    # 民营 private
    p1 = Recruit.objects.filter(Rfinancing__contains='民营').filter(Rsalary_l__contains='4k')
    p2 = Recruit.objects.filter(Rfinancing__contains='民营').filter(Rsalary_l__range=('4k', '6k'))
    p3 = Recruit.objects.filter(Rfinancing__contains='民营').filter(Rsalary_l__range=('7k', '9k'))
    p4 = Recruit.objects.filter(Rfinancing__contains='民营').filter(Rsalary_l__range=('10k', '15k'))
    # 上市公司 Listed company
    l1 = Recruit.objects.filter(Rfinancing__contains='上市公司').filter(Rsalary_l__contains='4k')
    l2 = Recruit.objects.filter(Rfinancing__contains='上市公司').filter(Rsalary_l__range=('4k', '6k'))
    l3 = Recruit.objects.filter(Rfinancing__contains='上市公司').filter(Rsalary_l__range=('7k', '9k'))
    l4 = Recruit.objects.filter(Rfinancing__contains='上市公司').filter(Rsalary_l__range=('10k', '15k'))
    # 国企 State-owned enterprises
    s1 = Recruit.objects.filter(Rfinancing__contains='国企').filter(Rsalary_l__contains='4k')
    s2 = Recruit.objects.filter(Rfinancing__contains='国企').filter(Rsalary_l__range=('4k', '6k'))
    s3 = Recruit.objects.filter(Rfinancing__contains='国企').filter(Rsalary_l__range=('7k', '9k'))
    s4 = Recruit.objects.filter(Rfinancing__contains='国企').filter(Rsalary_l__range=('10k', '15k'))
    # 合资 joint venture
    j1 = Recruit.objects.filter(Rfinancing__contains='合资').filter(Rsalary_l__contains='4k')
    j2 = Recruit.objects.filter(Rfinancing__contains='合资').filter(Rsalary_l__range=('4k', '6k'))
    j3 = Recruit.objects.filter(Rfinancing__contains='合资').filter(Rsalary_l__range=('7k', '9k'))
    j4 = Recruit.objects.filter(Rfinancing__contains='合资').filter(Rsalary_l__range=('10k', '15k'))
    # 外商独资 Foreign-owned
    f1 = Recruit.objects.filter(Rfinancing__contains='外商独资').filter(Rsalary_l__contains='4k')
    f2 = Recruit.objects.filter(Rfinancing__contains='外商独资').filter(Rsalary_l__range=('4k', '6k'))
    f3 = Recruit.objects.filter(Rfinancing__contains='外商独资').filter(Rsalary_l__range=('7k', '9k'))
    f4 = Recruit.objects.filter(Rfinancing__contains='外商独资').filter(Rsalary_l__range=('10k', '15k'))
    # 股份制企业 Shareholding system
    sh1 = Recruit.objects.filter(Rfinancing__contains='股份制企业').filter(Rsalary_l__contains='4k')
    sh2 = Recruit.objects.filter(Rfinancing__contains='股份制企业').filter(Rsalary_l__range=('4k', '6k'))
    sh3 = Recruit.objects.filter(Rfinancing__contains='股份制企业').filter(Rsalary_l__range=('7k', '9k'))
    sh4 = Recruit.objects.filter(Rfinancing__contains='股份制企业').filter(Rsalary_l__range=('10k', '15k'))
    # 港澳台公司  Hong Kong, Macao and Taiwan companies
    hmt1 = Recruit.objects.filter(Rfinancing__contains='港澳台公司').filter(Rsalary_l__contains='4k')
    hmt2 = Recruit.objects.filter(Rfinancing__contains='港澳台公司').filter(Rsalary_l__range=('4k', '6k'))
    hmt3 = Recruit.objects.filter(Rfinancing__contains='港澳台公司').filter(Rsalary_l__range=('7k', '9k'))
    hmt4 = Recruit.objects.filter(Rfinancing__contains='港澳台公司').filter(Rsalary_l__range=('10k', '15k'))

    #热门语言与薪资统计图
    py1 = Direction.objects.get(Did=4).recruit_set.filter(Rsalary_l__range=('2k','6k'))
    py2 = Direction.objects.get(Did=4).recruit_set.filter(Rsalary_l__range=('7k', '9k'))
    py3 = Direction.objects.get(Did=4).recruit_set.filter(Rsalary_l__range=('10k', '15k'))

    java1 = Direction.objects.get(Did=1).recruit_set.filter(Rsalary_l__range=('2k', '6k'))
    java2 = Direction.objects.get(Did=1).recruit_set.filter(Rsalary_l__range=('7k', '9k'))
    java3 = Direction.objects.get(Did=1).recruit_set.filter(Rsalary_l__range=('10k', '15k'))

    php1 = Direction.objects.get(Did=3).recruit_set.filter(Rsalary_l__range=('2k', '6k'))
    php2 = Direction.objects.get(Did=3).recruit_set.filter(Rsalary_l__range=('7k', '9k'))
    php3 = Direction.objects.get(Did=3).recruit_set.filter(Rsalary_l__range=('10k', '15k'))

    # 各地区平均薪资空心饼图
    a1 = Area.objects.get(Aid=1).recruit_set.aggregate(Avg('Rsalary_r'))
    a1 = round(a1['Rsalary_r__avg'],2)

    a2 = Area.objects.get(Aid=2).recruit_set.aggregate(Avg('Rsalary_l'))
    a2 = round(a2['Rsalary_l__avg'], 2)

    a3 = Area.objects.get(Aid=3).recruit_set.aggregate(Avg('Rsalary_l'))
    a3 = round(a3['Rsalary_l__avg'], 2)

    a4 = Area.objects.get(Aid=4).recruit_set.aggregate(Avg('Rsalary_l'))
    a4 = round(a4['Rsalary_l__avg'], 2)

    a5 = Area.objects.get(Aid=5).recruit_set.aggregate(Avg('Rsalary_l'))
    a5 = round(a5['Rsalary_l__avg'], 2)

    # a6 = Area.objects.get(Aid=6).recruit_set.aggregate(Avg('Rsalary_l'))
    # a6 = round(a6['Rsalary_l__avg'], 2)

    a7 = Area.objects.get(Aid=7).recruit_set.aggregate(Avg('Rsalary_l'))
    a7 = round(a7['Rsalary_l__avg'], 2)

    a8 = Area.objects.get(Aid=8).recruit_set.aggregate(Avg('Rsalary_l'))
    a8 = round(a8['Rsalary_l__avg'], 2)

    a9 = Area.objects.get(Aid=9).recruit_set.aggregate(Avg('Rsalary_l'))
    a9 = round(a9['Rsalary_l__avg'], 2)

    a10 = Area.objects.get(Aid=10).recruit_set.aggregate(Avg('Rsalary_l'))
    a10 = round(a10['Rsalary_l__avg'], 2)

    a11 = Area.objects.get(Aid=11).recruit_set.aggregate(Avg('Rsalary_l'))
    a11 = round(a11['Rsalary_l__avg'], 2)

    # print(a1)
    # print(a2)
    # print(a3)
    # print(a4)
    # print(a5)
    # # print(a6)
    # print(a7)
    # print(a8)
    # print(a9)
    # print(a10)
    # print(a11)

    # print(len(py1))
    # print(len(py2))
    # print(len(py3))






    return render(request,'recruit/Salary.html',{
        # 薪资统计图
        'sa1': len(sa1), 'sa2': len(sa2), 'sa3': len(sa3), 'sa4': len(sa4), 'sa5': len(sa5), 'sa6': len(sa6),
        'sa7': len(sa7), 'sa8': len(sa8), 'sa9': len(sa9), 'sa10': len(sa10), 'sa11': len(sa11), 'sa12': len(sa12),
        'sa13': len(sa13), 'sa14': len(sa14), 'sa15': len(sa15),
        #企业类型与薪资关系图
        'p1': len(p1), 'p2': len(p2), 'p3': len(p3), 'p4': len(p4),
        'l1': len(l1), 'l2': len(l2), 'l3': len(l3), 'l4': len(l4),
        's1': len(s1), 's2': len(s2), 's3': len(s3), 's4': len(s4),
        'j1': len(j1), 'j2': len(j2), 'j3': len(j3), 'j4': len(j4),
        'f1': len(f1), 'f2': len(f2), 'f3': len(f3), 'f4': len(f4),
        'sh1': len(sh1), 'sh2': len(sh2), 'sh3': len(sh3), 'sh4': len(sh4),
        'hmt1': len(hmt1), 'hmt2': len(hmt2), 'hmt3': len(hmt3), 'hmt4': len(hmt4),
        #热门语言与薪资关系图
        'py1': len(py1), 'py2': len(py2), 'py3': len(py3),
        'java1': len(java1), 'java2': len(java2), 'java3': len(java3),
        'php1': len(php1), 'php2': len(php2), 'php3': len(php3),
        #各地区平均薪资
        'a1':a1,'a2':a2,'a3':a3,'a4':a4,'a5':a5,'a7':a7,'a8':a8,'a9':a9,'a10':a10,'a11':a11,
    })

def degree(request):
    #学历与薪资统计图
    # 本科
    u1 = Recruit.objects.filter(Rdegree__contains='本科').filter(Rsalary_l__range=('2k','4k'))
    u2 = Recruit.objects.filter(Rdegree__contains='本科').filter(Rsalary_l__range=('5k', '8k'))
    u3 = Recruit.objects.filter(Rdegree__contains='本科').filter(Rsalary_l__range=('10k', '13k'))
    #  大专Junior college
    j1 = Recruit.objects.filter(Rdegree__contains='大专').filter(Rsalary_l__range=('2k', '4k'))
    j2 = Recruit.objects.filter(Rdegree__contains='大专').filter(Rsalary_l__range=('5k', '8k'))
    j3 = Recruit.objects.filter(Rdegree__contains='大专').filter(Rsalary_l__range=('10k', '13k'))
    #硕士 masters
    m1 = Recruit.objects.filter(Rdegree__contains='硕士').filter(Rsalary_l__range=('2k', '4k'))
    m2 = Recruit.objects.filter(Rdegree__contains='硕士').filter(Rsalary_l__range=('5k', '8k'))
    m3 = Recruit.objects.filter(Rdegree__contains='硕士').filter(Rsalary_l__range=('10k', '13k'))
    #经验不限 noexp
    n1 = Recruit.objects.filter(Rdegree__contains='学历不限').filter(Rsalary_l__range=('2k', '4k'))
    n2 = Recruit.objects.filter(Rdegree__contains='学历不限').filter(Rsalary_l__range=('5k', '8k'))
    n3 = Recruit.objects.filter(Rdegree__contains='学历不限').filter(Rsalary_l__range=('10k', '13k'))
    #中技 Technical secondary school
    ts1 = Recruit.objects.filter(Rdegree__contains='中专/中技').filter(Rsalary_l__range=('2k', '4k'))
    ts2 = Recruit.objects.filter(Rdegree__contains='中专/中技').filter(Rsalary_l__range=('5k', '8k'))
    ts3 = Recruit.objects.filter(Rdegree__contains='中专/中技').filter(Rsalary_l__range=('10k', '13k'))
    # print(len(u1))
    # print(len(u2))
    # print(len(u3))

    #学历与经验统计图
    # 本科
    u4 = Recruit.objects.filter(Rdegree__contains='本科').filter(Rex_l__contains=0)
    u5 = Recruit.objects.filter(Rdegree__contains='本科').filter(Rex_l__contains=3)
    u6 = Recruit.objects.filter(Rdegree__contains='本科').filter(Rex_l__contains=5)
    #  大专Junior college
    j4 = Recruit.objects.filter(Rdegree__contains='大专').filter(Rex_l__contains=0)
    j5 = Recruit.objects.filter(Rdegree__contains='大专').filter(Rex_l__contains=3)
    j6 = Recruit.objects.filter(Rdegree__contains='大专').filter(Rex_l__contains=5)
    # # 硕士 masters
    # m4 = Recruit.objects.filter(Rdegree__contains='硕士').filter(Rex_l__contains=0)
    # m5 = Recruit.objects.filter(Rdegree__contains='硕士').filter(Rex_l__contains=3)
    # m6 = Recruit.objects.filter(Rdegree__contains='硕士').filter(Rex_l__contains=5)
    # 学历不限 noexp
    n4 = Recruit.objects.filter(Rdegree__contains='学历不限').filter(Rex_l__contains=0)
    n5 = Recruit.objects.filter(Rdegree__contains='学历不限').filter(Rex_l__contains=3)
    n6 = Recruit.objects.filter(Rdegree__contains='学历不限').filter(Rex_l__contains=5)
    # # 中技 Technical secondary school
    # ts4 = Recruit.objects.filter(Rdegree__contains='中专/中技').filter(Rex_l__contains=0)
    # ts5 = Recruit.objects.filter(Rdegree__contains='中专/中技').filter(Rex_l__contains=3)
    # ts6 = Recruit.objects.filter(Rdegree__contains='中专/中技').filter(Rex_l__contains=5)







    return render(request,'recruit/Degree.html',{
                                'u1': len(u1), 'u2': len(u2), 'u3': len(u3),
                                'j1': len(j1), 'j2': len(j2), 'j3': len(j3),
                                'm1': len(m1), 'm2': len(m2), 'm3': len(m3),
                                'n1':len(n1), 'n2': len(n2), 'n3': len(n3),
                                'ts1': len(ts1), 'ts2': len(ts2), 'ts3': len(ts3),
                                'u4': len(u4), 'u5': len(u5), 'u6': len(u6),
                                'j4': len(j4), 'j5': len(j5),'j6': len(j6),
                                # 'm4': len(m4), 'm5': len(m5),'m6': len(m6),
                                'n4': len(n4), 'n5': len(n5),'n6': len(n6),
                                # 'ts4': len(ts4), 'ts5': len(ts5),'ts6': len(ts6),
    })

def experience(request):
    return render(request,'recruit/Experience.html')

def learning(request):
    return render(request,'recruit/learning.html')

class LearningView(PaginationMixin,ListView):
    model = Learning
    template_name = 'recruit/resource.html'
    context_object_name = 'resource_list'
    paginate_by = 6

