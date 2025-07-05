


def binary_string_to_int(num_servers, num_players, num_admins):
    x = int(num_servers, 2)
    y = int(num_players, 2)
    z = int(num_admins, 2)
    return x, y, z

data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
print(data_a)
# 4
print(data_b)
# 5
print(data_c)
# 6
