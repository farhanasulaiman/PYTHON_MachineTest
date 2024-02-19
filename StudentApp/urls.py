from django.urls import path

from StudentApp import views, admin_views, student_views, api_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('mylogin',views.login_view,name='mylogin'),
    path('mylogout',views.logout_view,name='mylogout'),
    path('adminreg',views.register_admin,name='adminreg'),
    path('studreg',views.register_stud,name='studreg'),
    path('adminhome',views.admin_home,name='adminhome'),
    path('studhome',views.stud_home,name='studhome'),
    path('studlist',admin_views.view_stud,name='studlist'),
    path('updtstud/<int:id>/',admin_views.updt_stud,name='updtstud'),
    path('addmarks',admin_views.add_marks,name='addmarks'),
    path('markslist',admin_views.view_marks,name='markslist'),
    path('updtmarks/<int:id>/',admin_views.updt_marks,name='updtmarks'),
    path('delmarks/<int:id>/',admin_views.del_marks,name='delmarks'),
    path('myprofile',student_views.view_profile,name='myprofile'),
    path('updtprofile',student_views.updt_profile,name='updtprofile'),

    path('studentlist', api_views.f_studentlist, name='studentlist'),
    path('studentrecord/<int:id>/', api_views.f_studentrecord, name='studentrecord')

]
