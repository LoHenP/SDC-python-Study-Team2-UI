from custom_protocol.entity.CustomProtocol import CustomProtocol
from order_form.repository.OrderFormRepository import OrderFormRepository


class OrderFormRepositoryImpl(OrderFormRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("OrderFormRepositoryImpl 초기화")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createOrderPurchaseForm(self):
        return CustomProtocol.ORDER_PURCHASE.value

    def createOrderListForm(self):
        return CustomProtocol.ORDER_LIST.value