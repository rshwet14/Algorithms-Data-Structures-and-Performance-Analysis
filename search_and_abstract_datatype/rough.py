# class HashAlgo:
#     def __init__(self, size):
#         self.size = size
#         self.hash_table = self.create_buckets()
#
#     def __str__(self):
#         return "".join(str(item) for item in self.hash_table)
#
#     def create_buckets(self):
#         return [[] for _ in range(self.size)]
#
#     def set_val(self, keys, values):
#
#         # hash_key = hash(keys)%self.size
#         hash_key = 4
#         bucket = self.hash_table[hash_key]
#         bucket.append((keys, values))
#
#
# hashtable = HashAlgo(10)
#
# hashtable.set_val("rshwet14@gmail.com", "King")
# hashtable.set_val("rajshwet07@gmail.com", "Savage")
# print(hashtable)

records = [('rshwet14@gmail.com', 'hello shwet'),
           ('rajshwet07@gmail.com', 'hello raj'),
           ('shwetk7@gamil.com', 'hello shwetu')
          ]

for index, record in enumerate(records):
    key, value = record
    # print(index,key,value)
    if key == 'rshwet14@gmail.com':
        break
key, value = ('rshwet14@gmail.com', 'hello abc')
records[index] = (key, value)
print(records)
