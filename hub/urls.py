from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("courses", views.course_list_view, name="coursesList"),
    path("courses/join/<int:course_id>", views.course_join, name="courseJoin"),
    path("course/create", views.course_create, name="courseCreate"),
    path("course/<int:id>", views.course_view, name="course"),
    path("course/<int:course_id>/leave", views.course_leave, name="courseLeave"),
    path("course/<int:course_id>/assignment/<int:post_id>", views.course_assignment, name="assignment"),
    path("course/<int:course_id>/assignment/<int:post_id>/delete", views.assignment_delete_file, name="deleteAssignment"),
    path("course/<int:id>/forum", views.course_forum, name="courseForum"),
    path("course/<int:id>/students", views.course_students, name="courseStudents"),
    path("grades", views.grades_view, name="grades"),
    path("course/<int:course_id>/assign", views.assign_grades_view, name="assignGrades")
]