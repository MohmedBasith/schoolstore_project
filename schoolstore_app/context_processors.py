from . models import Department, Course


def menu_links(request):
    links=Department.objects.all()
    return dict(links=links)


def menu_links2(request):
    links1=Course.objects.all()
    return dict(links1=links1)
