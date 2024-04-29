import sqlite3
from .models import Product


class Database:
    def __init__(self, name: str = "testdatabase.db"):
        """Initial function to create the database
        This function creates a database (usually testdatabase.db) if it's not there
        """
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            product_category TEXT,
            alternate TEXT,
            berrybase TEXT,
            welectron TEXT,
            botland TEXT,
            rossmann TEXT,
            aldi_sued TEXT,
            lidl TEXT,
            skandic TEXT,
            struck TEXT,
            ikea TEXT
            )
            """
        )
        self.conn.commit()

    def add_product(self, product: Product):
        """Add a product
        This function get's a product object (you can see it in models.py) and then adds it in the database
        """
        self.cur.execute(
            """
            INSERT INTO products (name, product_category, alternate, berrybase, welectron, botland, rossmann, aldi_sued, lidl, skandic, struck, ikea)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                product.name,
                product.category,
                product.alternate,
                product.berrybase,
                product.welectron,
                product.botland,
                product.rossmann,
                product.aldi_sued,
                product.lidl,
                product.skandic,
                product.struck,
                product.ikea,
            ),
        )
        self.conn.commit()

    def search_by_id(self, id_: int):
        """Get the product with a specific id
        With this function, you can get the product by an id. The id has to be id_
        """
        a = self.cur.execute(
            "SELECT * FROM products WHERE id = ?", (id_,)
        ).fetchone()
        return Product(
            name=a[1],
            category=a[2],
            alternate=a[3],
            berrybase=a[4],
            welectron=a[5],
            botland=a[6],
            rossmann=a[7],
            aldi_sued=a[8],
            lidl=a[9],
            skandic=a[10],
            struck=a[11],
            ikea=a[12],
        )

    def search_by_name(self, name: str):
        """Get all products that match with name
        You get a list back with all of the products that match your query
        """
        query = "SELECT * FROM products WHERE name LIKE ?"
        name_pattern = f"%{name}%"  # allows searching for substrings in names
        results = self.cur.execute(query, (name_pattern,)).fetchall()
        end_results = []
        for result in results:
            end_results.append(
                Product(
                    name=result[1],
                    category=result[2],
                    alternate=result[3],
                    berrybase=result[4],
                    welectron=result[5],
                    botland=result[6],
                    rossmann=result[7],
                    aldi_sued=result[8],
                    lidl=result[9],
                    skandic=result[10],
                    struck=result[11],
                    ikea=result[12],
                )
            )
        return end_results

    def get_all_product_ids(self):
        """Get all the ids from all products"""
        results = self.cur.execute("SELECT id FROM products").fetchall()
        return results
