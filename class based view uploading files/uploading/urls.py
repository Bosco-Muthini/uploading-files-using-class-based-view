from django.urls import path
from .views import BookListView,UploadBookView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',BookListView.as_view(),name='class_book_list'),
    path('upload/',UploadBookView.as_view(),name='class_upload_book'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
