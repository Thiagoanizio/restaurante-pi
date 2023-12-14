from flask import Flask, send_from_directory, send_file, request, render_template

#bd
class Mesa:
    def __init__(self, id, capacidade) -> None:
        self.id = id
        self.capacidade = capacidade

class Reserva:
    def __init__(self, id, cliente_id, mesa_id, dia) -> None:
        self.id = id
        self.cliente_id = cliente_id
        self.mesa_id = mesa_id
        self.dia = dia

class Cliente:
    def __init__(self, email, nome, telefone, quantidade) -> None:
        self.id = email
        self.nome = nome
        self.telefone = telefone
        self.quantidade = quantidade
#arrays do bd
MESAS = [
    Mesa(1, 8), 
    Mesa(2, 4),
    Mesa(3, 4),
    Mesa(4, 6),
    Mesa(5, 6),
    Mesa(6, 6)
]

RESERVAS = [
    #Reserva(1, 'B', 2, '2022-02-17')
]

CLIENTES = [

]
app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/<nome>.html")
def index2(nome):
    return send_file(f"{nome}.html")

@app.route('/images/<filename>')
def my_images(filename):
    return send_from_directory("images", filename)

@app.route('/css/<filename>')
def my_css(filename):
    return send_from_directory("css", filename)

@app.route('/js/<filename>')
def my_js(filename):
    return send_from_directory("js", filename)

@app.route('/salvar_reserva', methods = ['GET'])
def salvar_reserva():
    nome = request.args.get('nome')
    telefone = request.args.get('telefone')
    email = request.args.get('email')
    dia = request.args.get('dia')
    quantidade = request.args.get('quantidade')
    mesa_id = request.args.get('mesa_id')

    cliente = Cliente(email, nome, telefone, quantidade)
    CLIENTES.append(cliente)

    reserva = Reserva(len(RESERVAS)+1, cliente.id, int(mesa_id), dia)
    RESERVAS.append(reserva)
    return 'Reserva Concluída!'

@app.route('/reserva', methods = ['GET'])
def listar_mesas_disponiveis():
    nome = request.args.get('nome')
    telefone = request.args.get('telefone')
    email = request.args.get('email')
    dia = request.args.get('dia')
    quantidade = request.args.get('quantidade')
    
    id_mesas_ocupadas = []

    for reserva in RESERVAS:
        if reserva.dia == dia:
            id_mesas_ocupadas.append(reserva.mesa_id)

    mesas_disponiveis = [mesa for mesa in MESAS if mesa.id not in id_mesas_ocupadas]

    return render_template('reserva.html', nome = nome, email = email, telefone = telefone, dia = dia, quantidade = quantidade, mesas = mesas_disponiveis)


@app.route('/reservas')
def reservas():
    import json
    return json.dumps([ob.__dict__ for ob in RESERVAS])
