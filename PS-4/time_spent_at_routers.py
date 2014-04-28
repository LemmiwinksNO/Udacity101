

distance = 5000  # km
speed = 200000  # km/s
total_time = .075  # in seconds, total round trip time

# how long round trip should take without delays
travel_time = float(distance)/speed

router_time = total_time - travel_time

print travel_time
print router_time