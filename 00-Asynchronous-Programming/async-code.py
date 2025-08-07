import asyncio
import time

async def brew_coffee():
    print("Brewing Coffee")
    await asyncio.sleep(3)  # assume 3 min
    print("Coffee is Ready.")

async def tost_bagel():
    print("Toasting Bagel")
    await asyncio.sleep(2)  # assume 2 min to take prepare the tost
    print("Bagel Ready.")   

async def main():
    
    start = time.time()
    
    coffee = brew_coffee()
    bagel = tost_bagel()
    
    result = await asyncio.gather(coffee, bagel)
    
    end = time.time()
    print(f"Time: {end - start:.2f} Minutes")
    
    

if __name__ == ("__main__"):
    asyncio.run(main())