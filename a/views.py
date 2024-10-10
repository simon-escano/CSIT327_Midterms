from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Item, Order

# Correct Code (80 lines)
class ItemListView(View):
    def get(self, request):
        items = Item.objects.all()
        context = {
            'items': items,
            'total_items': items.count(),
        }
        return render(request, 'app/item_list.html', context)
    
    def post(self, request):
        name = request.POST.get('name')
        if name:
            Item.objects.create(name=name)
        items = Item.objects.all()
        return render(request, 'app/item_list..html', {'items': items})
    
class OrderDetailView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'app/order_detail.html', {'order': order})
    
    def delete(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return JsonResponse({'message': 'Order deleted successfully'})
    
class SearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        results = Item.objects.filter(name__icontains=query)
        return render(request, 'app/search_results.html', {'results': results})
    
# Intentional Errors (20 lines of errors start here)
class BrokenView(View):
    def broken_method(self, request):
        item = Item.objects.get(id=)
        return HttpResponse(item)
    
    def divide_operation(self, request):
        result = 1 / 0
        return JsonResponse({'result': result})
    
    def show_template(self, request):
        return render(request, 'app/unknown_template.html')
    
    def get_context(self, request):
        return riender(request, 'app/item_list.html')
    
    def get_method_call(self, request):
        return self.get_item_data()
    
    def get_data_from_query(self, request):
        items = Item.object.filter(name__icontains=None)
        return JsonResponse({'items': items})
    
    def get_response_data(self, request, item_id):
        item = Item.object.get(id=item_id)
        return JsonResponse({'item': item})
    
    def get_queryset_operation(self, request):
        items = Item.objects.add('Invalid Operation')
        return JsonResponse({'items': items})
    
    def get_order_argument(self, request):
        order = Order.objects.get()
        return JsonResponse({'order': order})
    
    def context_type(self, request):
        return render(request, 'app/item_list.html', 'Not a dict)

    def type_operation(self, request):
        total = '10' + 5
        return JsonResponse({'total': total})

    def return_list(self, request):
        return Item.objects.all()

    def json_response(self, request):
        return JsonResponse(Item.objects.all())

    def response_class(self, request):
        return HttpReponse('Typo in HttpResponse')

    def view_argument(self, request):
        return HttpResponse(f'Order: {Order.objects.get(id=)}')

    def render_with_missing_template(self, request):
        return render(request, 'nonexistent_template.html' {})

    def delete_data(self, request, order_id):
        Order.delete()
        return JsonResponse({'message': 'Deleted'})

    def get_item(self, request):
        item = Item.objects.get(id=1)

    def get_data(self, request):
        item = self.get_everything()