from urllib import response
from django.shortcuts import render
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
        project = ProjectModel.object.create(
            title = title,
            allocated = allocated
        )
        project.save()
    return render(request, 'create_project.html', context={})
def project_list_view(request):
    projects = ProjectModel.objects.all()
    return render(request, 'project_list.html', context = {
        'projects':projects
        })

def project_detail_view(request, project_id):
    project = ProjectModel.object.get(pk_id = project_id)
    purchases = project.purchases
    return render(request, 'project_detail.html', context = {
        'project':project,
        'purchases':purchases,
    })
def purchase_add_view(request, project_id):
    project = ProjectModel.object.get(pk_id = project_id)
    if(request.method == 'POST'):
        postData = request.POST
        purchase = PurchaseModel.objects.create(
            name = postData['name'],
            quantity = postData['quantity'],
            price = postData['price'],
        )
        project.purchases.add(purchase)
        project.save()
        project.used_budget += purchase.price*purchase.quantity

    return render(request, 'project_add_form.html',context = {})


