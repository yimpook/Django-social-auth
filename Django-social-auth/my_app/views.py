from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# def home(request):
#     home = "Hello "
#     t = get_template("homeGoogle.html")
#     html = t.render(Context({'home':home}))
#     return HttpResponse(html)

from django.shortcuts import render
import social.apps.django_app.default.models as sm
from django.contrib.auth import authenticate, login, logout
def home(request):
		uname=""
		if request.method == 'POST' and 'submit' in request.POST:
				submit = request.POST['submit']
 				if submit=="sign-out":
					logout(request)
		if '_auth_user_id' in request.session:
				uname=sm.UserSocialAuth.objects.get(
					user_id=int(request.session['_auth_user_id'])
					).user
		return render(request,'home.html',{'uname': uname})



