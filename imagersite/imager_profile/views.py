"""Views."""

from django.shortcuts import render
from django.contrib.auth.models import User


def home_view(request, page='Home'):
    """View that returns homepage view."""

    context = {'page': page}
    return render(request, 'imager_profile/home.html', context=context)


def login_view(request, page='Login'):
    """View that returns login view."""

    if request.method == 'GET':
        context = {'page': page}
        return render(request, 'imager_profile/login.html', context=context)
    elif request.method == 'POST':
        from django.contrib.auth import authenticate

        unicode_request = request.body.decode('utf8')
        username = unicode_request.split('&')[1].split('=')[1]
        password = unicode_request.split('&')[2].split('=')[1]

        user = authenticate(username=username, password=password)

        if user is not None:
            from django.shortcuts import redirect
            import imagersite.settings
            return redirect(imagersite.settings.LOGIN_REDIRECT_URL)
        else:
            pass


def register_view(request, page='Register'):
    """View that returns login view."""
    from imager_profile.forms import EmailRegistrationForm
    from django.shortcuts import render, redirect
    from django.contrib.sites.shortcuts import get_current_site
    from django.utils.encoding import force_bytes
    from django.utils.http import urlsafe_base64_encode
    from django.template.loader import render_to_string
    from imager_profile.tokens import account_activation_token

    if request.method == 'POST':
        form = EmailRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('imager_profile/user_activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return render(request, 'imager_profile/activation_sent.html')
    else:
        form = EmailRegistrationForm()
    return render(request, 'imager_profile/register.html', {'form': form, 'page': page})


def activate(request, uidb64, token):
    """View that checks user activation token."""
    from django.contrib.auth import login
    from django.contrib.auth.models import User
    from django.shortcuts import render, redirect
    from django.utils.encoding import force_text
    from django.utils.http import urlsafe_base64_decode
    from imager_profile.tokens import account_activation_token

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'imager_profile/activation_invalid.html')


def activation_sent_view(request):
    """View that displays when activation has been sent."""
    return render(request, 'imager_profile/activation_sent.html')


def profile_view(request):
    """View for user profile."""
    if request.is_authenticated():
        return render(request, 'imager_profile/profile.html')
