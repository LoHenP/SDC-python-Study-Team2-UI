import abc

class ProductFormRepository(abc.ABC):
    @abc.abstractmethod
    def createProductListForm(self):
        pass

    @abc.abstractmethod
    def createProductInfoForm(self):
        pass


    @abc.abstractmethod
    def createProductAddForm(self):
        pass
