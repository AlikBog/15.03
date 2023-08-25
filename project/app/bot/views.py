from django.shortcuts import render
# import os
# import environ
 
 
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
# # reading .env file
# environ.Env.read_env()
 
# # Create your views here.
 
# def index(request):
 
#     return render(
#         request,
#         'index.html',
#         context={'variables': os.environ}
#     )
 
 
# def environ(request):
 
#     variable_env = env('HELLO')
#     return render(
#         request,
#         'environ.html',
#         context={'variable': variable_env}
#     )
