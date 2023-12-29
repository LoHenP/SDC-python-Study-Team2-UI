from custom_protocol.entity.CustomProtocol import CustomProtocol
from product_form.repository.ProductFormRepository import ProductFormRepository

from utility.keyboard.KeyboardInput import KeyboardInput


class ProductFormRepositoryImpl(ProductFormRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("ProductFormRepositoryImpl 초기화")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createProductListForm(self):
        return CustomProtocol.PRODUCT_LIST.value

    def createProductCheckForm(self):
        productCheckNum = KeyboardInput.getKeyboardInput("상품 번호를 입력하세요.")
        return productCheckNum, productCheckNum

    def createProductAddForm(self):
        productName = KeyboardInput.getKeyboardInput("상품 이름을 입력하세요.")
        productInfo = KeyboardInput.getKeyboardInput("상품 정보를 입력하세요.")
        return productName, productInfo
