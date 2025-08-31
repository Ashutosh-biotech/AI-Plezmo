from django.contrib import admin
from django.urls import path
from plezmoapp import views
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views

admin.sites.AdminSite.site_header = 'Ashutosh Intelligence Admin'
admin.sites.AdminSite.site_title = 'Ashutosh Intelligence Admin'
admin.sites.AdminSite.index_title = 'Ashutosh Intelligence Admin'

urlpatterns = [
    path('admin/', admin.site.urls),

    # ? home page
    path('', views.home, name="home"),

    # ? register and login and loout
    path('log/in', views.user_login, name="signin"),
    path('log/in', views.user_login, name="login"),
    path('join/register', views.join, name="join"),
    path('<str:user_name>/logout', views.user_logout, name="logout"),

    # ? custom 404 page
    path('page_not_found/404/AI?url=unknown', views.bad_request, name="404"),

    # ? user profile
    path('<str:user_profile>/profile', views.profile, name="profile"),
    path('<str:user_profile_update>/update/profile', views.update_profile, name="update_profile"),

    # ? General Url
    path('user/<str:username>/creating/tag/input', views.tag_input, name="input_tag"),
    path('AI/projects', views.get_request, name="request"),

    # ? forgot password setting
    path('password_reset/',auth_views.PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # ? verifying email
    path('verify/', views.verify, name='Verify'),
    path('email/verify/<str:user>', views.VerifyEmail, name='VerifyEmail'),

    # ? blog
    path('blog', views.blog, name="blog"),
    path('blog/<str:slug>', views.blogPost, name="blog_post"),
    path('delete/post/', views.delete_post, name="delete_post"),
    path('postComment', views.postComment, name="postComment"),
    path('delete/comment/', views.delete_blogpost, name="delete_blogpost"),
    path('report', views.error, name="error"),
]

handler404 = views.file_not_found_404
