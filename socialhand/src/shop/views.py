from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from profiles.forms import ShopFor
from django.shortcuts import redirect
from profiles.views import ShowProfile
from profiles.models import Profile
from django.views.generic import TemplateView,View
from django.shortcuts import render_to_response
#para endless pagination
from django.template import RequestContext
from endless_pagination.decorators import page_template
#para infinte pagination
from django.views.generic.list import ListView
from infinite_pagination.paginator import InfinitePaginator
# para el-pagination 
from el_pagination.views import AjaxListView
# import redis

# connect to redis
# r = redis.StrictRedis(host='localhost', port=6379, db=0)

  
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	# products = Product.objects.filter(author=request.user).order_by('?')
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request,
				'shop/product/list.html',
				{'category'	: category,
				'categories': categories,
				'products': products})

def product_detail(request, id, slug):
	product = get_object_or_404(Product,
								id=id,
								slug=slug,
								available=True)
	# increment total image views by 1
	# total_views = r.incr('product:{}:views'.format(product.id))
	# increment image ranking by 1
	# r.zincrby('product_ranking', product.id, 1)
	cart_product_form = CartAddProductForm()
	# looking author of product
	creator=product.author
	if creator :
		craftsman = get_object_or_404 (Profile,user_id=creator)																			
	return render(request,
				 'shop/product/detail.html',{
				 'product': product,
				 # 'total_views':total_views,
				 'cart_product_form': cart_product_form,
				 'craftsman':craftsman,})
	
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

def product_ranking(request):
		# get image ranking dictionary
		product_ranking = r.zrange('product_ranking', 0, -1,desc=True)[:10]
		product_ranking_ids = [int(id) for id in product_ranking]
		# get most viewed images
		most_viewed = list(Product.objects.filter(id__in=product_ranking_ids))
		most_viewed.sort(key=lambda x: product_ranking_ids.index(x.id))
		return render(request,
					'shop/product/ranking.html',
					{'section': 'products',
					'most_viewed': most_viewed})



#paginacion alternativa . no definita one-by-one


# @page_template('shop/product/list_test.html')
# def pagination(request,template='shop/product/list_index.html',extra_context=None):
# 	pag_product = Product.objects.all()
# 	context = {'products':pag_product}
# 	if extra_context is not None:
# 		context.update(extra_context)
# 	return render_to_response(template,context,context_instance=RequestContext(request))	


#paginacion opciones alternas

class ProductListView(AjaxListView,View):
		context_object_name = "categories"
		model = Category

		template_name = 'shop/list_index.html'
		page_template = 'shop/category_list.html'
		

		def get(self,request,*args,**kwargs):
			
			categories = Category.objects.all()
			kwargs['categories']=categories
			return super(ProductListView,self).get(request,*args,**kwargs)


class ProductTestView(AjaxListView,View):
		context_object_name = "products"
		template_name = "shop/product/list.html"
		page_template = "shop/product_list.html"


		def get_queryset(self):
			return Product.objects.all()

		def get_context_data(self,**kwargs):
			kwargs['categories'] = Category.objects.all()
			return super(ProductTestView,self).get_context_data(**kwargs)
			