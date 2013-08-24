# Create your views here.
from coffin import shortcuts

def index(request):
    return shortcuts.render_to_response("page/index.html")
def about(request):
    return shortcuts.render_to_response("page/about.html")
def products(request):
    return shortcuts.render_to_response("page/products.html")
def services(request):
    return shortcuts.render_to_response("page/services.html")
def support(request):
    return shortcuts.render_to_response("page/support.html")
def project(request):
    return shortcuts.render_to_response("page/project.html")
def jiejue(request,page):
    htmlpathstr ="jiejue/"+page+".html"
    return shortcuts.render_to_response(htmlpathstr)
def about(request,page):
    htmlpathstr ="about/"+page+".html"
    return shortcuts.render_to_response(htmlpathstr)
def jiejue2(request):
    return shortcuts.render_to_response("page/support.html")
