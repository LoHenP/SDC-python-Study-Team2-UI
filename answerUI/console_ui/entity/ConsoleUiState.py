from console_ui.entity.ConsoleUiRoutingState import ConsoleUiRoutingState


class ConsoleUiState():

    def __init__(self):
        self.__currentRoutingState = ConsoleUiRoutingState.NOTHING
        # self.__currentReadNumber = None

    def setCurrentRoutingState(self, currentState):
        print(f"input data: {currentState}")
        self.__currentRoutingState = ConsoleUiRoutingState(currentState)

    def getCurrentRoutingState(self):
        return self.__currentRoutingState

