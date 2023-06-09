class Guitar:

    def __init__(self, name, description, stock, min_stock, buy_price, sell_price, maker, id = None ):
        self.name = name
        self.description = description
        self.stock = stock
        self.min_stock = min_stock
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.maker = maker
        self.id = id

    def margin(self):
        margin = self.sell_price - self.buy_price
        return margin
    
    def low_stock(self):
        if self.stock <= self.min_stock:
            return True
        else:
            return False




