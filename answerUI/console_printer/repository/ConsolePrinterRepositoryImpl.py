import json
import socket
import sys
from datetime import datetime
from time import sleep

from console_printer.repository.ConsolePrinterRepository import ConsolePrinterRepository
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl
from sample import Sample


class ConsolePrinterRepositoryImpl(ConsolePrinterRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("TransmitterRepositoryImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


    def printConsoleUi(self, transmitQueue, receiveQueue):

        consoleUiService = ConsoleUiServiceImpl.getInstance()
        consoleUiService.printMenu()
        consoleUiService.processUserInput(transmitQueue)

        while True:
            if not receiveQueue.empty():
                try:
                    response = receiveQueue.get()
                    print(f"Received response: {response}")
                    print(f"type: {type(response)}")
                    evalresponse = json.loads(response)

                    print(f"evalresponse: {evalresponse}")
                    print(f"type: {type(evalresponse)}")

                    consoleUiService.printMenu()
                    consoleUiService.processUserInput(transmitQueue)
                except json.JSONDecodeError as e:
                    print(f"JSON 디코딩 오류: {e}")
                except Exception as e:
                    print(f"오류 발생: {e}")

            else:
                sleep(0.5)



