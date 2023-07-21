from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Courses,sub_Courses
from .forms import CoursesForm, Sub_Course_Form
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView


def Homepage(request):
    return render(request, 'training_app/home.html', {})

def our_courses(request):
    course_list = Courses.objects.all()
    p = Paginator(Courses.objects.all(), 2)  # 2 per page
    page = request.GET.get('page')
    courses = p.get_page(page)
    nums = "a" * courses.paginator.num_pages  # a is just any string. you can use any letter
    # when a is multiplied it will give us a string of e.g aaaa which will be counted by forloops
    return render(request, 'training_app/our-courses.html', {
        'course_list': course_list,
        'courses': courses,
    })

def course_detail(request):
    return render(request, 'training_app/courses-details.html', {})

def Tab_page(request):
    render(request, 'training_app/testpage.html', {'active_tab':'demo-lft-tab-5'})

class CourseView(ListView):
    model = Courses
    template_name = "training_app/courses.html"

class Add_Course(CreateView):
    model = Courses
    form_class = CoursesForm
    template_name = 'training_app/add_course.html'

# class Update_Course(UpdateView):
#     model = Courses
#     form_class = CoursesForm
#     template_name = 'training_app/update_course.html'

def Update_Course(request, course_id):
    course = Courses.objects.get(pk=course_id)
    form = CoursesForm(request.POST or None, instance=course)  #  // instance will fill out the form texts with values
    if form.is_valid():
        form.save()
        return redirect('our-courses')
    return render(request, 'training_app/update_course.html', {
        'course': course,
        'form': form
    })

class Delete_Course(DeleteView):
    model = Courses
    template_name = 'training_app/delete_course.html'
    success_url = reverse_lazy('our-courses')

class Add_Sub_Course(CreateView):
    model = sub_Courses
    form_class = Sub_Course_Form
    template_name = 'training_app/add_sub_course.html'

class ViewSubCourses_all(ListView):
    model = sub_Courses
    template_name = 'training_app/view_sub_course_all.html'

class ViewSubCourses_all2(ListView):
    model = sub_Courses
    template_name = 'training_app/view_sub_course.html'

class Read_Sub_Course(DetailView):
    model = sub_Courses
    template_name = 'training_app/read_sub_course.html'

class Update_Sub_Course(UpdateView):
    model = sub_Courses
    form_class = Sub_Course_Form
    success_message = "Updated"
    template_name = 'training_app/update_sub_course.html'

class Delete_Sub_Course(DeleteView):
    model = sub_Courses
    template_name = 'training_app/delete_sub_course.html'
    success_message = "Sub Course Deleted Successfully"
    success_url = reverse_lazy('view_sub_course_all')

def Read_Sub_Course2(request, id): # note the additional id parameter
    band = sub_Courses.objects.get(id=id) #we get the course with that id
    return render(request, 'training_app/read_sub_course.html', {
        'band': band})  # we pass this to the template

def Course_Category_View(request, cats):
    course_category = sub_Courses.objects.filter(course=cats)
    return render(request, 'training_app/view_sub_course.html', {
        'cats': cats.title(),
        'course_category': course_category})

def Show_Sub_Courses(request, course_id):
    courses = Courses.objects.get(pk=course_id)
    subcourses = courses.sub_courses_set.all()
    return render(request, 'training_app/view_sub_course.html', {
        'subcourses': subcourses,
        'courses': courses
    })



