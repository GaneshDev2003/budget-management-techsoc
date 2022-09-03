from urllib import response
from django.shortcuts import render,redirect
from .models import ProjectModel, PurchaseModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProjectSerializer
# Create your views here.


class ProjectList(APIView):
    def get(self,request):
        projectsObj = ProjectModel.objects.all()
        serializedObj = ProjectSerializer(projectsObj, many = True)
        return Response(serializedObj.data)

def create_project_view(request):
    if(request.method == 'POST'):
        postData = request.POST
        title = postData['title']
        allocated = postData['allocated']
        project = ProjectModel.objects.create(
            title = title,
            allocated = allocated
        )
        project.save()
        return redirect('project_list')
    return render(request, 'create_project.html', context={})
def project_list_view(request):
    projects = ProjectModel.objects.all()
    return render(request, 'project_list.html', context = {
        'projects':projects
        })

def project_detail_view(request, project_id):
    project = ProjectModel.objects.get(pk = project_id)
    purchases = project.purchases
    if(request.method == 'POST'):
        postData = request.POST
        purchase = PurchaseModel.objects.create(
            name = postData['name'],
            quantity = postData['quantity'],
            price = postData['price'],
        )
        print(type(postData['price']))
        purchases.add(purchase)
        
        project.used_budget = float(project.used_budget) +  float(postData['price'])
        project.save()
    return render(request, 'project_detail.html', context = {
        'project':project,
        'purchases':purchases,
    })
def purchase_add_view(request, project_id):
    

    return render(request, 'project_detail.html',context = {})


