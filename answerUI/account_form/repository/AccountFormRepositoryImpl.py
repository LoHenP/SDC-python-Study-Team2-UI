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
        userInputId = KeyboardInput.getKeyboardInput('\033[95m'+"아이디를 입력하세요: "+'\033[0m')
        userInputPassword = KeyboardInput.getKeyboardInput('\033[95m'+"비밀번호를 입력하세요: "+'\033[0m')
        return userInputId, userInputPassword


    def AccountLoginForm(self):
        userInputId = KeyboardInput.getKeyboardInput('\033[95m'+"아이디를 입력하세요: "+'\033[0m')
        userInputPassword = KeyboardInput.getKeyboardInput('\033[95m'+"비밀번호를 입력하세요: "+'\033[0m')
        return userInputId, userInputPassword

    def AccountLogoutForm(self):
        print('\033[31m \033[107m'+" 로그아웃합니다. "+'\033[0m')
        return

    def AccountDeleteForm(self):
        print('\033[31m \033[107m'+" 회원 탈퇴를 진행합니다. "+'\033[0m')
        return
        # userInputId = KeyboardInput.getKeyboardInput("아이디를 입력하세요:")
        # userInputPassword = KeyboardInput.getKeyboardInput("비밀번호를 입력하세요:")
        # userInputTrans = KeyboardInput.getKeyboardInput('\033[31m'+"회원 탈퇴를 진행할까요? (y/n):"+'\033[0m')
        # if userInputTrans is not None:
        #     # b'입력값\n 을 입력값 으로 변환 (예를들어 b'y\n 을 y 으로 변환)
        #     newUserInputTrans = userInputTrans.decode().strip()
        #     print(userInputId, userInputPassword, newUserInputTrans)
        # if newUserInputTrans == "y" or newUserInputTrans == "Y":
        #     return userInputId, userInputPassword
        # else:
        #     # 회원 탈퇴를 취소할 경우 되돌아가는 경로가 필요함
        #     return

    def createProgramCloseForm(self):
        print("프로그램을 종료합니다.")
        return
