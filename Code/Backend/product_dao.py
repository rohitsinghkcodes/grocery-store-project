from sql_connection import get_sql_connection


# GETTING ALL THE PRODUCTS
def get_all_products(connection):
    cursor = connection.cursor()
    query = "SELECT products.product_id, products.name, products.UOM_id, uom.uom_name, products.price_per_unit FROM products INNER JOIN uom ON products.uom_id = uom.uom_id"
    cursor.execute(query)
    # list storing response from the db
    response = []
    # now results are in the curson
    for (product_id, name, uom_id, uom_name, price_per_unit) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'uom_name' : uom_name,
                'price_per_unit' : price_per_unit
            }
        )
    
    return response


# INSERTING A PRODUCT
def insert_new_product(connection, product):
    cursor = connection.cursor()
    # parameterized query
    query = ("INSERT INTO products (name, uom_id,price_per_unit) VALUES (%s, %s, %s)")
    data = (product['name'], product['uom_id'], product['price_per_unit'])
    # executing query 
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


# DELETING A PRODUCT
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id =" + str(product_id))
    # executing query 
    cursor.execute(query)
    connection.commit()
    return "Deletion Completed"

if __name__ == '__main__':
    connection = get_sql_connection()

    # print(get_all_products(connection))


    # print(insert_new_product(connection, {
    #             'name': 'milk',
    #             'uom_id': '3',
    #             'price_per_unit' : '40'
    # }))

    print(delete_product(connection, 5))
    