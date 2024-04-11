print("length of vectors:")
len_vectors = input()
print("num of vectors (not counting v):")
num_u_vectors = input()

v = [int(v) for v in input("enter v like \"a,b,c\":").split(",")]
print(v)

u_list = []
for i in range(0, int(num_u_vectors)):
    u_list.append([int(u) for u in input("enter u" + str(i + 1) + " like \"a,b,c\":").split(",")])

print(u_list)

# proj = (v dot u / u dot u) * each value in u + (...)
#      = v1*u1 + v2*u2 ... / u1*u2...

# build each vector:
def dot_product(v1, v2):
    print("dot " + str(v1))
    print(" and " + str(v2))
    sum = 0
    for i in range(0, len(v1)):
        sum += v1[i] * v2[i]
    print("sum: " + str(sum))
    return sum

def build_vector(v, u):
    numerator = dot_product(v, u)
    denom = dot_product(u, u)
    temp = []
    for num in u:
        temp.append(numerator/denom * num)
    print("vector = " + str(temp))
    print()
    return temp

lists = []
for u_vector in u_list:
    lists.append(build_vector(v, u_vector))
print("summing " + str(lists))

def add_lists(lists_of_lists):
    # Use zip to iterate through lists element-wise
    result = [sum(values) for values in zip(*lists_of_lists)]
    return result

result_list = add_lists(lists)
print("result vector: " + str(result_list))

