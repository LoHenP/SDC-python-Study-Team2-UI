
class ProductListResponse:
    def __init__(self):
        self.__productsLength = 0

    def set_productsLength(self, productsLength):
        self.__productsLength = productsLength

    def get_productsLength(self):
        return self.__productsLength