from console_ui.entity.ConsoleUiRoutingState import ConsoleUiRoutingState
from console_ui.entity.ConsoleUiState import ConsoleUiState
from console_ui.entity.Session import Session
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from custom_protocol.entity.CustomProtocol import CustomProtocol
from utility.keyboard.KeyboardInput import KeyboardInput
from product.response.ProductReadResponse import ProductReadResponse



class ConsoleUiRepositoryImpl(ConsoleUiRepository):
    __instance = None
    __sessionId = -1
    __productId = None
    __uiMenuTable = {}
    # restrictUserInput
    __nothingLogout = [0, 3]
    __nothingNum = [0, 4]
    __productMenuNum = [0, 7]
    __productMenuLogout = [0, 2, 5, 7]
    __productInfoNum = [0, 7]
    __productInfoLogout = [0, 2, 5, 7]
    __orderList = [0, 3]


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__setSessionId()

            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.NOTHING.value] = cls.__instance.__printDefaultMenu
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_REGISTER.value] = cls.__instance.__printAccountRegister
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_LOGIN.value] = cls.__instance.__printAccountLogin
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_LOGOUT.value] = cls.__instance.__printAccountLogout
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_DELETE.value] = cls.__instance.__printAccountDelete
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_LIST.value] = cls.__instance.__printProductList
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_INFO.value] = cls.__instance.__printProductInfo
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_ADD.value] = cls.__instance.__printProductAdd
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_DELETE.value] = cls.__instance.__printProductDelete
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_EDIT.value] = cls.__instance.__printProductEdit
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ORDER_PURCHASE.value] = cls.__instance.__printOrderPurchase
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ORDER_LIST.value] = cls.__instance.__printProductEdit



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

    def aquireSessionId(self):
        return self.__sessionId

    def aquireProductId(self):
        return self.__productId

    def restrictUserInput(self):
        CurrentRoutingState = self.acquireCurrentRoutingState()
        restrictChoice = [0, 10] # 임시
        if self.__sessionId == -1:
            if CurrentRoutingState == ConsoleUiRoutingState.NOTHING or \
                    CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGIN or \
                    CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGOUT or \
                    CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_REGISTER or \
                    CurrentRoutingState == ConsoleUiRoutingState.ORDER_PURCHASE or \
                    CurrentRoutingState == ConsoleUiRoutingState.ORDER_DELETE:
                restrictChoice = self.__nothingLogout
                while (True):
                    userChoice = KeyboardInput.getKeyboardIntegerInput('\033[95m'+"원하는 선택지를 입력하세요.:"+'\033[0m')
                    if restrictChoice[0] <= userChoice <= restrictChoice[1]:
                        return userChoice
                    print("다시 입력 해주세요.")

            if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_LIST or \
                    CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_ADD or \
                    CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_DELETE or \
                    CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_EDIT:
                restrictChoice = self.__productMenuLogout
            if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_INFO:
                restrictChoice = self.__productInfoLogout
            while(True):
                userChoice = KeyboardInput.getKeyboardIntegerInput('\033[95m'+"원하는 선택지를 입력하세요.:"+'\033[0m')
                if restrictChoice[1] <= userChoice <= restrictChoice[2]:
                    print("로그인을 해야 이용 가능합니다.")
                if restrictChoice[0] <= userChoice < restrictChoice[1] or \
                        restrictChoice[2] < userChoice <= restrictChoice[3]:
                    return userChoice
                print("다시 입력 해주세요.")

        if CurrentRoutingState == ConsoleUiRoutingState.NOTHING or \
            CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGIN or \
            CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGOUT or \
            CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_REGISTER or \
            CurrentRoutingState == ConsoleUiRoutingState.ORDER_PURCHASE or \
            CurrentRoutingState == ConsoleUiRoutingState.ORDER_DELETE:
            restrictChoice = self.__nothingNum
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_LIST or \
            CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_ADD or \
            CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_DELETE or \
            CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_EDIT:
            restrictChoice = self.__productMenuNum
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_INFO:
            restrictChoice = self.__productInfoNum
        if CurrentRoutingState == ConsoleUiRoutingState.ORDER_LIST:
            restrictChoice = self.__orderList

        while(True):
            userChoice = KeyboardInput.getKeyboardIntegerInput('\033[95m'+"원하는 선택지를 입력하세요.:"+'\033[0m')
            if restrictChoice[0] <= userChoice <= restrictChoice[1]:
                return userChoice
            print("다시 입력 해주세요.")




    def userInputConverter(self, userChoice):
        CurrentRoutingState = self.acquireCurrentRoutingState()
        print(f"Current Routing State: {CurrentRoutingState}")
        if self.__sessionId == -1:
            if CurrentRoutingState == ConsoleUiRoutingState.NOTHING or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGIN or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGOUT or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_REGISTER or \
                CurrentRoutingState == ConsoleUiRoutingState.ORDER_PURCHASE or \
                CurrentRoutingState == ConsoleUiRoutingState.ORDER_DELETE:
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
                CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_DELETE or \
                    CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_EDIT:
                if userChoice == 1:
                    return CustomProtocol.PRODUCT_INFO.value
                if userChoice == 2:
                    return CustomProtocol.PRODUCT_ADD.value
                if userChoice == 3:
                    return CustomProtocol.PRODUCT_EDIT.value
                if userChoice == 4:
                    return CustomProtocol.PRODUCT_DELETE.value
                if userChoice == 5:
                    return CustomProtocol.ORDER_LIST.value
                if userChoice == 6:
                    return CustomProtocol.ACCOUNT_LOGIN.value
                if userChoice == 7:
                    return CustomProtocol.ACCOUNT_REGISTER.value
                if userChoice == 0:
                    return CustomProtocol.PROGRAM_CLOSE.value
            if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_INFO:
                if userChoice == 1:
                    return CustomProtocol.PRODUCT_LIST.value
                if userChoice == 2:
                    return CustomProtocol.ORDER_PURCHASE.value
                if userChoice == 3:
                    return CustomProtocol.PRODUCT_EDIT.value
                if userChoice == 4:
                    return CustomProtocol.PRODUCT_DELETE.value
                if userChoice == 5:
                    return CustomProtocol.ORDER_LIST.value
                if userChoice == 6:
                    return CustomProtocol.ACCOUNT_LOGIN.value
                if userChoice == 7:
                    return CustomProtocol.ACCOUNT_REGISTER.value
                if userChoice == 0:
                    return CustomProtocol.PROGRAM_CLOSE.value

        if CurrentRoutingState == ConsoleUiRoutingState.NOTHING or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGIN or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_LOGOUT or \
                CurrentRoutingState == ConsoleUiRoutingState.ACCOUNT_REGISTER or \
                CurrentRoutingState == ConsoleUiRoutingState.ORDER_PURCHASE or \
                CurrentRoutingState == ConsoleUiRoutingState.ORDER_DELETE:
            if userChoice == 1:
                return CustomProtocol.ACCOUNT_LOGOUT.value
            if userChoice == 2:
                return CustomProtocol.ACCOUNT_DELETE.value
            if userChoice == 3:
                return CustomProtocol.PRODUCT_LIST.value
            if userChoice == 4:
                return CustomProtocol.ORDER_LIST.value
            if userChoice == 0:
                return CustomProtocol.PROGRAM_CLOSE.value
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_LIST or \
                CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_ADD or \
                CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_DELETE or \
                CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_EDIT:
            if userChoice == 1:
                return CustomProtocol.PRODUCT_INFO.value
            if userChoice == 2:
                return CustomProtocol.PRODUCT_ADD.value
            if userChoice == 3:
                return CustomProtocol.PRODUCT_EDIT.value
            if userChoice == 4:
                return CustomProtocol.PRODUCT_DELETE.value
            if userChoice == 5:
                return CustomProtocol.ORDER_LIST.value
            if userChoice == 6:
                return CustomProtocol.ACCOUNT_LOGOUT.value
            if userChoice == 7:
                return CustomProtocol.ACCOUNT_DELETE.value
            if userChoice == 0:
                return CustomProtocol.PROGRAM_CLOSE.value
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_INFO:
            if userChoice == 1:
                return CustomProtocol.PRODUCT_LIST.value
            if userChoice == 2:
                return CustomProtocol.ORDER_PURCHASE.value
            if userChoice == 3:
                return CustomProtocol.PRODUCT_EDIT.value
            if userChoice == 4:
                return CustomProtocol.PRODUCT_DELETE.value
            if userChoice == 5:
                return CustomProtocol.ORDER_LIST.value
            if userChoice == 6:
                return CustomProtocol.ACCOUNT_LOGOUT.value
            if userChoice == 7:
                return CustomProtocol.ACCOUNT_DELETE.value
            if userChoice == 0:
                return CustomProtocol.PROGRAM_CLOSE.value
        if CurrentRoutingState == ConsoleUiRoutingState.ORDER_LIST:
            if userChoice == 1:
                return CustomProtocol.ORDER_DELETE.value
            if userChoice == 2:
                return CustomProtocol.PRODUCT_LIST.value
            if userChoice == 3:
                return CustomProtocol.ACCOUNT_LOGOUT.value
            if userChoice == 0:
                return CustomProtocol.PROGRAM_CLOSE.value


        print(f"userChoice: {userChoice}")
        return userChoice



    def printMenu(self):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()
        print(f"Current Routing State: {currentRoutingState}")
        menu = self.__uiMenuTable[currentRoutingState.value]
        menu()


    def printMenuResponse(self, response):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()
        print(f"response: {response}")
        print(f"Current Routing State: {currentRoutingState}")
        if self.__isResponseNotFalse(response) == False:
            currentRoutingState = self.__consoleUiState.revertToDefaultState()
            menu = self.__uiMenuTable[currentRoutingState.value]
            menu()
        else:
            menu = self.__uiMenuTable[currentRoutingState.value]
            menu(response)


    def __printDefaultMenu(self):
        #세션 로그인 확인 필요
        if self.__sessionId == -1:
            print('\033[30m \033[103m'+"[][] 메뉴 [][]"+'\033[0m')
            print("1. 로그인")
            print("2. 회원가입")
            print("3. 상품 목록")
            print("0. 종료")
            return

        print('\033[30m \033[103m'+"[][] 메뉴 [][]"+'\033[0m')
        print("1. 로그아웃")
        print("2. 회원 탈퇴")
        print("3. 상품 목록")
        print("4. 주문 내역")
        print("0. 종료")

    def __setSessionId(self):
        self.__session = Session()


    def __printAccountLogin(self, response):
        print(response['message'])
        sessionid = response['sessionAccountId']
        self.__sessionId = sessionid
        Session().set_session_id(self.__sessionId)

        checksessionid = self.__sessionId
        print(f"sessionid: {checksessionid}")

        self.__printDefaultMenu()

    def __printAccountRegister(self, response):
        print("회원가입 성공")
        self.__printDefaultMenu()

    def __printAccountLogout(self, response):
        print("로그아웃 성공")
        self.__sessionId = -1
        Session().set_session_id(self.__sessionId)
        checksessionid = self.__sessionId
        print(f"sessionid: {checksessionid}")
        self.__printDefaultMenu()

    def __printAccountDelete(self, response):
        print("회원탈퇴 성공")
        self.__sessionId = -1
        Session().set_session_id(self.__sessionId)
        checksessionid = self.__sessionId
        print(f"sessionid: {checksessionid}")
        self.__printDefaultMenu()

    def __printProductMenu(self, response=None):
        # 세션 확인해서 로그인중이면 로그아웃만 뜨게해야함
        if self.__sessionId == -1:
            print("1. 상품 조회")
            print("2. 상품 추가")
            print("3. 상품 수정")
            print("4. 상품 삭제")
            print("5. 주문 내역")
            print("6. 로그인")
            print("7. 회원가입")
            print("0. 종료")
            return

        print("1. 상품 조회")
        print("2. 상품 추가")
        print("3. 상품 수정")
        print("4. 상품 삭제")
        print("5. 주문 내역")
        print("6. 로그아웃")
        print("7. 회원 탈퇴")
        print("0. 종료")

    def __printProductList(self, response):
        print('\033[31m \033[107m'+"[][] 상품 목록 [][]"+'\033[0m')
        try:
            for i in response:
                print(f"name: {i['__productName']}, price: {i['__productPrice']}")
            self.__printProductMenu()
        except Exception as e:
            self.__printDefaultMenu()


    def __printProductInfo(self, response=None):
        print('\033[31m \033[107m'+"[][] 상품 조회 [][]"+'\033[0m')
        self.__productId = response['__productId']
        print("------------------------")
        print(f"name : {response['__productName']}")
        print(f"price : {response['__productPrice']}")
        print(f"info : {response['__productInfo']}")
        print("------------------------")

        #세션 로그인 확인 필요
        if self.__sessionId == -1:
            print("1. 상품 목록")
            print("2. 상품 주문")
            print("3. 상품 수정")
            print("4. 상품 삭제")
            print("5. 주문 내역")
            print("6. 로그인")
            print("7. 회원가입")
            print("0. 종료")
            return


        print("1. 상품 목록")
        print("2. 상품 주문")
        print("3. 상품 수정")
        print("4. 상품 삭제")
        print("5. 주문 내역")
        print("6. 로그아웃")
        print("7. 회원탈퇴")
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

    def __printProductEdit(self, response):
        print("상품 수정 성공")
        print("상품 수정 실패")
        self.__printProductMenu()

        
    def __printOrderPurchase(self, response):
        print("주문 성공")
        print("주문 실패")

        self.__printDefaultMenu()

    def __printOrderList(self, response):
        print("주문 내역")

        for i in response:
            print(f"name: {i['__productName']}, price: {i['__productPrice']}")

        print("주문 내역 메뉴")
        print("1. 주문 취소")
        print("2. 상품 목록")
        print("3. 로그아웃")
        print("0. 종료")

    def __printOrderDelete(self, response):
        print("주문 취소 성공")
        print("주문 취소 실패")

        self.__printDefaultMenu()

    def __isResponseNotFalse(self, response):
        print("check response is bool")
        result = None
        try:
            result = response['__success']
        except:
            result = True
        finally:
            print(f"response is: {result}")
            return result

