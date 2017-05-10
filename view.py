from django.http import HttpResponse
import json
import database

def hello(request):
    return HttpResponse("Hello world ! ")

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
    return HttpResponse(python_to_json)

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
    return HttpResponse(python_to_json)
