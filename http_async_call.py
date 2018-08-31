import asyncio  
import time  
from datetime import datetime
import requests
import random


async def custom_sleep(name):
    temp = random.randint(1,5)

    print('Task {} SLEEP {} secs {}\n'.format(name, temp, datetime.now()))
    await asyncio.sleep(temp)


async def httpCall(name):
	await custom_sleep(name)
	r = requests.get('https://webhook.site/33879aac-dfa3-43d8-acb0-ae23bf9e847a')
	print ('Task {} HTTP Call Date {}'.format(name, r.headers['Date']) )


start = time.time()  
loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(httpCall("A")),
    asyncio.ensure_future(httpCall("B")),
    asyncio.ensure_future(httpCall("C")),

]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()
end = time.time()  
print("Total time: {}".format(end - start))
