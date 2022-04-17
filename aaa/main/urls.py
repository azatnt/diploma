from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_urls'),
    path('contacts', contacts, name='contacts_urls'),
    path('about_us', about_us, name='about_us_urls'),
    path('register', register, name='register_urls'),
    path('login/', login_request, name='login_urls'),
    path('logout', logout_request, name='logout_urls'),
    path('staff_info/<int:id>', staff_info, name='staff_info_urls'),
    path('mission', mission, name='mission_urls'),
    path('history', history, name='history_urls'),
    path('laws', laws, name='laws_urls'),
    path('rights', rights, name='rights_urls'),
    path('questions', questions, name='questions_urls'),
    path('services', services, name='services_urls'),
    path('get_service_time/<int:id>', get_service_time, name='get_service_time_url'),
    path('order_online', order_online, name='order_online_url'),
    path('send_message', send_message, name='send_message_url'),
    path('feedback', feedback, name='feedback_url')

]