def check(tab, n):
    bad_points_i = 0
    bad_points = [0]*(n**2)
    bad_x = set()
    bad_y = set()
    for y in range(n):
        for x in range(n):
            if bin(tab[y][x]).count("1") % 2 == 0:
                bad_points[bad_points_i] = (y, x)
                bad_points_i += 1
                bad_x.add(x)
                bad_y.add(y)
    
    for removed_x1 in bad_x:
        for removed_x2 in bad_x:
            for removed_y in bad_y:
                # print(bad_points)
                for point_y, point_x in bad_points[:bad_points_i]:
                    if (removed_x1 != point_x and removed_y != point_y) and (removed_x2 != point_x and removed_y != point_y):
                        break
                else:
                    return True

    return False


t = [
    [1,1,1,1,1,1],
    [1,1,1,3,1,3],
    [1,1,1,3,3,3],
    [1,3,1,1,1,1],
    [1,1,1,3,1,1],
    [1,1,1,1,1,1]
]

print(check(t, 6))