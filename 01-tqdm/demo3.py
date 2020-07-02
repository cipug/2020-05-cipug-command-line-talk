import time
from tqdm import tqdm

# use a custom generator that doesn't expose the total length
def my_generator(n):
    for i in range(n):
        yield i

# iterate through a large number of items
for i in tqdm(my_generator(50)):

    # do some complicated processing on item
    time.sleep(0.1)
