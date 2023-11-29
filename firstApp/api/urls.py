from django.urls import path
from . import views

urlpatterns = [
    path("student/<int:id>", view=views.singleStudent, name="single_student"),
    path("allstudent", view=views.student_query)
]
