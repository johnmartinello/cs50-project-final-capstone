import json
import logging
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest, HttpResponseServerError
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Course, User, Grade, Post, Forum, Assignment
from .forms import UploadFileForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    
    user = request.user
    
    if user.is_authenticated:
        course = Course.objects.all()
        
        user_course = course.filter(students=user)
        
    else:
        user_course = None
    
    return render(request, "index.html",{
       "user": user,
       "courses": user_course,
    })


@login_required(login_url='login')
def course_list_view(request):
    user = request.user
    courses = Course.objects.exclude(students=user)
    
    return render(request, "coursesAvailable.html",{
       "user": user,
       "courses": courses,
    })


@login_required(login_url='login')
def course_join(request, course_id):
    user = request.user
    courses = Course.objects.exclude(students=user)
    course = Course.objects.get(id=course_id)
    
    if user in course.students.all():
        return render(request, "coursesAvailable.html",{
       "user": user,
       "courses": courses,
       "error": "You are already in this course"
    })
    
    course.students.add(user)
    course.save()
    
    return HttpResponseRedirect(reverse("course", args=[course_id]))


@login_required(login_url='login')
def course_leave(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    course.students.remove(user)
    
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='login')
def course_create(request):
    user = request.user

    if request.method =="POST":
        subject = request.POST["subject"]
        code = request.POST["code"]
        level = request.POST["level"]
        program = request.POST["program"]
        
        create_course = Course(
            subject = subject,
            code = code,
            level = level,
            professor= user,
            program = program
        )
        create_course.save()
        create_course.students.set([user])
        
        course_id = create_course.id
        
        return HttpResponseRedirect(reverse("course", args=[course_id]))
    
    else:
        return render(request,"createCourse.html", {
            "user": user
        })


@login_required(login_url='login')
def course_view(request, id):
    user = request.user
    course_id = get_object_or_404(Course, pk=id)
    courses = Course.objects.all()
    course_professor = courses.filter(professor=user)
    posts = Post.objects.filter(course=course_id).order_by('-timestamp')
    form = UploadFileForm()
    
    if request.method == "POST":
        content = request.POST.get("addPost", "")
        
        #checks if the checkbox receives a value and convert to boolean according
        if "checkbox" in request.POST:
            checkbox = True
        else:
            checkbox = False
        
        #retrieve the UploadFileForm class from the forms.py file (needed to be able to create a form for files)
        form = UploadFileForm(request.POST, request.FILES)
        filec = request.FILES.get('filec')
        
        addPost = Post(
            creator=user,
            content=content,
            course=course_id,
            filec=filec,
            assignment=checkbox
        )
        addPost.save()
        return HttpResponseRedirect(reverse("course", args=[id]))
    else:
        return render(request, "course.html", {
            "user": user,
            "course": course_id,
            "posts": posts,
            "form": form,
            "professor": course_professor,
        })
        
        
@login_required(login_url='login')
def course_assignment(request,course_id, post_id):
    user=request.user
    course = get_object_or_404(Course, pk=course_id)
    post = get_object_or_404(Post, pk=post_id)
    form = UploadFileForm()
    
    #checks if the user is the course professor (view change depending on this factor)
    if user == course.professor:
        assignment = Assignment.objects.filter(post=post).order_by('-timestamp')
    else:
        assignment = Assignment.objects.filter(post=post).first()
 
    if request.method == "POST":  
        form = UploadFileForm(request.POST, request.FILES)
        filec = request.FILES.get('filec')
        
        add_assignment = Assignment(
            post = post,
            student = user,
            filec = filec,
            course=course
        )
        add_assignment.save()
        return HttpResponseRedirect(reverse("assignment", args=[course_id,post_id]))
    
    return render(request, 'assignment.html', {
        'user': user,
        'course_id': course,
        'post': post,
        "form": form,
        "assignment": assignment,  
        })
        
        
@login_required(login_url='login')
def assignment_delete_file(request, course_id, post_id):
    user = request.user
    post = get_object_or_404(Post, pk=post_id)
    assignment = Assignment.objects.filter(post=post, student=user).first()

    if assignment and request.method == "POST":
        assignment.delete()
    
    return HttpResponseRedirect(reverse("assignment", args=[course_id,post_id]))
 

@login_required(login_url='login')
def course_forum(request,id):
    user = request.user
    course_id = get_object_or_404(Course, pk=id)
    comments = Forum.objects.filter(course=course_id)
    
    if request.method == "POST":
        content = request.POST["addComment"]
        addComment = Forum(
            creator = user,
            content = content,
            course = course_id
        )
        addComment.save()
        return HttpResponseRedirect(reverse("courseForum", args=[id]))
   
    else:
        return render(request, "forum.html", {
            "user": user,
            "course": course_id,
            "comments": comments,
        })


@login_required(login_url='login')    
def course_students(request,id):
    user = request.user
    course_id = get_object_or_404(Course, pk=id)
    students = course_id.students.all()
    
    return render(request, "students.html", {
        "user": user,
        "course": course_id,
        "students": students,
    })
    

@login_required(login_url='login') 
def grades_view(request):
    user = request.user
    course = Course.objects.all()
    user_course = course.filter(students=user)
    grades = Grade.objects.filter(student=user)
    return render(request, "grades.html", {
        "user": user,
       "grades": grades,
       "courses":user_course
    })


@login_required(login_url='login') 
def assign_grades_view(request, course_id):
    user = request.user
    course = get_object_or_404(Course, pk=course_id)
    students = course.students.all()
    
    if request.method == "POST":
        student_id = request.POST["student"] 
        grade = float(request.POST["grade"])
        student = User.objects.get(id=student_id)

        # Check if a grade already exists for the user and course
        existing_grade = Grade.objects.filter(student=student, course=course).exists()
        if existing_grade:
            return render(request, "assignGrades.html", {
                "user": user,
                "course": course,
                "students": students,
                "error_message": "A grade already exists for this user and course."
            })

        #to later assign if the student is going to fail the class or not
        if grade < 70.0:
            status = True
        else:
            status = False
            
        addGrade = Grade(
            student=student,
            course=course,
            grade=grade,
            is_failed=status
        )
        addGrade.save()
        return HttpResponseRedirect(reverse("assignGrades", args=[course_id]))
    
    else:
        return render(request, "assignGrades.html", {
            "user": user,
            "course": course,
            "students": students,
            
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


@login_required(login_url='register')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")
