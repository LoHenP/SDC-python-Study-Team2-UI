class Session:
    def __init__(self):
        self.__session_id = -1

    def set_session_id(self, session_id):
        self.__session_id = session_id

    def get_session_id(self):
        return self.__session_id