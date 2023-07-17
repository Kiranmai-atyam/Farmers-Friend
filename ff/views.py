from django.shortcuts import render,redirect
from django.contrib import messages
from django.http.response import HttpResponse
from django.http import HttpResponse
from ff.models import croprecomend
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request,'home.html')
def crops(request):
	return render(request,'crops.html')
def login(request):
	return render(request,'login.html')
def about(request):
	return render(request,'about.html')
def rice(request):
	return render(request,'rice.html')
def wheat(request):
	return render(request,'wheat.html')
def sugarcane(request):
	return render(request,'sugarcane.html')
def cotton(request):
	return render(request,'cotton.html')
def maize(request):
	return render(request,'maize.html')
def tea(request):
	return render(request,'tea.html')
def coffee(request):
	return render(request,'coffee.html')
def barley(request):
	return render(request,'barley.html')
def coconut(request):
	return render(request,'coconut.html')
def cashew(request):
	return render(request,'cashew.html')
def fruits(request):
	return render(request,'fruits.html')
def millets(request):
	return render(request,'millets.html')
def pulses(request):
	return render(request,'pulses.html')
def jowar(request):
	return render(request,'jowar.html')
def cereals(request):
	return render(request,'cereals.html')
def oilseeds(request):
	return render(request,'oilseeds.html')
def groundnut(request):
	return render(request,'groundnut.html')
def sunflower(request):
	return render(request,'sunflower.html')
def jute(request):
	return render(request,'jute.html')
def vegetables(request):
	return render(request,'vegetables.html')
def contact(request):
	return render(request,'contact.html')
def potato(request):
	return render(request,'potato.html')
def indexform(request):
	return render(request,'indexform.html')
def indexform(request):
	if request.method=="POST":
		prod=croprecomend()
		prod.soil=request.POST.get('soil',"Guest(or whatever)")
		prod.season=request.POST.get('season',"Guest(or whatever)")
		prod.crop=request.POST.get('crop',"Guest(or whatever)")
		if len(request.FILES)!=0:
			prod.image=request.FILES['image']
		prod.save()
		#croprecomend.objects.create(soil=so,season=sea,crop=cr,image=img)
		return HttpResponse("your data is submitted succesfully")
	return render(request,'indexform.html')
@login_required(login_url="/login/")
def video(request):
	return render(request,'video.html')
@login_required(login_url="/login/")
def croprecomendation(request):
	if request.method=="POST":
		soil=request.POST.get('soil')
		season=request.POST.get('season')
		searchcr=croprecomend.objects.filter(soil=soil ,season=season)
		return render(request,'index.html',{"data":searchcr})
	else:
		cropdisplay=croprecomend.objects.filter(id='0')
		return render(request,'index.html',{"data":cropdisplay})

def login(request):
	if request.method=='POST':
		usname = request.POST.get('usname',"Guest (or whatever)")
		pd = request.POST.get('pd',"Guest (or whatever)")

		user=auth.authenticate(username=usname,password=pd)

		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			messages.info(request,"invalid credentials")
			return redirect('login')
	else:
		return render(request,'login.html')
def register(request):
	if request.method =='POST':
		username = request.POST.get('username',"Guest (or whatever)")
		email = request.POST.get('email',"Guest (or whatever)")
		pword1 = request.POST.get('pword1',"Guest (or whatever)")
		pword2 = request.POST.get('pword2',"Guest (or whatever)")

		if(pword1==pword2):
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username is already existed')
				return redirect('login')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'email is already existed')
				return redirect('login')
			else:
				user=User.objects.create_user(username=username,email=email,password=pword1)
				user.save();
				print('User created')
				return redirect('login')
		else:
			messages.info(request,'password is not matching')
			print('pword not matching')
			return redirect('login')
		return redirect('home')

	else:
		return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('home')
def contact(request):
	return render(request,'contact.html')

	

        
    
