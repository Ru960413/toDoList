from django.db.models import Q
from .models import Task
from django.core.paginator import Paginator, EmptyPage

# BUG: 會搜尋到其它使用者的資料
def taskSearch(request):
    search_query = ""
    user = request.user
    
    
    if request.method == "GET":
        search_query = request.GET.get("search_query")
        
    
        tasks = Task.objects.filter(
            Q(task_name__icontains =search_query)|
            Q(description__icontains=search_query)|
            Q(category__icontains=search_query)
        )

    return search_query, tasks

# def pagination(request):
#     pagination = Paginator(Task, 8) 


#     return pagination