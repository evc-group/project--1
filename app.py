from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Example cart storage (in-memory for demonstration purposes)
cart_items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Endpoint to handle user login
@app.route('/user_login', methods=['POST'])
def user_login():
    username = request.form['username']
    password = request.form['password']
    # Add logic to authenticate user
    return redirect(url_for('user_account'))

# Endpoint to handle seller login
@app.route('/seller_login', methods=['POST'])
def seller_login():
    username = request.form['username']
    password = request.form['password']
    # Add logic to authenticate seller
    return redirect(url_for('seller_account'))

@app.route('/user_account')
def user_account():
    return render_template('user_account.html')

@app.route('/seller_account')
def seller_account():
    return render_template('seller_account.html')

# Endpoint to display product list
@app.route('/product_list')
def product_list():
    return render_template('product_list.html')

# Endpoint to display cart items
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Endpoint to add item to cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product = request.json.get('product')
    price = request.json.get('price')
    quantity = request.json.get('quantity', 1)  # Default quantity to 1 if not provided
    cart_items.append({'product': product, 'price': price, 'quantity': quantity})
    return jsonify({'message': 'Item added to cart successfully.'})

@app.route('/get_cart_items', methods=['GET'])
def get_cart_items():
    try:
        return jsonify({'items': cart_items, 'total': sum(item['price'] * item['quantity'] for item in cart_items)})
    except Exception as e:
        print(f"Error fetching cart items: {str(e)}")
        return jsonify({'error': 'Failed to fetch cart items.'}), 500


# Endpoint to remove item from cart
@app.route('/remove_from_cart/<product>', methods=['DELETE'])
def remove_from_cart(product):
    global cart_items
    cart_items = [item for item in cart_items if item['product'] != product]
    return jsonify({'message': f'Item {product} removed from cart successfully.'})

if __name__ == '__main__':
    app.run(debug=True)
