import psycopg2
import random
import string
import datetime
from random import randint
from dateutil.relativedelta import relativedelta
import time


# Establishing connection with the database server
try:
    # connection values to establish a connection
    conn = psycopg2.connect(host="localhost", database="postgres", user="postgres")
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
except Exception as e:
            print("Ooops, can't connect. Invalid database name, user or password?")
            print(e)

# Counter for loop and for ID of product
count_products = 1

# Start timer to calculate the time when performing the loop
start_time = time.time()

# Feeding the text files into python lists.
with open('title.txt', 'r') as infile:
    title_list = infile.read().splitlines()
with open('brand.txt', 'r') as infile:
    brand_list = infile.read().splitlines()
with open('producer.txt', 'r') as infile:
    producer_list = infile.read().splitlines()
with open('produced_in.txt', 'r') as infile:
    produced_in_list = infile.read().splitlines()
with open('description.txt', encoding="utf8") as infile:
    description_list = infile.read().splitlines()
with open('category.txt', 'r') as infile:
    category_list = infile.read().splitlines()
with open('url.txt', 'r') as infile:
    url_list = infile.read().splitlines()
with open('ingredients.txt', 'r') as infile:
    ingredients_list = infile.read().splitlines()

# Loop that creates dummy products and writes them on the database server
while count_products < 10:

    # Variables that take a random item from the lists
    title = random.choice(title_list)
    brand = random.choice(brand_list)
    producer = random.choice(producer_list)
    produced_in = random.choice(produced_in_list)
    description = random.choice(description_list)
    category = random.choice(category_list)
    weight_prod = randint(100.0, 1000.0)
    capacity_prod = randint(100.0, 1000.0)
    urls = random.choice(url_list)
    package_units = randint(1, 24)
    package_weight_prod = randint(100.0, 1000.0)
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now() + relativedelta(days=5)
    ingredients = random.choice(ingredients_list)
    company_id = randint(1000, 100000)
    kind = randint(1, 10)
    type_of = random.choice(["Food", "Beverages", "Non-food"])
    private_label = random.choice(["True", "False"])
    shelf_time = randint(3, 700)
    alcohol_vol = randint(0, 75)
    visible = random.choice(["True", "False"])

# function that creates a random string of length 10
    def randomword(length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    code = randomword(10)

    # Try statement that will gather the information from the text files embedded in the variables each time an iteration of the loop occurs
    try:
        sql = "INSERT INTO products VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

# execute the sql statement
        cursor.execute(sql, (count_products, title, brand, producer, produced_in, description, category, weight_prod, capacity_prod, urls, package_units, package_weight_prod, code, created_at, updated_at, ingredients, company_id, kind, type_of, private_label, shelf_time, alcohol_vol, visible))

# Commit changes to database server
        conn.commit()
        count_products = count_products + 1

    except Exception as e:
            print("Error in the SQL execution")
            print(e)

# Print the total time of execution of the code
print("--- %s seconds ---" % (time.time() - start_time))












