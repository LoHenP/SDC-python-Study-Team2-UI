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

    def processUserInput(self, transmitQueue):
        if self.__session is None:
            print("메뉴")
            print("1. 로그인")
            print("2. 회원 가입")
            print("3. 상품 목록")
            print("4. 종료")
        else:
            print("1. 로그 아웃")
            print("2. 상품 목록")
            print("3. 구매 목록 조회")
            print("4. 회원 탈퇴")
            print("5. 종료")

        # if not receiveQueue.empty():
        #     sessionid = receiveQueue.get()
        #     self.__session = Session(sessionid)

        userChoice = KeyboardInput.getKeyboardIntegerInput()
        self.__repository.saveCurrentRoutingState(userChoice)

        # 필요하다면 여기 중간에 몇 가지 작업들이 더 처리 될 수 있습니다.
        transmitQueue.put(userChoice)


