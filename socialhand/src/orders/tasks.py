# -*- coding: utf-8 -*-
from celery import task
from django.core.mail import send_mail
from .models import Order


# @task
# def order_created(order_id):
# 	"""
# 	Task to send an e-mail notification when an order is
# 	successfully created.
# 	"""
# 	order = Order.objects.get(id=order_id)
# 	subject = 'Orden núm: {}'.format(order.id)
# 	message = 'Estimado {},\n\nHaz realizado tu pedido de manera exitosa.\
# 				Tu número de orden es {}.'.format(order.first_name,
# 											order.id)
# 	mail_sent = send_mail  (subject,
# 							message,
# 							'g.avilez.ig@gmail.com',
# 							[order.email])
	
# 	return mail_sent
def order_created(order_id):
	order = Order.objects.get(id=order_id)
	subject = 'Orden núm: {}'.format(order.id)
	message = 'Estimado {},\n\nHaz realizado tu pedido de manera exitosa.\
				Tu número de orden es {}.'.format(order.first_name,
											order.id)
	mail_sent = send_mail  (subject,
								message,
								'g.avilez.ig@gmail.com',
	 							[order.email])
	return mail_sent

	