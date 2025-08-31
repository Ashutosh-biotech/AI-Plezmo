from django.shortcuts import render, redirect
from .models import user_data, appdatabase, requested_app, BlogComment, Post, message
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from plezmo import settings
from random import randint
from django.core.mail import send_mail


def home(request):
    if request.user:
        try:
            userdata = user_data.objects.get(username=request.user.username)
            logo = {"pic": userdata.logo}
            return render(request, "index.html", logo)
        except user_data.DoesNotExist:
            userdata = None
    return render(request, "index.html")


def user_login(request):
    if request.method == "POST":
        user_name = request.POST["username"]
        key = request.POST["user_password"]
        user = authenticate(username=user_name, password=key)
        if user is not None:
            login(request, user=user)
            verified = user_data.objects.get(username=user_name)
            if verified.verified == "False":
                messages.warning(request, "Your Email is not Verified")
                logout(request)
                return redirect("Verify")
            messages.success(request, "Succesfully login!")
            return redirect("home")
        else:
            messages.error(
                request,
                "Please enter the correct username and password for a your account. Note that both fields are very case-sensitive.",
            )
            return redirect("login")
    else:
        return render(request, "login.html")


def join(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("useremail")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("password_repeat")
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeric = "1234567890"
        if name[0].isalpha():
            for i in range(1, 27):
                if name[0].upper() == alpha[i - 1]:
                    num = f"A ({i})"
                    break
                else:
                    num = 0

        elif name[0].isnumeric():
            for i in range(1, 11):
                if name[0] == numeric[i - 1]:
                    num = f"N ({i})"
                    break
                else:
                    num = 0

        else:
            num = "D"

        try:
            AI_user = User.objects.get(email=email)
            messages.warning(request, "This email is already in use")
            return redirect("join")
        except:
            if pass1 == pass2 and len(pass1) >= 8 and len(email) < 150:
                otp = randint(10000000, 99999999)
                status = send_mail(
                    "Email verification From AI",
                    f"""Hello {name},\nThis is to inform you that, this is not sended to you for your email verification i.e. You have given us a true email address about your self or fake.\nYour verification otp : {otp}.\nPlease don,t share your otp with others.(Reccommended)\nThank You""",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                user = User.objects.create(username=name, email=email)
                user.set_password(pass1)
                auth = user_data.objects.create(
                    username=name,
                    email=email,
                    logo=f"/assets/img/svg/{num}.svg",
                    one_time_password=otp,
                )
                auth.save()
                user.save()

                if status:
                    messages.success(
                        request,
                        "Congratulation, you are register. Verify your Email, then get full access.",
                    )
                    return redirect("Verify")
                else:
                    messages.error(
                        request,
                        "Something wents wrong! Please try again later",
                    )
                    return redirect("join")
            else:
                messages.warning(
                    request,
                    "Might be password is not matched or length of password is less than 8. ",
                )
                return redirect("join")
    else:
        return render(request, "registration.html")


def file_not_found_404(
    request, exception, template_name="404.html"
):  # ! custom 404 views
    return render(request, "404.html")


def user_logout(request, user_name):
    if request.user.username == user_name:
        logout(request)
        messages.success(
            request, "Thanks for spending some quality time with the Web site today."
        )
        return redirect("login")
    else:
        return redirect("404")


def get_request(request):
    params = {
        "app_data": appdatabase.objects.all(),
        "requested_app": requested_app.objects.all(),
    }
    if request.method == "POST":
        app_name = request.POST["appname"]
        desc = request.POST["desc"]
        app = requested_app.objects.create(
            username=request.user, app_name=app_name, app_desc=desc
        )
        app.save()
        messages.success(request, "Request sended successfully!")
        return redirect("request")
    elif request.user.is_authenticated:
        try:
            userdata = user_data.objects.get(username=request.user.username)
            params = {
                "app_data": appdatabase.objects.all(),
                "requested_app": requested_app.objects.all(),
                "pic": userdata.logo,
            }
        except user_data.DoesNotExist:
            userdata = None
    return render(request, "faq.html", params)


def profile(request, user_profile):
    if request.user.username == user_profile:
        user_details = {"profile": user_data.objects.get(username=user_profile)}
        return render(request, "profile.html", user_details)
    else:
        return redirect("404")


def update_profile(request, user_profile_update):
    if request.method == "POST":
        if request.user.username == user_profile_update:
            if User.objects.get(username=user_profile_update):
                pro = user_data.objects.get(username=user_profile_update)
                gender = request.POST.get("select")
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                _pro_ = User.objects.get(username=user_profile_update)
                if gender == "male":
                    pro.gender = 1
                if gender == "female":
                    pro.gender = 2
                if gender == "other":
                    pro.gender = 3
                pro.last_name = _pro_.last_name = last_name
                pro.first_name = _pro_.first_name = first_name
                pro.save()
                _pro_.save()
                messages.success(
                    request,
                    "Congratulation! Your profile has been changed successfully",
                )
                return redirect(f"/{ request.user.username }/profile")
            else:
                return redirect("404")
        else:
            return redirect("404")
    else:
        return redirect("404")


def bad_request(request):
    return render(request, "404.html")


def tag_input(request, username):
    if request.user.username == username:
        return render(request, "code.html")
    else:
        return redirect("404")


def VerifyEmail(request, user):
    if request.method == "POST":
        user_name = request.POST["username"]
        key = request.POST["user_password"]
        otp = request.POST["user_otp"]
        user = authenticate(username=user_name, password=key)
        if user is not None:
            login(request, user=user)
            verified = user_data.objects.get(username=request.user.username)
            if verified.one_time_password == int(otp):
                pass
            else:
                logout(request)
                messages.error(request, "Otp is wrong")
                return redirect("Verify")

            if verified.verified == "False":
                verified.verified = "True"
                verified.one_time_password = 1032004020130716
                verified.save()
                messages.success(request, "Your Email is Verified, Succesfully login!")
                return redirect("home")
            else:
                messages.info(request, "Your Email is already Verified")
                return redirect("home")
        else:
            messages.error(
                request,
                "Email verification failed due to wrong username and password. Please Try Again Later.",
            )
            return redirect("Verify")
    else:
        return redirect("404")


def verify(request):
    return render(request, "confirm_template.html")


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    if post:
        try:
            userdata = user_data.objects.get(username=request.user.username)
            comments = BlogComment.objects.filter(post=post)
            context = {"post": post, "comments": comments, "user": request.user, "pic": userdata.logo}
            return render(request, "blog-post.html", context)
        except:
            comments = BlogComment.objects.filter(post=post)
            context = {"post" :post,"comments" : comments, "user":request.user}
            return render(request, "blog-post.html", context)
    else:
        return redirect("404")


def blog(request):
    if request.method == "POST":
        comment = request.POST.get("content")
        user = request.user
        title = request.POST.get("title")
        image = user_data.objects.get(username=request.user.username)
        post = Post(title=title, content=comment, author=user, slug=title, logo=image.logo)
        post.save()
        return redirect("blog")
    else:
        if request.user:
            try:
                userdata = user_data.objects.get(username=request.user.username)
                context = {"allPosts": Post.objects.all(), "pic": userdata.logo}
                return render(request, "blog.html", context)
            except user_data.DoesNotExist:
                userdata = None
        context = {"allPosts": Post.objects.all()}
        return render(request, "blog.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        image = user_data.objects.get(username=request.user.username)
        comment = BlogComment(comment=comment, user=user, post=post, logo=image.logo)
        comment.save()

    return redirect(f"/blog/{post.slug}")


def delete_post(request):
    try:
        if request.method == "POST":
            sno = request.POST.get("sno")
            if Post.objects.get(sno=sno, author=request.user):
                val = Post.objects.get(sno=sno)
                val.delete()
            return redirect("blog")
        else:
            return redirect("404")
    except:
        return redirect("404")


def delete_blogpost(request):
    try:
        if request.method == "POST":
            sno = request.POST.get("sno")
            if BlogComment.objects.get(sno=sno, user=request.user):
                val = BlogComment.objects.get(sno=sno)
                val.delete()
            return redirect("blog")
        else:
            return redirect("404")
    except:
        return redirect("404")


def error(request):
    if request.method == "POST":
        error_to = request.POST.get("error_to")
        error_from = request.POST.get("error_from")
        error = request.POST.get("error")
        val = message(error=error, error_from=error_from, error_to=error_to)
        val.save()
        messages.success(request, "Thank you for your report")
        return redirect("blog")
    else:
        return redirect("404")
