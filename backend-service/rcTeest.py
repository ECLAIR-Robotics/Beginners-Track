from Embedded.RelayContainer import RelayContainer

relay_container = RelayContainer()
relay_container
print(relay_container.getSize())

relay_container.addRelay(20, True, "thign1", "foo")
relay_container.addRelay(16, False, "thing2", "fuh")


print(relay_container.getAllRelays())
for relay in relay_container.getAllRelays():
    print(relay)
    print(relay.get_id())
