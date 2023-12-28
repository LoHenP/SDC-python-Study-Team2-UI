import ast
import json
import multiprocessing
import socket
import unittest
from time import sleep
from unittest.mock import patch, Mock

from console_ui.entity.Session import Session
from utility.keyboard.KeyboardInput import KeyboardInput


class TestUlgyCode(unittest.TestCase):
    def testRequestFormatter(self):
        sendProtocol = 1
        request = '(b\'btest\\n\', b\'btest\\n\')'
        print(f"request: {request}")

        requestTuple = ast.literal_eval(request)
        if not isinstance(requestTuple, tuple) or len(requestTuple) != 2:
            raise ValueError("Invalid request format")

        sendingRequest = {
            'accountId': requestTuple[0].decode().strip(),
            'password': requestTuple[1].decode().strip()
        }

        combinedRequestData = {
            'protocol': sendProtocol,
            'data': sendingRequest,
        }

        combinedRequestDataString = json.dumps(combinedRequestData)
        print(f"Combined Request Data String: {combinedRequestDataString}")

        self.assertIn('"protocol":', combinedRequestDataString)
        self.assertIn('"data":', combinedRequestDataString)

    def testEvalClassGeneration(self):
        class TestAccountRegisterResponse:
            def __init__(self, __isSuccess):
                self.__isSuccess = __isSuccess

            def getIsSuccess(self):
                return self.__isSuccess

        data = "TestAccountRegisterResponse(_TestAccountRegisterResponse__isSuccess=True)"
        responseBbject = eval(data)

        isSuccessValue = responseBbject.getIsSuccess()

        print(f'Extracted __isSuccess value: {isSuccessValue}')

    def testprocessUserInput(self):
        receiveQueue = multiprocessing.Queue()
        #receiveQueue.put({'username': 'test', 'password': '<PASSWORD>', 'list': ['1', '2', '3', '4', '5']})

        receiveQueue.put({'username': 'test', 'password': '<sad>', 'list': ['1', '2',  '4', '5']})
        print('put')
        sleep(0.5)

        if receiveQueue.empty():
            print('1empty')
        sleep(0.5)

        if not receiveQueue.empty():
            print('1not empty')
        sleep(0.5)

        print(receiveQueue.get())
        print('get')
        sleep(0.5)

        if receiveQueue.empty():
            print('2empty')
        sleep(0.5)

        if not receiveQueue.empty():
            print('2not empty')
        sleep(0.5)

        receiveQueue.put({'username': 'test', 'password': '<sad>', 'list': ['1', '2', '4', '5']})
        print('put')
        sleep(0.5)

        if receiveQueue.empty():
            print('3empty')
        sleep(0.5)

        if not receiveQueue.empty():
            print('3not empty')
        sleep(0.5)

if __name__ == '__main__':
    unittest.main()
