def get_binary(x):
    return f'{x:b}'


x = 10
bin_x = get_binary(x)
print(bin_x)  # print binary of the x
print(get_binary(x >> 2))
