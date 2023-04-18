from django.urls import path, re_path
from .views import *
urlpatterns = [

    path('',index,name='home'),
    path('trainingSelfDevelopment/',Training1.as_view(),name='training1'),
    path('trainingSelfDevelopment/',AllTraining1.as_view(),name='training1'),
    path('trainingManager1/',training_manager1,name='training_manager1'),
    path('trainingPsychology/',training2,name='training2'),
    path('books/',cache_page(60)(AllBooks.as_view()),name='books'),
    path('',index,name='home'),
    path('trainingSelfDevelopment/',training1,name='training1'),
    path('trainingManager1/',training_manager1,name='training_manager1'),
    path('trainingPsychology',training2,name='training2'),
    path('books',books,name='books'),
    path('category/<int:category_id>/',show_category,name='category'),
    path('post/<int:post_id>/', show_post, name='post')


]