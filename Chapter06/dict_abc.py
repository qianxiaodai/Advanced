from collections.abc import Mapping
from _collections_abc import __all__
from collections import defaultdict
from random import randint


d = {"name": "Tom", "age": 17, "height": 176}

new_d = d.copy()
# print(new_d)
new_d["age"] = 18
pass
# print(new_d)

# print(d)

k_list = ["bobby", "Jam"]
d = dict.fromkeys(k_list, {"company: imooc"})
pass

nums = [1, 2, 3]
for i, ele in enumerate(nums):
    print(i, ele)
    nums.remove(ele)
    # print(id(ele))

print(nums)

print('\n')
nums = [1, 2, 3]
for i, ele in enumerate(nums[:]):
    print(i, ele)
    nums.remove(ele)
    # print(id(ele))
print(nums)


list

