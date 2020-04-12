from django.http imports HttpResponse


# Create your views here.
def homePageView(request):
	return_HttpResponse('Hello world!')
