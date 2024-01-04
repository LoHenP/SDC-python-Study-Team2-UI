from console_ui.service.ConsoleUiService import ConsoleUiService
from utility.keyboard.KeyboardInput import KeyboardInput


class ConsoleUiServiceImpl(ConsoleUiService):
    __instance = None
    __session = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__repository = repository
        return cls.__instance

    def __init__(self, repository):
        print("ConsoleUiServiceImpl 생성자 호출")

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def printMenu(self):

        self.__repository.printMenu()

    def printMenuResponse(self, response):

        self.__repository.printMenuResponse(response)

    def processUserInput(self, transmitQueue):
        userChoice = self.__repository.restrictUserInput()
        userChoice = self.__repository.userInputConverter(userChoice)
        self.__repository.saveCurrentRoutingState(userChoice)

        transmitData = {'protocolNum': userChoice, 'session': self.__repository.aquireSession()}
        # 필요하다면 여기 중간에 몇 가지 작업들이 더 처리 될 수 있습니다.
        transmitQueue.put(transmitData)


