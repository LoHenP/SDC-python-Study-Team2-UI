from console_ui.entity.ConsoleUiRoutingState import ConsoleUiRoutingState
from console_ui.entity.ConsoleUiState import ConsoleUiState
from console_ui.entity.Session import Session
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from custom_protocol.entity.CustomProtocol import CustomProtocol
from utility.keyboard.KeyboardInput import KeyboardInput
from product.response.ProductReadResponse import ProductReadResponse



class ConsoleUiRepositoryImpl(ConsoleUiRepository):
    __instance = None
    __uiMenuTable = {}
    __nothingNum = [0, 3]
    __productMenuNum = [0, 6]
    __productInfoNum = [0, 5]

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.NOTHING.value] = cls.__instance.__printDefaultMenu
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_REGISTER.value] = cls.__instance.__printAccountRegister
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_LOGIN.value] = cls.__instance.__printAccountLogin
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_LOGOUT.value] = cls.__instance.__printAccountLogout
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_LIST.value] = cls.__instance.__printProductList
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_INFO.value] = cls.__instance.__printProductInfo
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_ADD.value] = cls.__instance.__printProductAdd
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_DELETE.value] = cls.__instance.__printProductDelete







        return cls.__instance

    def __init__(self):
        print("ConsoleUiRepository 초기화 동작")

        self.__consoleUiState = ConsoleUiState()
        self.__session = Session()

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


    def restrictUserInput(self):
        CurrentRoutingState = self.acquireCurrentRoutingState()
        restrictChoice = [0, 10] # 임시
        if CurrentRoutingState == ConsoleUiRoutingState.NOTHING or \
            CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGIN or \
            CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGOUT or \
            CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_REGISTER:
            restrictChoice = self.__nothingNum
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_LIST or \
            CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_ADD or \
            CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_DELETE:
            restrictChoice = self.__productMenuNum
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_INFO:
            restrictChoice = self.__productInfoNum

        while(True):
            userChoice = KeyboardInput.getKeyboardIntegerInput("원하는 선택지를 입력하세요.")
            if restrictChoice[0] <= userChoice <= restrictChoice[1]:
                return userChoice
            print("다시 입력 해주세요.")




    def userInputConverter(self, userChoice):
        CurrentRoutingState = self.acquireCurrentRoutingState()
        print(f"Current Routing State: {CurrentRoutingState}")
        if self.__session.get_session_id() == -1:
            if CurrentRoutingState == ConsoleUiRoutingState.NOTHING or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGIN or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGOUT or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_REGISTER:
                if userChoice == 1:
                    return CustomProtocol.ACCOUNT_LOGIN.value
                if userChoice == 2:
                    return CustomProtocol.ACCOUNT_REGISTER.value
                if userChoice == 3:
                    return CustomProtocol.PRODUCT_LIST.value
                if userChoice == 0:
                    return CustomProtocol.PROGRAM_CLOSE.value
            if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_LIST or \
                CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_ADD or \
                CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_DELETE:
                if userChoice == 1:
                    return CustomProtocol.PRODUCT_INFO.value
                if userChoice == 2:
                    return CustomProtocol.PRODUCT_ADD.value
                if userChoice == 3:
                    return CustomProtocol.PRODUCT_EDIT.value
                if userChoice == 4:
                    return CustomProtocol.PRODUCT_DELETE.value
                if userChoice == 5:
                    return CustomProtocol.ACCOUNT_LOGIN.value
                if userChoice == 6:
                    return CustomProtocol.ACCOUNT_REGISTER.value
                if userChoice == 0:
                    return CustomProtocol.PROGRAM_CLOSE.value
            if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_INFO:
                if userChoice == 1:
                    return CustomProtocol.PRODUCT_LIST.value
                if userChoice == 2:
                    return CustomProtocol.PRODUCT_EDIT.value
                if userChoice == 3:
                    return CustomProtocol.PRODUCT_DELETE.value
                if userChoice == 4:
                    return CustomProtocol.ACCOUNT_LOGIN.value
                if userChoice == 5:
                    return CustomProtocol.ACCOUNT_REGISTER.value
                if userChoice == 0:
                    return CustomProtocol.PROGRAM_CLOSE.value

        if CurrentRoutingState == ConsoleUiRoutingState.NOTHING or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGIN or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGOUT or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_REGISTER:
            if userChoice == 1:
                return CustomProtocol.ACCOUNT_LOGOUT.value
            if userChoice == 2:
                return CustomProtocol.ACCOUNT_DELETE.value
            if userChoice == 3:
                return CustomProtocol.PRODUCT_LIST.value
            if userChoice == 0:
                return CustomProtocol.PROGRAM_CLOSE.value
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_LIST or \
                CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_ADD or \
                CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_DELETE:
            if userChoice == 1:
                return CustomProtocol.PRODUCT_INFO.value
            if userChoice == 2:
                return CustomProtocol.PRODUCT_ADD.value
            if userChoice == 3:
                return CustomProtocol.PRODUCT_EDIT.value
            if userChoice == 4:
                return CustomProtocol.PRODUCT_DELETE.value
            if userChoice == 5:
                return CustomProtocol.ACCOUNT_LOGOUT.value
            if userChoice == 6:
                return CustomProtocol.ACCOUNT_DELETE.value
            if userChoice == 0:
                return CustomProtocol.PROGRAM_CLOSE.value
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_INFO:
            if userChoice == 1:
                return CustomProtocol.PRODUCT_LIST.value
            if userChoice == 2:
                return CustomProtocol.PRODUCT_EDIT.value
            if userChoice == 3:
                return CustomProtocol.PRODUCT_DELETE.value
            if userChoice == 4:
                return CustomProtocol.ACCOUNT_LOGOUT.value
            if userChoice == 5:
                return CustomProtocol.ACCOUNT_DELETE.value
            if userChoice == 0:
                return CustomProtocol.PROGRAM_CLOSE.value
        return userChoice



    def printMenu(self):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()

        menu = self.__uiMenuTable[currentRoutingState.value]
        menu()


    def printMenuResponse(self, response):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()

        menu = self.__uiMenuTable[currentRoutingState.value]
        menu(response)

    def __printDefaultMenu(self):
        #세션 로그인 확인 필요
        if self.__session.get_session_id() == -1:
            print("메뉴")
            print("1. 로그인")
            print("2. 회원가입")
            print("3. 상품 목록")
            print("0. 종료")
            return

        print("메뉴")
        print("1. 로그아웃")
        print("2. 회원 탈퇴")
        print("3. 상품 목록")
        print("0. 종료")

    def __printAccountLogin(self, response):
        print(response['message'])
        sessionid = response['sessionAccountId']
        self.__session.set_session_id(sessionid)

        checksessionid = self.__session.get_session_id()
        print(f"sessionid: {checksessionid}")

        self.__printDefaultMenu()

    def __printAccountRegister(self, response):
        print("회원가입 성공")
        self.__printDefaultMenu()

    def __printAccountLogout(self, response):
        print("로그아웃 성공")
        self.__session.set_session_id(-1)
        checksessionid = self.__session.get_session_id()
        print(f"sessionid: {checksessionid}")
        self.__printDefaultMenu()

    def __printProductMenu(self):
        # 세션 확인해서 로그인중이면 로그아웃만 뜨게해야함
        if self.__session.get_session_id() == -1:
            print("1. 상품 조회")
            print("2. 상품 추가")
            print("3. 상품 수정")
            print("4. 상품 삭제")
            print("5. 로그인")
            print("6. 회원가입")
            print("0. 종료")
            return

        print("1. 상품 조회")
        print("2. 상품 추가")
        print("3. 상품 수정")
        print("4. 상품 삭제")
        print("5. 로그아웃")
        print("6. 회원 탈퇴")
        print("0. 종료")

    def __printProductList(self, response):
        print("상품목록")

        for i in response:
            print(f"id: {i['id']}, name: {i['name']}, price: {i['price']}")
        self.__printProductMenu()

    def __printProductInfo(self, response):
        print("상품 조회")
        print("------------------------")
        print(f"")
        print("------------------------")

        #세션 로그인 확인 필요
        if self.__session.get_session_id() == -1:
            print("1. 상품 목록")
            print("2. 상품 수정")
            print("3. 상품 삭제")
            print("4. 로그인")
            print("5. 회원가입")
            print("0. 종료")
            return


        print("1. 상품 목록")
        print("2. 상품 수정")
        print("3. 상품 삭제")
        print("4. 로그아웃")
        print("5. 회원탈퇴")
        print("0. 종료")


    def __printProductAdd(self, response):
        #response 에서 실패 성공 받아서 둘중하나 출력
        print("상품 추가 완료")
        print("상품 추가 실패")

        self.__printProductMenu()

    def __printProductDelete(self, response):
        #response 에서 실패 성공 받아서 둘중하나 출력
        print("상품 삭제 성공")
        print("상품 삭제 실패")

        self.__printProductMenu()
