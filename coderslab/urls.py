"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from exercises_app.views import (SchoolView, SchoolClassView, StudentClassView, GradesClassView, StudentSearchView,
                                 AddStudentView, ExchangeView, AddGradeView, PresenceListView, SetColorView, FemaleNamesView,
                                 NumberAndString, SubjectCreate, SubjectCreate2, Login, MessageView, StudentNoticeView,
                                 AddNoticeView, DeleteNoticeView, UserListView, Login2View, LogoutView, AddUserView,
                                 ResetPasswordView)

from homework_app.views import (CategoriesView, CategoryDetails, ProductDetails, AddCategoryView, EditCategoryView,
                                ProductListView, EditProductView, AddProductView, SearchView, Login3View)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SchoolView.as_view(), name="index"),
    path('class/<int:school_class>/', SchoolClassView.as_view(), name="school-class"),
    path('student/<int:student_id>/', StudentClassView.as_view(), name="student"),
    path('grades/<int:student_id>/<int:subject_id>/', GradesClassView.as_view(), name="grades"),
    path('student_search/', StudentSearchView.as_view(), name="student_search"),
    path('add_student/', AddStudentView.as_view(), name="add_student"),
    path('exchange/', ExchangeView.as_view(), name="exchange"),
    path('add_grade/', AddGradeView.as_view(), name="add_grade"),
    path('class_presence/<int:student_id>/<str:date>', PresenceListView.as_view(), name="presence_list"),
    path('set_color/', SetColorView.as_view(), name="set_color"),
    path('login/', Login.as_view(), name='login'),
    path('d2_p3_e3/', FemaleNamesView.as_view(), name="female_names"),
    path('d2_p3_e4/', NumberAndString.as_view(), name='no_and_str'),
    path('subject_create/', SubjectCreate.as_view(), name='subject_create'),
    path('subject_create2/', SubjectCreate2.as_view(), name='subject_create2'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('category/<slug>', CategoryDetails.as_view(), name='category-details'),
    path('product/<int:product_id>', ProductDetails.as_view(), name='product-details'),
    path('send_message/', MessageView.as_view(), name='message'),
    path('notices/<int:student_id>', StudentNoticeView.as_view(), name='notices'),
    path('notices/<int:student_id>', StudentNoticeView.as_view(), name='notices'),
    path('add_notice/', AddNoticeView.as_view(), name='add-notice'),
    path('delete_notice/<int:pk>', DeleteNoticeView.as_view(), name='delete-notice'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('edit_category/<str:slug>', EditCategoryView.as_view(), name='edit-category'), #slug:slug
    path('products/', ProductListView.as_view(), name='products'),
    path('edit_product/<int:pk>/', EditProductView.as_view(), name='edit-product'),
    path('add_product/', AddProductView.as_view(), name='add-product'),
    path('search/', SearchView.as_view(), name='search'),
    path('list_users/', UserListView.as_view(), name='list-users'),
    path('login2/', Login2View.as_view(), name='login2'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_user/', AddUserView.as_view(), name='add-user'),
    path('reset_password/<int:id>/', ResetPasswordView.as_view(), name='reset_password'),
    path('login3/', Login3View.as_view(), name='login3'),

]
