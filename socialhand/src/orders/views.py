# -*- coding: utf-8 -*-
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.conf import settings
import weasyprint
from .tasks import order_created



def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
										product=item['product'],
										price=item['price'],
										quantity=item['quantity'])
			
			# clear the cart
			cart.clear()
			# launch asynchronous task
			order_created.delay(order.id)
			request.session['order_id'] = order.id 
			return redirect(reverse('payment:process'))

	else:
		form = OrderCreateForm()
	return render(request,
				'orders/order/create.html',
				{'cart': cart, 'form': form})


# decorator to make sure only staff users can access this view for pdf´s	
@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request,
				'orders/order/detail.html',
				{'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	html = render_to_string('orders/order/pdf.html',
							{'order': order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename=\"order_{}.pdf"'.format(order.id)
	weasyprint.HTML(string=html).write_pdf(response,
		stylesheets=[weasyprint.CSS(
			settings.STATIC_ROOT + 'css/pdf.css')])
	return response