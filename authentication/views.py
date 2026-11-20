from django.contrib.auth import login
from django.shortcuts import redirect, render

from authentication.forms import SignupForm


def signup_view(request):
    """Inscrit un nouvel utilisateur puis le connecte."""
    if request.user.is_authenticated:
        return redirect('flux')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flux')
    else:
        form = SignupForm()

    return render(request, 'authentication/signup.html', {'form': form})
