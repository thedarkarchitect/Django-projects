from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logout/', views.userLogout, name='logout'),

    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('user/', views.userPage, name='user'),
    path('account/', views.accountSettings, name='account'),

    path('create_order/<str:pk>', views.createOrder, name='createOrder'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete/<str:pk>/', views.delete, name='delete'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="reset_password" ),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name="password_reset_done" ),#will notify the password was reset
    path('reset/<uidb64/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), name="password_reset_confirm" ),#this will send the user the link too accept password change, token makes sure the password is valid
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_Reset_complete" ),#show success message
]

"""
1 - Submit email from                          //PasswordRestView.as_view()
2 - Email sent success message                //PasswordRestDoneView.as_view()
3 - Link to password Rest form in email      //PasswordResetConfirmView.as_view()
4 - Password successfully changed message   //PaswordResetCompleteView.as_view()
"""