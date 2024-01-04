from account_form.repository.AccountFormRepository import AccountFormRepository
from custom_protocol.entity.CustomProtocol import CustomProtocol

from utility.keyboard.KeyboardInput import KeyboardInput


class AccountFormRepositoryImpl(AccountFormRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("AccountFormRepositoryImpl 초기화 동작")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createAccountRegisterForm(self):
        userInputId = KeyboardInput.getKeyboardInput("아이디를 입력하세요:")
        userInputPassword = KeyboardInput.getKeyboardInput("비밀번호를 입력하세요:")
        return userInputId, userInputPassword


    def AccountLoginForm(self):
        userInputId = KeyboardInput.getKeyboardInput("아이디를 입력하세요:")
        userInputPassword = KeyboardInput.getKeyboardInput("비밀번호를 입력하세요:")
        return userInputId, userInputPassword

    def AccountLogoutForm(self):
        print("로그아웃합니다.")
        return

    def AccountDeleteForm(self):
        print('\033[31m'+"회원 탈퇴를 진행합니다."+'\033[0m')
        userInputId = KeyboardInput.getKeyboardInput("아이디를 입력하세요:")
        userInputPassword = KeyboardInput.getKeyboardInput("비밀번호를 입력하세요:")
        return userInputId, userInputPassword
        # userInputTrans = KeyboardInput.getKeyboardInput('\033[31m'+"회원 탈퇴를 진행할까요? (y/n):"+'\033[0m')
        # print(userInputId, userInputPassword, userInputTrans)
        # if userInputTrans == "b'y\n" or userInputTrans == "b'Y\n":
        #     return userInputId, userInputPassword
        # else:
        #     # 회원 탈퇴를 취소할 경우 되돌아가는 경로가 필요함
        #     return None, None

    def createProgramCloseForm(self):
        return
