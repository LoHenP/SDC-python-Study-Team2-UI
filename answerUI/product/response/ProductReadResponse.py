
class ProductReadResponse:
    def __init__(self, __id, __accountId):
        self.__id = 0
        self.__accountId = 0

    def set_id(self, __id):
        self.__id = __id

    def set_accountId(self, __accountId):
        self.__accountId = __accountId

    def get_product_id(self):
        return self.__id

    def get_accountId(self):
        return self.__accountId