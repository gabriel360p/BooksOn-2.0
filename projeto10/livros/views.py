from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import urls
from .models import tb_book,tb_user

def viewlogin(request):	
	return render(request,'login.html')

def viewregistro(request):
	return render(request,'registro.html')

def viewdashboard(request):
	books=tb_book.objects.all()
	return render(request,'dashboard.html',{'books':books})

def viewperfil(request):
	perfils=tb_user.objects.all()
	try:
		return render(request,'perfil.html',{'users':perfils})
	except:
		return redirect('livros:perfil',{'users':perfils})
	
def vieweditarperfil(request,id):
	perfil=tb_user.objects.get(pk=id)
	return render(request,'editarperfil.html',{'perfil':perfil})

def viewnvlivro(request):
	categorias=tb_book.objects.all()
	return render(request,'reglivro.html',{'categoria':categorias})

def vieweditarlivro(request):
	return render(request,'editarlivro.html')

def viewverlivro(request):
	return render(request,'verlivro.html')

def viewnvcategoria(request):
	categorias=tb_book.objects.all()
	return render(request,'nvcategoria.html',{'categoria':categorias})

def viewnedicate(request,id):
	categorias=tb_book.objects.get(pk=id)
	return render(request,'edicate.html',{'categoria':categorias})


def viewsoeu(request):
	user=tb_user.objects.all()
	return render(request,'soeu.html',{'users':user})


def caduser(request):
	if request.method=="POST":
		gmail=request.POST.get('email')
		gmail=tb_user.objects.filter(email=gmail)

		if gmail:
			return render(request,'registro.html',{'cor':"#f8d7da",'mensage':"Email já Cadastrado"})
		else:
			nome=request.POST.get('nome')
			sobrenome=request.POST.get('sobrenome')
			email=request.POST.get('email')
			senha=request.POST.get('senha')
			critpto=md5(senha)
			endereco=request.POST.get('endereco')
			cidade=request.POST.get('cidade')
			estado=request.POST.get('estado')
			#salvando no banco de dados
			user=tb_user(name=nome,lastname=sobrenome,email=email,password=critpto,address=endereco,city=cidade,state=estado)
			user.save()
			return redirect('livros:login')
	else:
		print("|Acesso GET negado")
		return render(request,'registro.html')



def ediuser(request,id):	
	useredit=tb_user.objects.get(pk=id)

	useredit.name=request.POST.get('nome')
	useredit.lastname=request.POST.get('sobrenome')
	useredit.email=request.POST.get('email')
	useredit.password=request.POST.get('senha')
	useredit.address=request.POST.get('endereco')
	useredit.city=request.POST.get('cidade')
	useredit.state=request.POST.get('estado')
	useredit.save()
	return redirect('livros:perfil')


def loginuser(request):
	if request.method=="POST":
		email=request.POST.get('email')
		senha=request.POST.get('senha')
		useremail=tb_user.objects.filter(email=email)
		usersenha=tb_user.objects.filter(password=senha)

		#por algum  motivo o 'or' esta assummindo o palpel do 'and' 
		if not useremail or not usersenha:
			return redirect('livros:registro')
		else:
			return redirect('livros:biblioteca')
	else:
		return HttpResponse("|Get negado")

def deleteuser(request,id):
	user=tb_user.objects.get(pk=id)
	user.delete()
	return redirect('livros:perfil')


def cadlivro(request):
	if request.method=="POST":
		titulo=request.POST.get('titulo')
		autor=request.POST.get('autor')
		preco=request.POST.get('preco')
		categoria=request.POST.get('categoria')
		texto=request.POST.get('texto')
		book=tb_book(title=titulo,author=autor,price=preco,categorie=categoria,text=texto)
		book.save()
		return redirect('livros:biblioteca')
	else:
		return redirect('livros:biblioteca')

def deletelivro(request,id):
	book=tb_book.objects.get(pk=id)
	book.delete()
	return redirect('livros:biblioteca')

def verlivro(request,id):
	bookinfo=tb_book.objects.get(pk=id)
	return render(request,'verlivro.html',{'bookinfo':bookinfo})

def editlivro(request,id):
	editlivros=tb_book.objects.get(pk=id)
	return render(request,'editarlivro.html',{'bookinfos':editlivros})

def edtlivro(request,id):
	if request.method=="POST":
		edbook=tb_book.objects.get(pk=id)
		edbook.title=request.POST.get('titulo')
		edbook.author=request.POST.get('autor')
		edbook.price=request.POST.get('preco')
		edbook.categorie=request.POST.get('categoria')
		edbook.text=request.POST.get('texto')
		edbook.save()

		return redirect('livros:biblioteca')
	else:
		return redirect('livros:biblioteca')

def nvcate(request):
	if request.method=="POST":
		categoria=request.POST.get('categoria')
		
		categorie=tb_book(categorie=categoria)
		categorie.save()
		return redirect('livros:biblioteca')

def editcate(request,id):
	cate=tb_book.objects.get(pk=id)
	cate.categorie=request.POST.get('categoria')
	cate.save()
	return redirect('livros:nvcategoria')

def deletecate(request,id):
	cate=tb_book.objects.get(pk=id)
	cate.delete()
	return redirect('livros:nvcategoria')