import json
import logging
import os
from typing import List, Optional

project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
log_file = "product_category.log"
log_directory = os.path.join(project_root, "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
log_path = os.path.join(log_directory, log_file)

# log in console&file
logging.basicConfig(
    filename=log_path, filemode="w", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        logging.info(f"Product created: {self}, {name}")


class Category:
    total_categories: int = 0
    total_products: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: Optional[List[Product]] = None,
        products_file: Optional[str] = None,
    ):
        self.name = name
        self.description = description
        self.products: List[Product] = products if products is not None else []

        # increas category counter when creat new object
        Category.total_categories += 1
        logging.info(f"Category created: {self}, {name}")

        # accounting total number products in the counter
        Category.total_products += len(self.products)

        # adding products from a JSON-file, if the file exists
        if products_file:
            try:
                with open("products.json", "r") as file:
                    products_list = json.load(file)
                    for product_data in products_list:
                        product = Product(**product_data)
                        self.products.append(product)
                        #Category.total_products += 1
                        logging.info(f"Added product {product} to category {self.name}")
            except (json.JSONDecodeError, FileNotFoundError) as e:
                logging.error(f"Error reading products file: {e}")
