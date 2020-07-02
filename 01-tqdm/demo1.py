import time

# iterate through a large number of items
for i in range(50):

    # do some complicated processing on item
    time.sleep(0.1)

    # output a primitive progress marker
    print('.', end='', flush=True)
