def max_of_free(a, b, c, d):
    return max(max(a, b, c), max(a, b, d), max(a, c, d))
print(max_of_free(11 , 25, 52, 67))