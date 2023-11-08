from Embedded.RelayContainer import RelayContainer

relay_container = RelayContainer()

print(relay_container.getSize())

relay_container.addRelay(1, True, "thign1", "foo")
relay_container.addRelay(3, False, "thing2", "fuh")
    
print(relay_container.getSize())
