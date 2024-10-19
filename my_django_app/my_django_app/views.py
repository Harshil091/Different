from django.http import HttpResponse
import os
import time
import subprocess

def htop_view(request):
    name="Harshil"
    username=os.getlogin()
    server_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    top_output=subprocess.getoutput("top -b -n1")

    