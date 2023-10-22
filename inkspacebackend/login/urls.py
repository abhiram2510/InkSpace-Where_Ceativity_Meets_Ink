#Importing modules for backend
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signIn, name= "signIn"),
    path('home/',views.home,name= "homepage"),
    path('signUp/',views.signUp,name = 'signUpPage'),
    path('signUp/signIn/',views.signIn,name = 'signInPage'),
    # path('signIn/signUp/',views.signUpPage,name = 'signUpPage'),
    path('display/', views.display, name= "display"),
    path('viewFullBlog/',views.viewFullBlog,name="viewFullBlog"),
    path('addBlog/',views.addBlog, name="addBlog"),
    path('blog_detail/<slug>',views.blog_detail,name="blog_detail"),
    path('view_blog/',views.view_blog,name="view_blog"),
    path('blog_delete/<id>',views.blog_delete,name="blog_delete"),
    path('blog_update/<slug>',views.blog_update,name="blog_update"),
    path('logout_view/',views.logout_view,name="logout_view")
]

