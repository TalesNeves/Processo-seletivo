# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from sqlalchemy import create_engine
# username = "root"
# password = "pass"

# url =

# DEBUG = True

# a


from flask import Flask, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow
from flask_cors import CORS 
app = Flask(__name__)

db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow()


mysql = MySQL(app)



class Operadora(db.Model):
    __tablename__ = "Operadoras"
    reg_ans = db.Column(db.String(35),nullable=False)
    cnpj = db.Column(db.String(35),nullable=False,primary_key=True)
    razao_social = db.Column(db.String(35),nullable=False)
    nome_fantasia = db.Column(db.String(35),nullable=False)
    modalidade = db.Column(db.String(35),nullable=False)
    logradouro = db.Column(db.String(35),nullable=False)
    numero = db.Column(db.String(35),nullable=False)
    complemento = db.Column(db.String(35),nullable=False)
    bairro = db.Column(db.String(35),nullable=False)
    cidade = db.Column(db.String(35),nullable=False)
    uf = db.Column(db.String(35),nullable=False)
    cep = db.Column(db.String(35),nullable=False)
    ddd = db.Column(db.String(35),nullable=False)
    telefone = db.Column(db.String(35),nullable=False)
    fax = db.Column(db.String(35),nullable=False)
    email = db.Column(db.String(35),nullable=False)
    representante = db.Column(db.String(35),nullable=False)
    cargo_representante = db.Column(db.String(35),nullable=False)
    data_registro_ans = db.Column(db.String(35),nullable=False)

    def __init__(self,data,red_ans,cd_conta_contabil,descricao,vl_saldo_inicial,vl_saldo_final):
        self.reg_ans = reg_ans 
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.modalidade = modalidade
        self.logradouro = logradouro 
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep 
        self.ddd = ddd
        self.telefone = telefone
        self.fax = fax
        self.email = email
        self.representante = representante
        self.cargo_representante = cargo_representante
        self.data_registro_ans = data_registro_ans


class OperadoraSchema(ma.Schema):
    class Meta:
        fields = ('reg_ans',
        'cnpj',
        'razao_social',
        'nome_fantasia',
        'modalidade',
        'logradouro',
        'numero',
        'complemento',
        'bairro',
        'cidade',
        'uf',
        'cep',
        'ddd',
        'telefone',
        'fax',
        'email',
        'representante',
        'cargo_representante',
        'data_registro_ans'
        )

operadora_schema = OperadoraSchema()
operadoras_schema = OperadoraSchema(many=True)
    
CORS(app, resources={r'/*': {'origins': '*'}})

with app.app_context():
    db.create_all()

@app.route('/all', methods=['GET'])
def get_operadora():
    operadoras = []
    data = Operadora.query.all()
    # print(data)
    operadoras = operadoras_schema.dump(data)
    return  jsonify(operadoras)

@app.route('/like/<lookfor>', methods=['GET'])
def get_like(lookfor):
    print(lookfor)
    operadoras = []
    data = Operadora.query.filter(Operadora.razao_social.like(f'%{lookfor}%'))

    # print(data)
    operadoras = operadoras_schema.dump(data)
    return  jsonify(operadoras)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

