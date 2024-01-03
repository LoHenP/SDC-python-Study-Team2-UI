import abc
class OrderFormRepository(abc.ABC):
    @abc.abstractmethod
    def createOrderPurchaseForm(self):
        pass
    @abc.abstractmethod
    def createOrderListForm(self):
        pass