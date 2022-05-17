numbers = [4, 8, 15, 16, 23, 42]

with open("numbers.txt", mode="wt") as f:
    for number in numbers:
        f.write(str(number))

"""
     | 4   |  8   | 15  ...
"""
with open("numbers.data", mode="wb") as f:
    for number in numbers:
        f.write(number.to_bytes(8, byteorder="big"))

with open("numbers.data", mode="rb") as f:
    f.seek(8*2) # offset
    print(int.from_bytes(f.read(8), byteorder="big"))
