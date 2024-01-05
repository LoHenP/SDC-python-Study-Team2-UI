import psutil


class TaskEntity:
    def __init__(self, taskPid, target, args):
        self.__taskPid = taskPid
        self.__target = target
        self.__args = args

    def getTaskPid(self):
        return self.__taskPid

    def getTarget(self):
        return self.__target

    def getArgs(self):
        return self.__args

    def terminateTask(self):
        try:
            process = psutil.Process(self.__taskPid)
            process.terminate()
            print(f"프로세스 {self.__taskPid}가 종료되었습니다.")
        except psutil.NoSuchProcess:
            print(f"프로세스 {self.__taskPid}를 찾을 수 없습니다.")