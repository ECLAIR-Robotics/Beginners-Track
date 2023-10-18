from embedded.Relay import Relay
import RelayContainer

if (__name__ == "__main__"):
    r = Relay(17, False)
    r.setState(True)
    print("#1: ", r.getRelayState())

    r.setState(False)
    print("22:", r.getRelayState())

    rc = RelayContainer.RelayContainer()

    rc.addCreatedRelay(r)
    rc.addRelay(4, True)
    print("#2: ", rc.str())

    print("#3 ", rc.getRelayIndex(0).getID())
    print("4 ", rc.getRelay(17).getID())
    print("5 ", rc.getAllRelays())
