
from flask import Flask, render_template # Importando as bibliotecas Flask e para a criação de uma aplicação web
from flask_socketio import SocketIO # Importando a biblioteca SocketIO para adicionar recursos de comunicação

# Criando o Flask
app = Flask(__name__)

# Criando uma SocketIO paro o  Flask
socketio = SocketIO(app)

# Classe Logger para o registros de log
class Logger:
    def log(self, mensagem):
        print(mensagem)

# Criando a instância da classe Logger
logger = Logger()

# Rota principal da aplicação Flask com o HTML
@app.route('/')
def index():
    return render_template('index.html')

# Executa as mensagens recebidas
@socketio.on('mensagem')
def handle_message(mensagem):
    
    logger.log(mensagem)# Registra as mensagem no console
    socketio.send(mensagem)# Enviando as mensagem para o cliente

# Verificando se o arquivo está sendo executado 
if __name__ == '__main__':

    # Iniciando o servidor 
    socketio.run(app)









