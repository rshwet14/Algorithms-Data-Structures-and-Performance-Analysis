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
hash_table = AlgoHashTable(1000000)

with open("data.txt") as f:
    for line in f:
        key, value = line.split(":")
        value = value.strip("\n")
        hash_table.set_val(key, value)

print(hash_table)
