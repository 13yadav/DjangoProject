from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Q
from products.models import Phone, Laptop, Feedback


def home(request):
    return render(request, 'home.html', {})


def phones(request):
    phone = Phone.objects.all().order_by('-date_added')
    return render(request, 'phone.html', {'phone': phone})


def laptops(request):
    laptop = Laptop.objects.all().order_by('-date_added')
    return render(request, 'laptop.html', {'laptop': laptop})


def ph_detail(request, phone_id):
    detail = get_object_or_404(Phone, ph_id=phone_id)
    return render(request, 'ph_detail.html', {'ph_detail': detail})


def lap_detail(request, laptop_id):
    detail = get_object_or_404(Laptop, lap_id=laptop_id)
    return render(request, 'lap_detail.html', {'lap_detail': detail})


def allproducts(request):
    phone = Phone.objects.all().order_by('-date_added')[0:4]
    laptop = Laptop.objects.all().order_by('-date_added')[0:4]
    all = {
        'phone': phone,
        'laptop': laptop,
    }

    return render(request, 'all.html', all)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q').strip()

        if query is not None:
            ph_q = Q(brand_name__contains=query) | Q(
                model__contains=query)
            lap_q = Q(brand_name__contains=query) | Q(
                model__contains=query)

            result1 = Phone.objects.filter(ph_q).distinct()
            result2 = Laptop.objects.filter(lap_q).distinct()

            context = {'result1': result1, 'result2': result2}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken...')
            return redirect(reverse('account:register'))

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already registered...')
            return redirect(reverse('account:register'))

        else:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            user.save()
            messages.info(request, 'User Created Successfully...')
        return redirect(reverse('account:login'))

    else:
        return render(request, 'register.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('homepage'))
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect(reverse('account:login'))

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('homepage'))


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        feedback = request.POST['name']

        feed = Feedback(name=name, email=email, feedback=feedback)
        feed.save()
        messages.info(request, 'Thank You, for your feedback!')

        return render(request, 'feed.html')
