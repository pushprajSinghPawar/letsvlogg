from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
path('home', views.index, name="blog"),
path('userlogin',views.userlogin,name="userloginlogin"),
path('signup',views.signup,name="signup"),
path('faqs',views.faqs,name="faqs"),
path('donations',views.donation,name="donation"),
path('about',views.about,name="about"),
path('aboutblogs',views.aboutblogs,name="aboutblogs"),
path('topbloggers',views.topbloggers,name="topbbloggers"),
path('blogbeforeview/<int:myid>',views.blogbeforeview,name="blogbeforeview"),
path('contact',views.contact_view,name="contact"),
path('search',views.search,name="search"),
path('feed',views.feed,name="feed"),

path('handle_sign_up',views.handle_sign_up,name="handle_sign_up"),
path('accopen',views.accopen,name="accopen"),
path('accclose',views.accclose,name="accclose"),
path('postablog',views.postablog,name="postablog"),

#this is end we die after this
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)