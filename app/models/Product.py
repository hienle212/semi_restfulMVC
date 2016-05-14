from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    def get_all_product(self):
        query = "SELECT products.id as products_id, name, description, price FROM products" 
        return self.db.query_db(query)   
    def create(self, product):
        query = "INSERT INTO products (name, description, price, created_at, updated_at) values (:name,:description, :price ,NOW(), NOW())"
        data = {'name': product['name'], 'description': product['description'], 'price' : product['price']}
        return self.db.query_db(query, data)
    def remove(self, product_id):
        query = "DELETE FROM products WHERE id = :product_id"
        data =  {"product_id" : product_id}
        return self.db.query_db(query, data)
    def show(self, product_id):
        query = "SELECT products.id as products_id, name, description, price FROM products WHERE products.id=:product_id"
        data =  {"product_id" : product_id}
        return self.db.query_db(query, data)
    def edit(self, product):
        query = "UPDATE products SET name = :name, description = :description, price = :price, created_at = NOW(), updated_at = NOW() WHERE id = :id"
        data = {'name': product['name'], 'description': product['description'], 'price' : product['price'], 'id' : product['id']}
        return self.db.query_db(query, data)
