
from lrucache.geo_lrucache import GeoLRUCache
from helper import TEST_DB_URL

import time

# Alberta's Latitude and Longitude = 54.1635492,-123.9813041
print("This is Alberta's Cache")

cache = GeoLRUCache((54.1635492,-123.9813041), db_url=TEST_DB_URL)


n = 0
while 1:

    all_keys = ["from_manitoba_cache", "from_quebec_cache", "from_nfl_cache", "from_bc_cache"]

    print()
    print('-'*50)
    for key in all_keys:
        val = cache.get(key)
        if val:
            print(f"Got item ({key}, {val})")

        # If the item does not exist, None is printed. None is also
        # printed if the item has expired in the cache        
        else:
            print("None")
    print('-'*50)      
    print()      

    # After 15 seconds, publish yours to every other cache in the environment
    if n == 15:
        print("I published ('from_alberta_cache', 'alberta_set') to every other cache in the environment")
        cache.set("from_alberta_cache", "alberta_set")

    # Stop the script after eighty seconds. The default expiry time of items in the cache
    # is sixty seconds. This is done to also test cache expiry.
    if n == 80:
        break  

    n += 1      
    time.sleep(1)
