from GF2 import *def vec_dot_product(v,u):    t = 0;    for i in range(len(v)):        t = t + v[i]*u[i]    return tu1 = [one,one,0,0]u2 = [one,0,one,0]u3 = [one,one,one,one]all_set = ([x1,x2,x3,x4] for x1 in[one,0] for x2 in[one,0] for x3 in[one,0] for x4 in[one,0])for vec in all_set:    if one == vec_dot_product(vec,u1) and one == vec_dot_product(vec,u2) and one == vec_dot_product(vec,u3) and one == vec_dot_product(vec,[one,one,one,one]):        print(vec)        exit()