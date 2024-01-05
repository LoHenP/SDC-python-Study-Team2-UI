import multiprocessing
import socket
import sys
from time import sleep
from decouple import config

from account_form.repository.AccountFormRepositoryImpl import AccountFormRepositoryImpl
from order_form.repository.OrderFormRepositoryImpl import OrderFormRepositoryImpl
from product_form.repository.ProductFormRepositoryImpl import ProductFormRepositoryImpl

# pip3 install python-decouple

from client_socket.repository.ClientSocketRepositoryImpl import ClientSocketRepositoryImpl
from client_socket.service.ClientSocketServiceImpl import ClientSocketServiceImpl
from console_printer.repository.ConsolePrinterRepositoryImpl import ConsolePrinterRepositoryImpl
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl
from custom_protocol.entity.CustomProtocol import CustomProtocol
from custom_protocol.service.CustomProtocolServiceImpl import CustomProtocolServiceImpl
from task_manage.repository.TaskManageRepository import TaskManageRepository
from task_manage.repository.TaskManageRepositoryImpl import TaskManageRepositoryImpl
from task_manage.service.TaskManageServiceImpl import TaskManageServiceImpl


def initServerSocketDomain():
    clientSocketRepository = ClientSocketRepositoryImpl()
    ClientSocketServiceImpl(clientSocketRepository)


def initTaskManageDomain():
    taskManageRepository = TaskManageRepositoryImpl()
    TaskManageServiceImpl(taskManageRepository)


def initConsolePrinterDomain():
    consoleUiRepository = ConsoleUiRepositoryImpl()
    ConsoleUiServiceImpl(consoleUiRepository)


def registerProtocol():
    customProtocolService = CustomProtocolServiceImpl.getInstance()
    accountFormRepository = AccountFormRepositoryImpl.getInstance()
    productFormRepository = ProductFormRepositoryImpl.getInstance()
    orderFormRepository = OrderFormRepositoryImpl.get_instance()

    customProtocolService.registerCustomProtocol(
        CustomProtocol.ORDER_DELETE.value,
        orderFormRepository.createOrderDeleteForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.ORDER_PURCHASE.value,
        orderFormRepository.createOrderPurchaseForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.ORDER_LIST.value,
        orderFormRepository.createOrderListForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.PROGRAM_CLOSE.value,
        accountFormRepository.createProgramCloseForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_INFO.value,
        productFormRepository.createProductInfoForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_ADD.value,
        productFormRepository.createProductAddForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_DELETE.value,
        productFormRepository.createProductDeleteForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_EDIT.value,
        productFormRepository.createProductEditForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_LIST.value,
        productFormRepository.createProductListForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_REGISTER.value,
        accountFormRepository.createAccountRegisterForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_LOGIN.value,
        accountFormRepository.AccountLoginForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_LOGOUT.value,
        accountFormRepository.AccountLogoutForm,
    )

    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_DELETE.value,
        accountFormRepository.AccountDeleteForm,
    )



def initEachDomain():
    initServerSocketDomain()
    initTaskManageDomain()
    initConsolePrinterDomain()
    registerProtocol()




if __name__ == '__main__':
    initEachDomain()

    clientSocketService = ClientSocketServiceImpl.getInstance()

    clientSocketService.createClientSocket(config('TARGET_HOST'), int(config('PORT')))
    clientSocketService.connectToTargetHost()

    taskManageService = TaskManageServiceImpl.getInstance()

    lock = multiprocessing.Lock()
    transmitQueue = multiprocessing.Queue()
    receiveQueue = multiprocessing.Queue()

    taskManageService.createTransmitTask(lock, transmitQueue)
    taskManageService.createReceiveTask(lock, receiveQueue)
    taskManageService.createPrinterTask(transmitQueue, receiveQueue)



    while True:
        try:
            sleep(5.0)

        except socket.error:
            sleep(0.5)


    TaskManageRepositoryImpl.getInstance().endTask()
    sys.exit(0)

