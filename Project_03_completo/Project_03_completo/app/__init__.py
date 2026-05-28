from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate    import Migrate
from typing           import Final

DB_CONECTION: Final[str] = 'mysql+mysqldb' # Estamos usando o mysql, mas pode usar outro se quiser.
DB_USER:      Final[str] = 'seu_usuario_do_banco'
DB_PASSWORD:  Final[str] = 'senha_do_usuario_do_banco'
DB_HOST:      Final[str] = 'localhost'
DB_PORT:      Final[str] = '3306'
DB_NAME:      Final[str] = 'nome_do_banco'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']        = f"{DB_CONECTION}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"]                     = 'sdaddasda4sdasd4s5d-4a6sdas84!!d8as49ds48'

db      = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import index
from app.routes import cadastrar_produto
from app.routes import listar_produtos
from app.routes import visualizar_produto
from app.routes import editar_produto
from app.routes import excluir_produto
from app.routes import relatorio
from app.models import Categoria, Produto

with app.app_context():
    if not Categoria.query.first():
        cat1 = Categoria(name = "Eletrônicos")
        cat2 = Categoria(name = "Alimentos")
        cat3 = Categoria(name = "Vestuário")
        db.session.add_all([cat1, cat2, cat3])
        db.session.commit()
        print("Categorias iniciais cadastradas com sucesso!")
