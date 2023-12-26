import abc

class CustomProtocolService(abc.ABC):
    @abc.abstractmethod
    def registerCustomProtocol(self, protocolNumber, pointerOfFunction):
        pass

    @abc.abstractmethod
    def loginCustomProtocol(self, protocolNumber, pointerOfFunction):
        pass

