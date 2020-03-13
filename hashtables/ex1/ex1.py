#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    
    for i in range(len(weights)):
        # check if the len of weights is equal to or less than 1
        if len(weights) <= 1:
            return None
        
        else:
            # otherwise check if the limit minus the number is in the hashtable
            target = limit - weights[i]
            # if the target is in the hash table get the index
            if hash_table_retrieve(ht,target) is not None:
                hash_table_insert(ht,weights[i],i)
                return (i,hash_table_retrieve(ht,target))

            # if the target isnt in the table add the weights as keys and the index as values
            hash_table_insert(ht,weights[i],i)
   


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# weight = [4, 4]
# print(get_indices_of_item_weights(weight,2,8))