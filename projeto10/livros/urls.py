from django.urls import path
from . import views

app_name="livros"

urlpatterns = [
	path('login/',views.viewlogin,name="login"),
	path('registro/',views.viewregistro,name="registro"),
	path('biblioteca/',views.viewdashboard,name="biblioteca"),
	path('perfil/',views.viewperfil,name="perfil"),
	path('nvlivro/',views.viewnvlivro,name="nvlivro"),
	path('editarperfil/<int:id>',views.vieweditarperfil,name="editarperfil"),
	path('editarlivro/',views.vieweditarlivro,name="editarlivro"),
	path('verlivro/',views.viewverlivro,name="verlivro"),
	path('nvcategoria/',views.viewnvcategoria,name="nvcategoria"),
	path('viewnedicate/<int:id>',views.viewnedicate,name="viewnedicate"),

	path('caduser/',views.caduser,name="caduser"),
	path('loginuser/',views.loginuser,name="loginuser"),
	path('ediuser/<int:id>',views.ediuser,name="ediuser"),
	
	path('cadlivro/',views.cadlivro,name="cadlivro"),
	path('deletelivro/<int:id>',views.deletelivro,name="deletelivro"),
	path('verlivro1/<int:id>',views.verlivro,name="verlivro1"),
	path('editlivro/<int:id>',views.editlivro,name="editlivro"),
	path('edtlivro/<int:id>',views.edtlivro,name="edtlivro"),
	path('nvcate/',views.nvcate,name="nvcate"),
	path('deletecate/<int:id>',views.deletecate,name="deletecate"),
	path('editcate/<int:id>',views.editcate,name="editcate"),
	path('deleteuser/<int:id>',views.deleteuser,name="deleteuser"),
]

