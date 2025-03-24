def sum_nested_list(nested_list):
    total_sum = 0
    for item in nested_list:
        if isinstance(item, list):
            total_sum += sum_nested_list(item)
        else:
            total_sum += item
    return total_sum

nested_list5 = [1, 2, 3]
print(f"Sum of nested_list5: {sum_nested_list(nested_list5)}")