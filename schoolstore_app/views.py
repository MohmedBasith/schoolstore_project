from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . forms import CourseForm
from schoolstore_app.models import Department, Course


# Create your views here.


def allCourse(request, c_slug=None):
    c_page = None
    course_list = None

    if c_slug != None:
        c_page = get_object_or_404(Department, slug=c_slug)
        course_list = Course.objects.all().filter(department=c_page, available=True)
    else:
        course_list = Course.objects.all().filter(available=True)
    paginator = Paginator(course_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        courses = paginator.page(page)
    except (EmptyPage, InvalidPage):
        courses = paginator.page(paginator.num_pages)

    return render(request, 'department.html', {'department': c_page, 'courses': courses})


def courseDetail(request, c_slug, course_slug):
    try:
        course = Course.objects.get(department__slug=c_slug, slug=course_slug)
    except Exception as e:
        raise e
    return render(request, 'course.html', {'course': course})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('form/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login/')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is already taken')
                return redirect('register/')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login/')
            print("Successfully created user")
        else:
            messages.info(request, "Incorrect Password")
            return redirect('register/')
        return redirect('/')
    return render(request, "register.html")


def form(request):
    form = CourseForm()
    return render(request, "form.html", {"form": form})


def load_courses(request):
    department_id = request.GET.get("department")
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return render(request, "course_options.html", {"courses": courses})


def submit(request):
    if request.method == 'POST':
        return redirect('/')
    return render(request, 'submit.html')

