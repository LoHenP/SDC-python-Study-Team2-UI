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
        return

    def createProductInfoForm(self):
        productInfoNum = KeyboardInput.getKeyboardIntegerInput("상품 번호를 입력하세요.")
        return productInfoNum

    def createProductAddForm(self):
        productName = KeyboardInput.getKeyboardInput("상품 이름을 입력하세요.")
        productPrice = KeyboardInput.getKeyboardIntegerInput("상품 가격을 입력하세요.")
        productInfo = KeyboardInput.getKeyboardInput("상품 정보를 입력하세요.")
        return productName, productPrice, productInfo

    def createProductDeleteForm(self):
        productNum = KeyboardInput.getKeyboardIntegerInput("삭제할 상품 번호를 입력하세요.")
        return productNum

    def createProductEditForm(self):
        productEditNum = KeyboardInput.getKeyboardIntegerInput("수정할 상품의 번호를 입력하세요.")
        productEditName = KeyboardInput.getKeyboardInput("수정할 상품의 이름을 입력하세요.")
        productEditPrice = KeyboardInput.getKeyboardIntegerInput("수정할 상품의 가격을 입력하세요.")
        productEditInfo = KeyboardInput.getKeyboardInput("수정할 상품의 내용을 입력하세요.")
        return productEditNum, productEditName, productEditPrice, productEditInfo