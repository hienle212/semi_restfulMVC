from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db   
    def index(self):
        products = self.models['Product'].get_all_product()
        return self.load_view('main.html', products = products)
    def new(self):
        return self.load_view('add_product.html')
    def edit(self, product_id):
        product_info = self.models['Product'].show(product_id)
        print product_info
        return self.load_view('edit_product.html', product_info = product_info[0])
    def create(self):
        newProduct = {'name': request.form['name'], 'description': request.form['description'], 'price': request.form['price']}
        self.models['Product'].create(newProduct)
        return redirect('/')       
    def show(self, product_id):
        product_info = self.models['Product'].show(product_id)
        return self.load_view('show_product.html', product_info = product_info)
    def update(self):
        self.models['Product'].edit(request.form)
        return redirect('/')
    def destroy(self,product_id):
        self.models['Product'].remove(product_id)
        return redirect('/')



