from app.models import Produto, Categoria
from app        import db

class ControllerProduto():
    @classmethod
    def registerNewProduct(cls, product: Produto):
        db.session.add(product)
        db.session.commit()
    
    @classmethod
    def product_order_by_name(cls):
        return Produto.query.order_by(Produto.name).all()

    @classmethod
    def product_order_by_price(cls):
        return Produto.query.order_by(Produto.price).all()
    
    @classmethod
    def product_get_by_id(cls, id):
        return Produto.query.get_or_404(id)

    @classmethod
    def updateProduct(cls, product: Produto):
        db.session.commit()

    @classmethod
    def deleteProduct(cls, id):
        product = Produto.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()

    @classmethod
    def products_count_by_category(cls):
        # Retorna lista de tuplas (categoria, quantidade_de_produtos)
        categorias = Categoria.query.all()
        result = []
        for cat in categorias:
            count = Produto.query.filter_by(categoria_id=cat.id).count()
            result.append({'categoria': cat.name, 'quantidade': count})
        return result
