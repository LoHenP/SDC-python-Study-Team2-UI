import atexit

from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiService import ConsoleUiService
from utility.keyboard.KeyboardInput import KeyboardInput
from console_ui.entity.Session import Session



class ConsoleUiServiceImpl(ConsoleUiService):
    __instance = None
    __session = None
    __transmitQueue = None
    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__repository = ConsoleUiRepositoryImpl.getInstance()
        return cls.__instance

    def __init__(self, repository):
        print("ConsoleUiServiceImpl 생성자 호출")
        atexit.register(self.onExit)

    def onExit(self):
        # transmitQueue에 종료코드를 보내주시면 됩니다.
        self.__transmitQueue.put(0)

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def printMenu(self):
        print("consoleUiServieceImpl 실행")
        self.__repository.printMenu()



    def processUserInput(self, transmitQueue):
        self.__transmitQueue = transmitQueue
        userChoice = KeyboardInput.getKeyboardIntegerInput()
        self.__repository.saveCurrentRoutingState(userChoice)




        # 필요하다면 여기 중간에 몇 가지 작업들이 더 처리 될 수 있습니다.
        self.__transmitQueue.put(userChoice)


