# SchoolHub
## preview
https://www.youtube.com/watch?v=QshT_inJXpQ

## Distinctiveness and Complexity
This project is distinct from all other projects done during the course. The idea of this website is to serve as a comprehensive platform that brings together students and teachers, offering a variety of features, such as: forums for the participants of each course; grading system available for teachers; posts for the courses(regular posts and assignment type of post, where the students can submit their work as files) and possibility to join new courses available and leave them and even creating new courses. I wanted to make a website where you can have direct acess to communities focused on education. Furthermore, the website is responsive for multiple screensizes and mobile responsive. It brings together some features that are simmiliar to other projects, but I tried to make them as distinct as possible and also writing the code almost completly from scratch.

## Structure:
The project is structured as follow:

### Capstone folder
* __init__.py
* asgi.py: ASGI config for capstone project.
* setting.py: Django settings for capstone project.
* urls.py: capstone URL Configuration

 ### Hub folder:  main project folder
* __init__.py:
* admin.py: models registration to admin site
* apps.py: Configuration of the Hub app
* forms.py: model to be able to create file forms
* models.py: all the models of the hub app
* tests.py: 
* urls.py: all urls of the hub app
* views.py: all views of the hub app
* /static/css/course.css: course page style and subsequent pages
* /static/css/style.css: first page css style
#### templates folder:
* assignGrades.html: assignment of grades (for professors) template
* assignment.html: assignment posts details template
* course.html: course overview page template
* coursesAvailable.html: all courses available page template
* createCourse.html: create a new course page template
* forum.html: course forum page template
* grades.html: visualize grades page template
* index.html: initial page of the site (view coursers subscribed) template
* layout.html: layout of the page (side menu and navbar) template
* login.html: login page template
* register.html: register page template
* students.html: list of students of the course template

### /media/uploads folder
* all documents added by users

### uploads folder
* uploads by users



## how to run
No need for any other package (besides the packages needed for the course. Only thing necessary is Python3 and Django).

Run these commands on the terminal:

ˋˋˋ 
python manage.py makemigrations hub

python manage.py migrate

python manage.py runserver
ˋˋˋ 
