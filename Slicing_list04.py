def main(list1):
    """
    A list of several elements is given. Return the three elements from the beginning.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    a = list1[:3]
    return a
print(main([1,2,3,4,5]))