from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()

    query = "SELECT products.product_id, products.name, products.UOM_id, uom.uom_name, products.price_per_unit FROM products inner join uom on products.uom_id = uom.uom_id"

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


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))