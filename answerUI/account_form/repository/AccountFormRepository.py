import abc


class AccountFormRepository(abc.ABC):
    @abc.abstractmethod
    def createAccountRegisterForm(self):
        pass


    @abc.abstractmethod
    def AccountLoginForm(self):
        pass

    @abc.abstractmethod
    def AccountLogoutForm(self):
        pass

    @abc.abstractmethod
    def AccountDeleteForm(self):
        pass

