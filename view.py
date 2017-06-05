from django.http import HttpResponse
import json
from django.shortcuts import render
import database

def hello(request):
    return HttpResponse("Hello world ! ")

def get_total(request):
    mydatabase=database.Database()
    new_list=mydatabase.read_total_data()
    total=[]
    for i in new_list:
         new_dict={}
         new_dict['repo']=i[1]
         new_dict['name']=i[0]
         total.append(new_dict)
    python_to_json=json.dumps(total,ensure_ascii=False)
    response=HttpResponse(python_to_json)
    response['Access-Control-Allow-Origin']="*"
    return response

def get_languages(request):
    mydatabase=database.Database()
    new_list=mydatabase.read_languages_data()
    languages=[]
    for i in new_list:
         new_dict={}
         new_dict['repo']=i[1]
         new_dict['language']=i[0]
         languages.append(new_dict)
    python_to_json=json.dumps(languages,ensure_ascii=False)
    response=HttpResponse(python_to_json)
    response['Access-Control-Allow-Origin']="*"
    return response

def get_locations(request):
    mydatabase=database.Database()
    new_list=mydatabase.read_locations_data()
    locations=[]
    for i in new_list:
         new_dict={}
         new_dict['repo']=i[1]
         new_dict['location']=i[0]
         locations.append(new_dict)
    python_to_json=json.dumps(locations,ensure_ascii=False)
    response=HttpResponse(python_to_json)
    response['Access-Control-Allow-Origin']="*"
    return response

def get_repositories(request):
    mydatabase=database.Database()
    new_list=mydatabase.read_repositories_data()
    repositories=[]
    for i in new_list:
         new_dict={}
         new_dict['repo']=i[1]
         new_dict['year']=i[0]
         repositories.append(new_dict)
    python_to_json=json.dumps(repositories,ensure_ascii=False)
    response=HttpResponse(python_to_json)
    response['Access-Control-Allow-Origin']="*"
    return response

def get_starts(request):
    mydatabase=database.Database()
    new_list=mydatabase.read_projects_data()
    repositories=[]
    for i in new_list:
         new_dict={}
         new_dict['id']=i[0]
         new_dict['repo_name']=i[1]
         new_dict['repo_url']=i[2]
         new_dict['stargazers_count']=i[3]
         new_dict['user_login']=i[4]
         new_dict['user_url']=i[5]
         repositories.append(new_dict)
    python_to_json=json.dumps(repositories,ensure_ascii=False)
    response=HttpResponse(python_to_json)
    response['Access-Control-Allow-Origin']="*"
    return response
