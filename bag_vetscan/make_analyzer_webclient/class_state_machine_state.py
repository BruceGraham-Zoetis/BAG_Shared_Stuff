class state_machine_states:
    def __init__(self):
        self.__dict_by_index = {}
        self.__dict_by_name = {}
        self.__nState = 0

    def add_state(self, strName : str, nState : int):
        self.__dict_by_index[nState] = strName
        self.__dict_by_name[strName] = nState

    def set(self, state):
        if (str == type(state)):
            try:
                nState = self.__dict_by_name[state]
                self.__nState = nState
            except:
                raise Exception("set_state_by_name('%s') - invalid state (str)" % state)
        elif (int == type(state)):
            # validate
            strName = self.__dict_by_index[state]
            if (0 < len(strName)):
                self.__nState = state
            else:
                raise Exception("set_state_by_name(%d) - invalid state (int)" % state)
        else:
            raise Exception("set_state_by_name(state) - type(state) must be 'str' or 'int'")

    def get_name(self) -> str:
        strName = self.__dict_by_index[self.__nState]
        return strName

    def get_index(self) -> int:
        return self.__nState


if __name__ == '__main__':
    print("-------- Test class ----------")
    stateMa = state_machine_states()

    stateMa.add_state("Startup", 0)
    stateMa.add_state("WaitForHubRestart", 1)
    stateMa.add_state("state2", 2)
    stateMa.add_state("state3", 3)
    
    try:
        stateMa.set("Startupx")
        raise Exception("failed invalid state name")
    except:
        print("passed invalid state name")

    stateMa.set(0)
    stateMa.set("Startup")

    try:
        stateMa.set(99)
        raise Exception("failed invalid state index")
    except:
        print("passed invalid state index")

    while True:
        strState = stateMa.get_name()
        print("State: " + stateMa.get_name())

        if ("Startup" == strState):
            nState = stateMa.get_index()
            nState += 1
            strState = stateMa.set(nState)

        elif ("WaitForHubRestart" == strState):
            strState = stateMa.set("state2")

        elif ("state2" == strState):
            strState = stateMa.set("state3")

        elif ("state3" == strState):
            print("End")
            break

        else:
            print("Error - state")
            break


