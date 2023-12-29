from console_ui.service.ConsoleUiService import ConsoleUiService
from utility.keyboard.KeyboardInput import KeyboardInput
from console_ui.entity.Session import Session



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

    def processUserInput(self, transmitQueue):
        print("메뉴")
        print("1. 로그인")
        print("2. 회원가입")
        print("5. 상품 목록")
        print("6. 상품 조회")
        # if not receiveQueue.empty():
        #     sessionid = receiveQueue.get()
        #     self.__session = Session(sessionid)

        userChoice = KeyboardInput.getKeyboardIntegerInput()
        self.__repository.saveCurrentRoutingState(userChoice)

        # 필요하다면 여기 중간에 몇 가지 작업들이 더 처리 될 수 있습니다.
        transmitQueue.put(userChoice)


