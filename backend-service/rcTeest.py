from Embedded.RelayContainer import RelayContainer
import time

relay_container = RelayContainer()
relay_container
#print(relay_container.relay_container)

#print(relay_container.getSize())

#relay_container.addRelay(20, True, "thign1", "foo")

# #print(relay_container.getSize())

# relay_container.addRelay(6, False, "thing2", "fuh")
# relay_container.addRelay(16, True, "thing2", "fuh")

#relay_container.removeRelay(25)

# print(relay_container)
# print(relay_container.getRelayIndex(1))
# print(relay_container.getRelay(6))
# print(relay_container)

#print(relay_container.getSize())


# print(relay_container.getAllRelays())
# for relay in relay_container.getAllRelays():
#     print(relay)
#     print(relay.get_id())

# relay_container.getRelay(27)
# relay_container.remove(27)
# relay_container.getRelay(27)

for relay in relay_container.getAllRelays():
    relay_container.removeRelay(relay.get_id())

for i in range(27):
    print(i)
    relay_container.addRelay(i, 1, f"name{i}", f"disc{i}")
    time.sleep(2)

#print(relay_container.getSize())

# for i in range(27):
#     relay_container.setState(i, 1, f"name{i}", f"disc{i}")

#print(relay_container.getRelayIndex(0))
#print(relay_container.getRelay(6))
#print(relay_container.getRelay(16))
#print(relay_container.get(Relay(27)))
print(relay_container)



