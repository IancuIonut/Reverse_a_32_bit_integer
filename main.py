def reverse(x: int) -> int:
    # Check if x is negative
    sign = -1 if x < 0 else 1

    # Convert x to a string, reverse it, and convert it back to an integer
    reversed_x = int(str(abs(x))[::-1])

    # Check if the reversed integer is within the 32-bit integer range
    if reversed_x > 2**31 - 1:
        return 0, False

    return reversed_x * sign, True

# enter number here. after x=
x = int(input())
result, is_within_range = reverse(x)

if is_within_range:
    print("Reversed integer:", result)
else:
    print("Out_of_32_bit_range ->", result)