"""
from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
   path('filter/',views.filter_form,name='filter_form'),
   path('edit/<int:student_id>',views.student_form,name='student_form'),
   path('result/',views.show_result,name='show_result'),
   path('add/',views.student_add,name='student_add'),
   path('delete/<int:student_id>',views.student_delete,name='student_delete'),
   path('view/<int:student_id>',views.student_view,name='student_view'),
   path('view/',views.view_students,name='view_students'),
   path('add/course/',views.course_add,name='course_add'),
<<<<<<< HEAD

]
"""
=======
   path('course_update/<int:student_id>/<int:course_id>/',views.course_data,name='course_data'),
]
>>>>>>> master
