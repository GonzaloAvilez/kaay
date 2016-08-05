from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from profiles.forms import ShopFor
from django.shortcuts import redirect
from profiles.views import ShowProfile
  
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True).order_by('?')
	# products = Product.objects.filter(author=request.user)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request,
				'shop/product/list.html',
				{'category'
				: category,
				'categories': categories,
				'products':products})

def product_detail(request, id, slug):
	product = get_object_or_404(Product,
								id=id,
								slug=slug,
								available=True)
	cart_product_form = CartAddProductForm()
	return render(request,
				'shop/product/detail.html',
				{'product': product,
				'cart_product_form': cart_product_form
				})

def product_edit(request,id,slug):
        product = get_object_or_404(Product,
                                    id=id,
                                   	slug=slug)                            	
        if request.method == "POST":
            form = ShopFor(request.POST or None, instance=product)
            if form.is_valid():
                product = form.save (commit=False)
                product.author = request.user
                product.save()
                return redirect("profiles:show_self")
        else:
            form = ShopFor (instance=product)
        return render(request, 'profiles/product_add.html', {'form':form})

def product_remove (request,id,slug):
		product = get_object_or_404(Product,
									id=id,
									slug=slug)
		user =request.user
		if product.author == user:
			product.delete()
		return redirect ('profiles:show_self')	
#considerar otra vista para redirecionar en lugar de show_self