from django.shortcuts import render, redirect
dados = []

# Create your views here.
def home(request):
    global dados
    nome = ""
    codigo_barras = ""
    preco = ""

    if request.POST:
        nome = request.POST.get("nome")
        codigo_barras = request.POST.get("codigo_barras")
        preco = request.POST.get("preco")
        dados.append({"nome":nome, "codigo_barras":codigo_barras, "preco":preco})
        
    for i,row in enumerate(dados):
        row["id"] = i
        
    return render(request, "site_app/global/home.html", context={"dados":dados,"nome":nome,"codigo_barras":codigo_barras,"preco":preco})

# def deletar(request,id):
#     global dados
#     dados.pop(id)
#     return redirect(home)

def atualizar(request,id):
    global dados
    
    if request.POST:
        r = dados.pop(id)
        print(r)
        nome = request.POST.get("nome")
        codigo_barras = request.POST.get("codigo_barras")
        preco = request.POST.get("preco")
        dados.insert(id,{"nome":nome, "codigo_barras":codigo_barras, "preco":preco})

        return redirect(home)
    
    nome = dados[id].get("nome")
    codigo_barras = dados[id].get("codigo_barras")
    preco = dados[id].get("preco")
    return render(request, "site_app/global/atualizar.html", context={"id":id, "nome":nome,"codigo_barras":codigo_barras,"preco":preco})

def criar(request):
    return render(request, "site_app/global/criar.html")

def deletar(request):
    return render(request, "site_app/global/deletar.html")

def pesquisar(request):
    return render(request, "site_app/global/pesquisar.html")

def pesquisar(request):
    global dados
    nome = ""
    codigo_barras = ""
    preco = ""

    if request.POST:
        nome = request.POST.get("nome")
        codigo_barras = request.POST.get("codigo_barras")
        preco = request.POST.get("preco")
        dados.append({"nome":nome, "codigo_barras":codigo_barras, "preco":preco})
        
    for i,row in enumerate(dados):
        row["id"] = i
        
    return render(request, "site_app/global/pesquisar.html", context={"dados":dados,"nome":nome,"codigo_barras":codigo_barras,"preco":preco})

def deletar(request, id=None):
    global dados
    nome = ""
    codigo_barras = ""
    preco = ""

    

    if request.POST:
        nome = request.POST.get("nome")
        codigo_barras = request.POST.get("codigo_barras")
        preco = request.POST.get("preco")
        dados.append({"nome":nome, "codigo_barras":codigo_barras, "preco":preco})
        
    for i,row in enumerate(dados):
        row["id"] = i
        
    return render(request, "site_app/global/pesquisar.html", context={"dados":dados,"nome":nome,"codigo_barras":codigo_barras,"preco":preco})

def produtos(request):
    return render(request, "site_app/global/produtos.html")

def precos(request, id=0):
    dados = [
        {
            "id":1,
            "titulo" : "X bacon",
            "descricao" : "Double Bacon, Dois super hamburgueres de 100g, queijo cheddar, cebola caramelizada",
            "img": "https://img.restaurantguru.com/r483-ItaGastroPub-burger-2021-09.jpg"
        },
        {
            "id":2,
            "titulo" : "X Galinha",
            "descricao" : "Dois super hamburgueres de Frango 100g, queijo Mussarela e tomate",
            "img": "https://imagens.jotaja.com/produtos/6dcc15bd-80cb-426f-acd7-2f52de6f75cb.jpg"
        },
        {
            "id":3,
            "titulo" : "Mafioso",
            "descricao" : "Dois super hamburgueres de 100g, queijo Mussarela, cebola caramelizada e Jack Daniels",
            "img": "https://img.restaurantguru.com/rcb4-burger-ItaGastroPub.jpg"
        },
    ]

    if id:
        # import ipdb; ipdb.set_trace()
        dados = [dados[id - 1]]
    return render(request, "site_app/global/precos.html", context={"dados":dados})