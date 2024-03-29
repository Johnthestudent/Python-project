from typing import List


def foo(nums: List[int]) -> List[int]:
    # Code returns products of all list members, except i index element
    product_list = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                product *= nums[j]
        product_list.append(product)
    print(product_list)
    return product_list

if __name__ == "__main__":
    assert foo([1, 2, 3, 4, 5])