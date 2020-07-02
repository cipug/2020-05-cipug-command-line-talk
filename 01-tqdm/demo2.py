import time
from tqdm import tqdm

# iterate through a large number of items
for i in tqdm(range(50)):

    # do some complicated processing on item
    time.sleep(0.1)
