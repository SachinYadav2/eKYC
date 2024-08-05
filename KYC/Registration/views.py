
from django.shortcuts import render
import logging
import os
from .forms import registerform
from django.http import HttpResponse


string_format = "[ %(asctime)s: %(levelname)s : %(module)s]: %(message)s"
log_dir = "Logs_file"
from .models import register
logging.basicConfig(filename=os.path.join(log_dir , 'ekyc_logs.log') , level=logging.INFO , format=string_format , filemode="a")

def Register(request):

    # Log save Start
    logging.info("Your Regirster Function is call now")

    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            logging.info("Your data is Enter ")

            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            mobile = request.POST['mobile']
            place = request.POST['place']

            logging.info(f"name:{first_name} last_name:{last_name} place :{place} mobile {mobile}")

            # Check the data user alreayd exits or not
            if register.objects.filter(mobile=mobile).exists():
                logging.info("This Mobile No user already inside the database !")
                return render(request , 'Registration/registration.html')
            else:


                instance = register(first_name=first_name , last_name=last_name , mobile=mobile ,place=place)
                instance.save()
                logging.info("Your Information is Succesfully save okk")
                return HttpResponse ("Login Page Welcome !")





    else:

        return render(request , 'Registration/registration.html')