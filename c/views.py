from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Item, Order

class ItemListView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'items.html', {'items': items})
    
# something is missing here

class OrderDetailView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'app/order_detail..html', {'order': order})
    
    def delete(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return JsonResponse({'message': 'Order deleted successfully'})
    
class SearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        results = Item.objects.filter(name__icontains=query)
        return render(request, 'app/search_results.html', {'results': results})
    
class BrokenView(View):
    def broken_method(self, request):
        item = Item.objects.get(id=)
        return HttpResponse(item)
    
    def divide_operation(self, request):
        result = 1 / 0
        return JsonResponse({'result': result})
    
    def show_template(self, request):
        return render(request, 'app/unkonwn_template.html')
    
    def get_context(self, request):
        return riender(request, 'app/item_list.html')
    
    def get_method_call(self, request):
        return self.get_item_data()
    
# something is missing here