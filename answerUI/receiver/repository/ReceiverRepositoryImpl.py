import errno
from socket import socket
from time import sleep

from receiver.repository.ReceiverRepository import ReceiverRepository


class ReceiverRepositoryImpl(ReceiverRepository):
    __instance = None
    __lengthHeaderSize = 8

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("ReceiverRepositoryImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    # 클라이언트 소켓에 수신
    def receiveCommand(self, clientSocketObject, lock, receiveQueue, finishQueue):
        clientSocket = clientSocketObject.getSocket()
        print(f"receiver: is it exist -> {clientSocket}")
        getMoreData = True
        while True:
            combineData = ""

            try:
                while True:

                    # 소켓으로 전송된 데이터 수신
                    data = clientSocket.recv(2048)
                    if not data:
                        clientSocket.closeSocket()
                        break
                    combineData += data.decode()
                    print(f"수신데이터 : {data.decode()}")

                    if getMoreData:
                        data_length = int(data[:self.__lengthHeaderSize])
                        print(f"data_length: {data_length}")
                        print(f"combineData_length: {len(combineData)}")
                        getMoreData = False

                    if len(combineData) - self.__lengthHeaderSize == data_length:
                        print(combineData[self.__lengthHeaderSize:])
                        receiveData = eval(combineData[self.__lengthHeaderSize:])
                        receiveQueue.put(receiveData)
                        getMoreData = True
                        break


                    # print(f'수신된 정보: {data.decode()}')


                try:
                    if receiveData['__protocolNumber'] == 0:
                        break

                except :
                    pass


            except socket.error as exception:
                if exception.errno == errno.EWOULDBLOCK:
                    pass

            finally:
                sleep(0.5)

        finishQueue.put(True)


