from django.shortcuts import render
from django.shortcuts import HttpResponse
import os
import logging

# Create your views here.



string_format = "[ %(asctime)s: %(levelname)s : %(module)s]: %(message)s"
log_dir = "Logs_file"
logging.basicConfig(filename=os.path.join(log_dir , 'ekyc_logs.log') , level=logging.INFO , format=string_format , filemode="a")


def Dash(request):
    logging.info("Your Dashbooard Page Function Call is Name is Dash")
    return render(request , "first.html")
