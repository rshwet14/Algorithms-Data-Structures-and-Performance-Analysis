# Hash Operation :
# 1. Insert -set_val
# 2. Update -set_val
# 3. Find/retrive - get_val
# 4. Delete -Delete one item, pop(return Delete value)

import time
class AlgoHashTable:

    def __init__(self,size):
        self.size = size
        self.hastable = self.create_buckets()


    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def __str__(self):
        return "".join(str(item) for item in self.hastable)

    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        #collision condition
        # hashed_key = 10
        bucket = self.hastable[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key)%self.size
        #collision condition
        # hashed_key = 10
        bucket = self.hastable[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found related to this email address"

    def delete_record(self, key):
            hashed_key = hash(key)%self.size
            bucket = self.hastable[hashed_key]
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_value = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                print(bucket.pop(index))
            else:
                print("no related record to remove")
start = time.time()
hash_table = AlgoHashTable(10000)
# print(hash_table)
hash_table.set_val('rshwet14@gmail.com', {"first_name":"Shwet", "Last_name":"Roy"})
hash_table.set_val('rahul07@gmail.com', {"first_name":"Rahul", "Last_name":"Roy"})
hash_table.set_val('shwetuk7@gmail.com', {"first_name":"Shwetu", "Last_name":"Roy"})
hash_table.set_val('abc12@gmail.com', {"first_name":"abc", "Last_name":"Roy"})
hash_table.delete_record("abc12@gmail.com")
print(hash_table)
stop = time.time()
print(stop - start)
# print(hash_table.get_val("rshwet14@gmail.com"))
# hash_table.delete_record('rshwet14@gmail.com')
# print()
# print()
# print(hash_table)
