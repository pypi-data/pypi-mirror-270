import requests
from bs4 import BeautifulSoup
from .models import Product
from .models import ShopResponse
import re


class Prices:
    def __init__(self, product: Product):
        self.product = product

    def alternate(self):
        """Get the price and availability from alternate"""
        url = str(self.product.alternate).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            price = float(
                soup.find("span", class_="price")
                .contents[0][2:]
                .replace(",", ".")
            )
            if "Artikel kann derzeit nicht gekauft werden" in page.text:
                availability = "no"
            else:
                availability = "yes"
            return ShopResponse(price=price, available=availability)

    def berrybase(self):
        """Get the price and availability from berrybase"""
        url = str(self.product.berrybase).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            price = float(
                soup.find_all("meta", attrs={"itemprop": "price"})[0].attrs[
                    "content"
                ]
            )
            if "Dieser Artikel steht derzeit nicht zur Verfügung!" in page.text:
                availability = "no"
            else:
                availability = "yes"
            return ShopResponse(price=price, available=availability)

    def welectron(self):
        """Get the price and availability from Welectron"""
        url = str(self.product.welectron).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            price_div = soup.find_all(
                "div", attrs={"class": "prodprice inclvat text-nowrap"}
            )[0]
            price = price_div.find("span").contents[0]
            price = price.strip(" €")
            if "ab Lager lieferbar" in page.text:
                availability = "yes"
            else:
                availability = "no"
            price = float(price.replace(",", "."))
            return ShopResponse(price=price, available=availability)

    def botland(self):
        """Get the price and availability from botland"""
        url = str(self.product.botland).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            price_span = soup.find(
                "span", attrs={"class": "current-price-display"}
            )
            price = price_span.contents[0]
            price = price.strip(" €")
            price = float(price.replace(",", "."))
            if "Erhältlich" in page.text:
                availability = "yes"
            elif "Wartezeit: 4-6 Wochen" in page.text:
                availability = "no"
            elif "Wartezeit: " in page.text:
                availability = "delayed"
            else:
                availability = None
            return ShopResponse(price=price, available=availability)

    def rossmann(self):
        """Get the price and availability from Rossmann"""
        url = str(self.product.rossmann).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            n1_price_span = soup.find(
                "span", attrs={"class": "rm-price__integer"}
            ).get_text()
            n2_price_span = soup.find(
                "span", attrs={"class": "rm-price__float"}
            ).get_text()
            price = f"{n1_price_span}.{n2_price_span}"
            if "Nur in der Filiale verfügbar" in page.text:
                availability = "only-in-store"
            elif "Bald verfügbar" in page.text:
                availability = "no"
            else:
                availability = "yes"
            if price == ".":
                return ShopResponse(available=availability)
            else:
                return ShopResponse(price=float(price), available=availability)

    def aldi_sued(self):
        """Get the price and availability from Aldi Süd"""
        url = str(self.product.aldi_sued).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            price_span = soup.find(
                "span", attrs={"class": "price__main"}
            ).get_text()
            price_span = re.sub(r"[^0-9.]", "", price_span)
            if "In den Warenkorb" in page.text:
                availability = "yes"
            elif (
                "Ausverkauft" in page.text
            ):  # FIXME: Also include new releasing products
                availability = "no"
            elif "Verkauf startet in" in page.text:
                availability = "no"
            else:
                availability = None
            price = float(price_span)
            return ShopResponse(price=price, available=availability)

    def lidl(self):
        """Get the price and availability from Lidl"""
        url = str(self.product.lidl).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            price_div = soup.find(
                "div", attrs={"class": "m-price__price"}
            ).get_text()
            price_div = re.sub(r"[^0-9.]", "", price_div)
            if "lieferbar" in page.text:
                availability = "yes"
            else:
                availability = "no"
            price = float(price_div)
            return ShopResponse(price=price, available=availability)

    def skandic(self):
        """Get the price and availability from Skandic"""
        url = str(self.product.skandic).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            price_div = soup.find(
                "div", attrs={"class": "product-price"}
            ).contents[1]
            price_div = re.sub(r"[^0-9,]", "", str(price_div))
            price = float(price_div.replace(",", "."))
            if "Neue Ware ist unterwegs" in page.text:
                availability = "delayed"
            elif "Sofort lieferbar" in page.text:
                availability = "yes"
            elif "Ungewisse Lieferzeit" in page.text:
                availability = "no"
            else:
                availability = "no"
            return ShopResponse(price=price, available=availability)

    def struck(self):
        """Get the price and availability from Struck (& Ludus)"""
        url = str(self.product.struck).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            price_span = soup.find("span", attrs={"class": "price"}).get_text()
            price_span = re.sub(r"[^0-9,]", "", price_span)
            price = float(price_span.replace(",", "."))
            if "Nicht vorrätig" in page.text:
                availability = "no"
            else:
                availability = "yes"
            return ShopResponse(price=price, available=availability)

    def ikea(self):
        """Get the price and availability from Ikea"""
        url = str(self.product.ikea).replace(" ", "")
        if url == "":
            return ShopResponse()
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            n1_price_span = soup.find(
                "span", attrs={"class": "pip-temp-price__integer"}
            ).get_text()
            n2_price_span = soup.find(
                "span", attrs={"class": "pip-temp-price__decimal"}
            ).get_text()
            n2_price_span = n2_price_span.strip(".")
            price = f"{n1_price_span}.{n2_price_span}"
            price = float(price)
            return ShopResponse(price=price)
