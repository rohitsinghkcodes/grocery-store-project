import product_dao
from sql_connection import get_sql_connection 
from flask import Flask, request, jsonify

app = Flask(__name__)

# getting the connection to sql and storing it in GLOBAL var
connection = get_sql_connection()

# endpoint for getting all the products
@app.route("/getProducts", methods = ['GET'])
def get_products():
    products = product_dao.get_all_products(connection)
    # converting response into json
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

# endpoint for deleting the product
@app.route("/deleteProduct", methods = ['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    # converting the response into json
    response.jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print('Starting Python Flask Server For Grocery Management Store')
    app.run(port = 5000)