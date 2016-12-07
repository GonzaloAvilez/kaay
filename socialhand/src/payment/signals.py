from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order
#send a pdf ticket
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import weasyprint
from io import BytesIO

from django.core.mail import send_mail
 

def payment_notification(sender, **kwargs):
	ipn_obj = sender
	if ipn_obj.payment_status == ST_PP_COMPLETED:
		# payment was successful
		order = get_object_or_404(Order, id=ipn_obj.invoice)
		# mark the order as paid
		order.paid = True
		order.save()
		# create invoice e-mail
		subject = 'iKaay - Invoice payment_notificationo. {}'.format(order.id)
		message = 'Please, find attached the invoice for your recent purchase.'
		email = EmailMessage(subject,
							message,
							'info@ikaay.com.mx',
							[order.email])
		# generate PDF
		html = render_to_string('orders/order/pdf.html',
					 			{'order': order})
		out = BytesIO()
		stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
		weasyprint.HTML(string=html,
			 			base_url=request.build_absolute_uri(),
			 			).write_pdf(out,
			 						stylesheets=stylesheets)
		# attach PDF file
		email.attach('order_{}.pdf'.format(order.id),
					out.getvalue(),	
					'application/pdf')
		# send e-mail
		email.send()

		# send_mail('HOLA'	,
		# 		'PAGO',
		# 		'g.avilez.ig@gmail.com',
		# 		[order.email])
		

valid_ipn_received.connect(payment_notification)