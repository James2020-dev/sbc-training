from django.contrib import admin
from django.urls import path,include
from .views import CourseView, Add_Course, Update_Course,Delete_Course,Add_Sub_Course,ViewSubCourses_all, Update_Sub_Course,Delete_Sub_Course,ViewSubCourses_all2
from .import views

urlpatterns = [
    path('', views.Homepage, name='home'),
    path('courses', CourseView.as_view(), name='courses'),
    path('add_course', Add_Course.as_view(), name='add_course'),
    path('our_courses', views.our_courses, name='our-courses'),
    path('course_detail', views.course_detail, name='course-detail'),
    path('test_page', views.Tab_page, name='test_page'),
    # path('training/edit<int:pk>', Update_Course.as_view(), name='update_course'),
    path('update_course/<course_id>', views.Update_Course, name='update_course'),
    path('training/delete/<int:pk>/remove', Delete_Course.as_view(), name='delete_course'),
    path('training/', Add_Sub_Course.as_view(), name='add-sub-course'),
    path('view_sub_course/', ViewSubCourses_all.as_view(), name='view_sub_course_all'),
    path('sub_course/edit/<int:pk>', Update_Sub_Course.as_view(), name='update_sub_course'),
    path('sub_course/delete/<int:pk>', Delete_Sub_Course.as_view(), name='delete_sub_course'),
    path('bands/<int:id>/', views.Read_Sub_Course2, name='read_sub_course'),
    path('course_category2/<int:pk>/', views.ViewSubCourses_all2.as_view(), name='course_category'),
    path('categories/<str:cats>/', views.Course_Category_View, name='view_based_on_category'),
    path('sub_courses/<course_id>', views.Show_Sub_Courses, name='sub_courses3')

]
