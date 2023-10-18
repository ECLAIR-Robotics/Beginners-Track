from embedded.Relay import Relay
import RelayContainer

if (__name__ == "__main__"):
    r = Relay(17, True)
    # r.setState(True)
    print("#1: ", r.getRelayState())

    r.setState(False)
    print("#2:", r.getRelayState())

    rc = RelayContainer.RelayContainer()

    rc.addCreatedRelay(r)
    rc.addRelay(27, False)
    print("#3: ", rc.str())

    print("#4 ", rc.getRelayIndex(0).getID())
    print("#5 ", rc.getRelay(17).getID())
    print("#6 ", rc.getAllRelays())
