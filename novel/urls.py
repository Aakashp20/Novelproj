from django.urls import path
from novel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 	path('login/',views.login,name='login'),
 	path('home/',views.home,name='home'),
 	path('register/',views.Register,name='register'),
	path('author/',views.author,name='author'),
	path('bookdata/<int:id>',views.bookdata,name='bookdata'),
	path('page/<int:id>',views.page,name='page'),
	path('page/<int:id>/<int:chapid>',views.chapter,name='chapter'),
 	#path('page/<int:id>/<int:chapid>',views.chapter,name='otherchap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
