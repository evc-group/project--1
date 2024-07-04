from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import User, Seller, Product, Cart

app = Flask(__name__)

# Example storage (in-memory for demonstration purposes)
users = []
sellers = []
products = []
carts = {}

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
    
    # Example: Authenticate user
    user = next((user for user in users if user.username == username and user.password == password), None)
    if user:
        return redirect(url_for('user_account'))
    else:
        return render_template('login.html', error='Invalid username or password')

# Endpoint to handle seller login
@app.route('/seller_login', methods=['POST'])
def seller_login():
    username = request.form['username']
    password = request.form['password']
    
    # Example: Authenticate seller
    seller = next((seller for seller in sellers if seller.username == username and seller.password == password), None)
    if seller:
        return redirect(url_for('seller_account'))
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route('/user_account')
def user_account():
    return render_template('user_account.html')

@app.route('/seller_account')
def seller_account():
    return render_template('seller_account.html')

# Endpoint to display product list
@app.route('/product_list')
def product_list():
    return render_template('product_list.html', products=products)

# Endpoint to display cart items
@app.route('/cart')
def cart():
    user_cart = carts.get('user1')  # Replace with actual user identification logic
    if not user_cart:
        user_cart = Cart()
        carts['user1'] = user_cart
    return render_template('cart.html', cart=user_cart)

# Endpoint to add item to cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    try:
        data = request.get_json()
        product_name = data.get('product')
        price = float(data.get('price'))
        quantity = int(data.get('quantity', 1))

        # Implement user identification logic to get the current user
        user = get_current_user()  # Replace with your user identification logic

        if not user:
            return jsonify({'error': 'You need to be logged in to add items to cart.'}), 401

        # Example: Add item to user's cart (replace with actual storage logic)
        user_cart = get_user_cart(user)  # Replace with logic to get user's cart
        user_cart.add_item(product_name, price, quantity)

        return jsonify({'message': 'Item added to cart successfully!'})
    except Exception as e:
        print(f"Error adding item to cart: {str(e)}")
        return jsonify({'error': 'Failed to add item to cart.'}), 500


            @app.route('/get_cart_items', methods=['GET'])
def get_cart_items():
    try:
        return jsonify({'items': cart_items, 'total': sum(item['price'] * item['quantity'] for item in cart_items)})
    except Exception as e:
        print(f"Error fetching cart items: {str(e)}")
        return jsonify({'error': 'Failed to fetch cart items.'}), 500
    
    



        # Example: Find product by name (assuming products are already defined)
        product = next((prod for prod in products if prod.name == product_name), None)
        if product:
            user_cart.add_item(product)
            return jsonify({'message': 'Item added to cart successfully.'})
        else:
            return jsonify({'error': 'Product not found.'}), 404

    except Exception as e:
        print(f"Error adding item to cart: {str(e)}")
        return jsonify({'error': 'Failed to add item to cart.'}), 500


# Endpoint to remove item from cart
@app.route('/remove_from_cart/<product_name>', methods=['DELETE'])
def remove_from_cart(product_name):
    user_cart = carts.get('user1')  # Replace with actual user identification logic
    if user_cart:
        user_cart.remove_item(product_name)
        return jsonify({'message': f'Item {product_name} removed from cart successfully.'})
    else:
        return jsonify({'error': 'Cart not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
