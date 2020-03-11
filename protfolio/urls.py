
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import  static
import jobs.views
from blog import views
from blog.views import detail
import blog.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', jobs.views.home,name='home'),
    path('blog/', include('blog.urls')),
    path('<int:blog_id>/',views.detail,name='detail'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

