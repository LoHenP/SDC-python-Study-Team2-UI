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
            cls.__requestFormGenerationTable[CustomProtocol.ACCOUNT_DELETE.value] = cls.__instance.generateAccountDeleteRequest
            cls.__requestFormGenerationTable[CustomProtocol.PRODUCT_INFO.value] = cls.__instance.generateProductInfoRequest
            cls.__requestFormGenerationTable[CustomProtocol.PRODUCT_ADD.value] = cls.__instance.generateProductAddRequest
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

    def generateAccountRegisterRequest(self, arguments):
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

    def generateAccountLoginRequest(self, arguments):
        print("RequestGeneratorService: login form")

        if not isinstance(arguments, tuple) or len(arguments) != 2:
            raise ValueError("Invalid request format")

        accountRequestData = {
            '__accountId': arguments[0].decode().strip(),
            '__password': arguments[1].decode().strip(),
        }

        return accountRequestData

    def generateAccountDeleteRequest(self, arguments):
        print("RequestGeneratorService: account delete form")

        if not isinstance(arguments, tuple) or len(arguments) != 2:
            raise ValueError("Invalid request format")

        accountRequestData = {
            '__accountId': arguments[0].decode().strip(),
            '__password': arguments[1].decode().strip(),
        }

        return accountRequestData


    def generateProductInfoRequest(self, arguments):
        print("RequestGeneratorService: product Info form")

        productRequestData = {
            '__data': arguments
        }

        return productRequestData


    def generateProductAddRequest(self, arguments):
        print("RequestGeneratorService: product add")

        if not isinstance(arguments, tuple) or len(arguments) != 3:
            raise ValueError("Invalid request format")

        productRequestData = {
            '__productName': arguments[0].decode().strip(),
            '__productprice': arguments[1],
            '__productinfo': arguments[2].decode().strip()
        }

        return productRequestData

    def generateOrderPurchaseRequest(self, arguments):
        print("RequestGeneratorService: order purchase form")

        orderRequestData = {
            '__orderId': arguments
        }

        return orderRequestData

    def generateOrderListRequest(self, arguments):
        print("RequestGeneratorService: order list form")

        orderRequestData = {
            '__orderList': arguments
        }

        return orderRequestData