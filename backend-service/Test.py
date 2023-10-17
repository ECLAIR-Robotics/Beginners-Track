from embedded.Relay import Relay
import RelayContainer

if (__name__ == "__main__"):
    r = Relay(1, False)
    r.setState(True)
    print(r.getRelayState())

    r.setState(False)
    print(r.getRelayState())

    rc = RelayContainer()

    rc.addRelay(r)
    rc.addRelay(1, True)
    rc.str()

    print(rc.getRelayIndex(0).getID())
    print(rc.getRelay(1).getID())
    print(rc.getAllRelays())
