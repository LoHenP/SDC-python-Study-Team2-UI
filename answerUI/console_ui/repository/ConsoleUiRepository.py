import abc


class ConsoleUiRepository(abc.ABC):

    @abc.abstractmethod
    def saveCurrentRoutingState(self, currentState):
        pass

    @abc.abstractmethod
    def acquireCurrentRoutingState(self):
        pass

    @abc.abstractmethod
    def saveRequestFormToTransmitQueue(self):
        pass

    @abc.abstractmethod
    def aquireSessionId(self):
        pass

    @abc.abstractmethod
    def aquireProductId(self):
        pass


    @abc.abstractmethod
    def restrictUserInput(self):
        pass


    @abc.abstractmethod
    def userInputConverter(self, userChoice):
        pass


    @abc.abstractmethod
    def printMenu(self):
        pass

    @abc.abstractmethod
    def printMenuResponse(self):
        pass

