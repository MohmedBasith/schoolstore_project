from django import forms

from . models import Department, Course


class CourseForm(forms.Form):

    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        widget=forms.Select(attrs={"hx-get": "/load_courses", "hx-target": "#id_course"}))
    course = forms.ModelChoiceField(queryset=Course.objects.none())

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['course'].queryset = Course.objects.none()
    #
    #     if 'department' in self.data:
    #         try:
    #             department_id = int(self.data.get('department'))
    #             self.fields['course'].queryset = Course.objects.filter(
    #                 country_id=department_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk and self.instance.department:
    #         self.fields['course'].queryset = self.instance.department.course_set.order_by(
    #             'name')
    #

