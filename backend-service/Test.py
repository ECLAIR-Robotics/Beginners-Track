from embedded.Relay import Relay
import RelayContainer

if (__name__ == "__main__"):
    rc = RelayContainer.RelayContainer()
    print(rc.str())
'''
    print(rc.getAllRelays())

    r = Relay(17, False)
    r.setState(True)
    print("#1: ", r.getRelayState())  # should be true

    r.setState(False)
    print("#2:", r.getRelayState())  # should be false

    rc = RelayContainer.RelayContainer()
    rc.add(r)
    print("#3: ", rc.str())

    rc.addRelay(27, False)
    print("#4: ", rc.str())

    print("#5 ", rc.getRelayIndex(0).getID())
    print("#6 ", rc.getRelay(17).getID())
    print("#7 ", rc.getAllRelays())

    rc.popRelay(0)
    print("#8: ", rc.str())

    rc.popRelay(1)
    print("#9: ", rc.str())
'''
