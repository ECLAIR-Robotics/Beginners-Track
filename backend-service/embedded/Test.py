from embedded.RelayControl import RelayContainer
from embedded.RelayControl import Relay

if (__name__ == "__main__"):
    rc = RelayContainer()

    print(rc.getAllRelays())

    r = Relay(17, True)
    r.setState(False)
    print("#1: ", r.getRelayState())  # should be true

    r.setState(True)
    print("#2:", r.getRelayState())  # should be false

    rc = RelayContainer()
    rc.add(r)
    print("#3: ", rc.str())

    rc.addRelay(27, True)
    print("#4: ", rc.str())

    print("#5 ", rc.getRelayIndex(0).getID())
    print("#6 ", rc.getRelay(17).getID())
    print("#7 ", rc.getAllRelays())

    rc.popRelay(0)
    print("#8: ", rc.str())

    rc.popRelay(1)
    print("#9: ", rc.str())
