from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('authors/add/', views.add_author, name='add_author'),
    path('books/add/', views.add_book, name='add_book'),
    path('borrow/add/', views.add_borrow_record, name='add_borrow_record'),
    path('authors/', views.list_authors, name='list_authors'),
    path('books/', views.list_books, name='list_books'),
    path('borrow/', views.list_borrow_records, name='list_borrow_records'),
    path('export/', views.export_to_excel, name='export_to_excel'),

    path('', auth_views.LoginView.as_view(template_name='library/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')    
]
