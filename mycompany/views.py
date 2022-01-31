from django.shortcuts import render, get_object_or_404 , redirect
from django.conf import settings
from django.core.mail import send_mail
from mycompany.models import Category,Product , Referance ,Blog
# Create your views here.


def index(request):

    category = Category.objects.all()

    return render(request, 'central/index.html', {'category': category})



def referance(request):
    service = Category.objects.all()[:4]
    last = Category.objects.all()[4:8]
    ref = Referance.objects.all()
    return render(request,'central/reference.html' , {'ref':ref,'service':service,'last':last})



def bloglist(request):
    service = Category.objects.all()[:4]
    last = Category.objects.all()[4:8]
    blog = Blog.objects.all()



    context={
        'blog':blog,
        'service':service,
        'last':last
    }
    return render(request,'central/blog_list.html',context)



def blog_detail(request,slug):
    service = Category.objects.all()[:4]
    last = Category.objects.all()[4:8]
    product = get_object_or_404(Blog, slug=slug)


    context = {
        'product':product,
        'service':service,
        'last':last
    }

    return render(request,'central/blog_detail.html',context)




def contact(request):
    service = Category.objects.all()[:4]
    last = Category.objects.all()[4:8]
    if 'btnSubmit' in request.POST:
        if True:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            company = request.POST.get('company')
            text = request.POST.get('text')
            message = request.POST.get('message')



            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, "djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nText:%s\nPhone:%s,\nCompany:%s,\nMessage:%s" % (
                name,
                email,
                text,
            phone,
            company,
            message)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')

    context={
        'service':service,
        'last':last
    }
    return render(request,'central/contact.html',context)


def product_detail(request,slug):
    service = Category.objects.all()[:4]
    last = Category.objects.all()[4:8]
    left = Blog.objects.all().order_by('?')
    right = Blog.objects.all().order_by('?')
    serviceinn = Category.objects.all()
    product = get_object_or_404(Category, slug=slug)

    if 'btnSubmit' in request.POST:
        if True:
            name = request.POST.get('name')
            email = request.POST.get('email')
            text = request.POST.get('text')

            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, "djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nText:%s" % (
                name,
                email,
                text,)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')

    context = {
        'product': product,
        'service': service,
        'left':left,
        'right':right,
        'serviceinn':serviceinn,
        'last':last
    }
    return render(request,'central/detail.html',context)



def about(request):
    service = Category.objects.all()[:4]
    last = Category.objects.all()[4:8]

    context = {
        'service': service,
        'last': last
    }
    return render(request,'central/about.html',context)