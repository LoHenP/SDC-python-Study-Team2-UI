import abc

class CustomProtocolService(abc.ABC):
    @abc.abstractmethod
    def registerCustomProtocol(self, protocolNumber, pointerOfFunction):
        pass

    @abc.abstractmethod
    def productListCustomProtocol(self, protocolNumber, pointerOfFunction):
        pass
