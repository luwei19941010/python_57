from django.shortcuts import render
from APP01 import models
# Create your views here.
import datetime

data_now=datetime.datetime.now()
def index(request):
    # user_obj=models.user(
    #     name='luwei',
    #     age=20
    # )
    # user_obj.save()

    # new_obj=models.user.objects.create(name='luwei1',age=21)
    # new_obj=models.user.objects.create(**{'name':'luwei3','age':23})

    # obj_list=[]
    # for i in range (5,30):
    #     obj=models.user(
    #         name='luwei%s'%i,
    #         age=20+i
    #     )
    #     obj_list.append(obj)
    # models.user.objects.bulk_create(obj_list)

    # models.user.objects.update_or_create(
    #     name='Daivlu',
    #     defaults={
    #         'age':100,
    #     }
    # )

    # obj=models.user.objects.get(name='luwei')     #models对象
    # obj=models.user.objects.filter(id=2)    #queryset集合
    # obj=models.user.objects.all()   #获取所有 queryset 集合

    # obj=models.user.objects.get(id=3).delete()
    # obj=models.user.objects.filter(name='luwei').delete()
    # obj=models.user.objects.all().delete()

    # obl=models.user.objects.get(name='luwei').update(age=111)
    # obj=models.user.objects.filter(name='luwei').update(age=111)

    # obj=models.user.objects.filter(id=57)

    # obj=models.user.objects.filter(**{'id':56,'name':'luweiwei'}).update(name='weilu',age=10)
    # obj=models.user.objects.filter(id=57,name='luwei11').update(name='luwei111',age=130)

    # obj=models.user.objects.exclude(id=60)
    # obj=models.user.objects.exclude(**{'id':60,'name':'luwei'})

    # obj = models.user.objects.order_by('age', 'name')
    # obj=models.user.objects.order_by('-age','name')

    # obj=models.user.objects.all().count()
    # obj=models.user.objects.filter(name__contains='i1').count()

    # obj=models.user.objects.first()
    # obj=models.user.objects.filter(name='luwei22').exists()

    # obj=models.user.objects.all().values()
    # obj=models.user.objects.filter(age__gt=14).values_list()

    # obj=models.user.objects.all().values('name').distinct()

    # obj=models.user.objects.filter(age__in=[10,14,11,12])
    # obj=models.user.objects.filter(age__range=[13,15])

    # obj=models.user.objects.filter(name__icontains='lu')


    # obj=models.data.objects.create(name='luwei',data=data_now)

    obj=models.data.objects.create(name='lu',data='2000-12-12')
    print(type(obj),obj.data)
    # print(obj[0].age,obj[0].name)



    return render(request,'index.html')

