import abc


class RequestGeneratorService(abc.ABC):

    @abc.abstractmethod
    def findRequestGenerator(self, protocolNumber):
        pass

    @abc.abstractmethod
    def generateAccountRegisterRequest(self, arguments, sessionId):
        pass

    @abc.abstractmethod
    def generateAccountLoginRequest(self, arguments, sessionId):
        pass

    @abc.abstractmethod
    def generateProductInfoRequest(self, arguments, sessionId):
        pass