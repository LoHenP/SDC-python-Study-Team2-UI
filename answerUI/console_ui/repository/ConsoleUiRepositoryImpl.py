from console_ui.entity.ConsoleUiRoutingState import ConsoleUiRoutingState
from console_ui.entity.ConsoleUiState import ConsoleUiState
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from custom_protocol.entity.CustomProtocol import CustomProtocol


class ConsoleUiRepositoryImpl(ConsoleUiRepository):
    __instance = None
    __uiMenuTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.NOTHING.value] = cls.__instance.__printDefaultMenu
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_REGISTER.value] = cls.__instance.__printDefaultMenu
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_LIST.value] = cls.__instance.__printProductList
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_LOGIN.value] = cls.__instance.__printDefaultMenu




        return cls.__instance

    def __init__(self):
        print("ConsoleUiRepository 초기화 동작")

        self.__consoleUiState = ConsoleUiState()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def saveCurrentRoutingState(self, currentState):
        self.__consoleUiState.setCurrentRoutingState(currentState)

    def acquireCurrentRoutingState(self):
        return self.__consoleUiState.getCurrentRoutingState()

    # 현재 시점에 약간 애매함
    def saveRequestFormToTransmitQueue(self):
        pass

    def printMenu(self):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()

        menu = self.__uiMenuTable[currentRoutingState.value]
        menu()


    def __printProductList(self):
        print("상품목록")


    def __printDefaultMenu(self):

        print("메뉴")
        print("1. 로그인")
        print("2. 회원가입")
        print("5. 상품 목록")
        print("6. 상품 조회")
