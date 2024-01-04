import ast

from custom_protocol.entity.CustomProtocol import CustomProtocol
from request_generator.service.RequestGeneratorService import RequestGeneratorService


class RequestGeneratorServiceImpl(RequestGeneratorService):
    __instance = None
    __requestFormGenerationTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__requestFormGenerationTable[CustomProtocol.ACCOUNT_REGISTER.value] = cls.__instance.generateAccountRegisterRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGIN.value] = cls.__instance.generateAccountLoginRequest
            cls.__requestFormGenerationTable[CustomProtocol.ACCOUNT_LOGOUT.value] = cls.__instance.generateAccountLogoutRequest
            cls.__requestFormGenerationTable[CustomProtocol.ACCOUNT_DELETE.value] = cls.__instance.generateAccountDeleteRequest
            cls.__requestFormGenerationTable[CustomProtocol.PRODUCT_INFO.value] = cls.__instance.generateProductInfoRequest
            cls.__requestFormGenerationTable[CustomProtocol.PRODUCT_ADD.value] = cls.__instance.generateProductAddRequest
            cls.__requestFormGenerationTable[CustomProtocol.PRODUCT_DELETE.value] = cls.__instance.generateProductDeleteRequest
            cls.__requestFormGenerationTable[CustomProtocol.PRODUCT_EDIT.value] = cls.__instance.generateProductEditRequest
            cls.__requestFormGenerationTable[CustomProtocol.ORDER_PURCHASE.value] = cls.__instance.generateOrderPurchaseRequest
            cls.__requestFormGenerationTable[CustomProtocol.ORDER_LIST.value] = cls.__instance.generateOrderListRequest


        return cls.__instance

    def __init__(self):
        print("RequestGeneratorServiceImpl 생성자 호출")


    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    # 사실 이 부분은 python Dictionary를 사용하여 개선하는 것이 더 좋음
    def findRequestGenerator(self, protocolNumber):
        print("RequestGeneratorService: request generator를 찾아옵니다")
        if self.__requestFormGenerationTable[protocolNumber] is not None:
            return self.__requestFormGenerationTable[protocolNumber]

        else:
            print(f"이 프로토콜 번호({protocolNumber}) 를 처리 할 수 있는 함수가 없습니다.")

    def generateAccountRegisterRequest(self, arguments, sessionId):
        print("RequestGeneratorService: register form")
        print(f"arguments의 타입: {type(arguments)}")
        print(f"지금부터 request를 생성합니다: {arguments}")

        if not isinstance(arguments, tuple) or len(arguments) != 2:
            raise ValueError("Invalid request format")

        print("make account request dictionary")

        accountRequestData = {
            '__accountId': arguments[0].decode().strip(),
            '__password': arguments[1].decode().strip(),
        }

        return accountRequestData

    def generateAccountLoginRequest(self, arguments, sessionId):
        print("RequestGeneratorService: login form")

        if not isinstance(arguments, tuple) or len(arguments) != 2:
            raise ValueError("Invalid request format")

        accountRequestData = {
            '__accountId': arguments[0].decode().strip(),
            '__password': arguments[1].decode().strip(),
        }

        return accountRequestData

    def generateAccountLogoutRequest(self, arguments, sessionId):
        print("RequestGeneratorService: Account Logout form")

        accountRequestData = {
            '__accountSessionId': sessionId[0]
        }

        return accountRequestData

    def generateAccountDeleteRequest(self, arguments, sessionId):
        print("RequestGeneratorService: account delete form")

        accountRequestData = {
            '__accountSessionId': sessionId[0]
        }

        return accountRequestData

    def generateProductInfoRequest(self, arguments, sessionId):
        print("RequestGeneratorService: product Info form")

        productRequestData = {
            '__productId': arguments
        }

        return productRequestData


    def generateProductAddRequest(self, arguments, sessionId):
        print("RequestGeneratorService: product add")

        if not isinstance(arguments, tuple) or len(arguments) != 3:
            raise ValueError("Invalid request format")

        productRequestData = {
            '__productName': arguments[0].decode().strip(),
            '__productPrice': arguments[1],
            '__productInfo': arguments[2].decode().strip()
        }

        return productRequestData

    def generateProductDeleteRequest(self, arguments, sessionId):
        print("RequestGeneratorService: product delete form")

        productRequestData = {
            '__productId': arguments
        }

        return productRequestData

    def generateProductEditRequest(self, arguments, sessionId):
        print("RequestGeneratorService: product edit")

        if not isinstance(arguments, tuple) or len(arguments) != 4:
            raise ValueError("Invalid request format")

        productRequestData = {
            '__productId': arguments[0],
            '__productName': arguments[1].decode().strip(),
            '__productPrice': arguments[2],
            '__productInfo': arguments[3].decode().strip()
        }

        return productRequestData

    def generateOrderPurchaseRequest(self, arguments, sessionId):
        print("RequestGeneratorService: order purchase form")

        orderRequestData = {
            '__productId': sessionId[1],
            '__accountSessionId': sessionId[0]
        }

        return orderRequestData

    def generateOrderListRequest(self, arguments, sessionId):
        print("RequestGeneratorService: order list form")

        orderRequestData = {
            '__accountSessionId': sessionId[0]
        }

        return orderRequestData