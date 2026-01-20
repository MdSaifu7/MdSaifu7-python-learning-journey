import asyncio



async def make_chai(name):
    print(f"Preparing {name} chai...")
    await asyncio.sleep(3)
    print(f"Finished {name} chai...")


async def main():
    await asyncio.gather(
        make_chai("Ginger"),
        make_chai("Lemon"),
        make_chai("Light")
    )

asyncio.run(main())
