
class ProductReadResponse:
    def __init__(self, __id):
        self.__id = 0

    def set_id(self, __id):
        self.__id = __id

    def get_product_id(self):
        return self.__id
