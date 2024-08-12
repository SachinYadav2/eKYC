import logging.config
from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse

import logging
import os

string_format = "[ %(asctime)s: %(levelname)s : %(module)s]: %(message)s"
log_dir = "Logs_file"
logging.basicConfig(filename=os.path.join(log_dir , 'ekyc_logs.log') , level=logging.INFO , format=string_format , filemode="a")

# Create your views here.
from  Registration.models import register

def Login(reuqest):
    logging.info("Your Login Page Function is Call")

    if reuqest.method == "POST":
        name = reuqest.POST['name']
        mobile = reuqest.POST['mobile']
        if register.objects.filter(mobile=mobile).exists():
            logging.info("Your All Information is Right and now Your Dashboard Page is call or show")
            return redirect("Dashboard:Dash")
        
        else:
            logging.info("Your Are Give Some miss Infromation please check it user by user ! or user are un Register Person")


            return redirect("Registration:Register")
    

    return render(reuqest,"Login/Login_first.html")