import math

def closest_pair(points):
    # Preprocess
    points_xsorted = merge_sort(points, sort_by=0)
    points_ysorted = merge_sort(points, sort_by=1)

    return _closest_pair(points_xsorted, points_ysorted)

def _closest_pair(points_xsorted, points_ysorted):
    n1 = len(points_xsorted)
    n2 = len(points_ysorted)

    assert n1 == n2, 'n1 and n2 must be equal'
    n = n1

    if n==2 or n==3:
        return closest_pair_brute(points_xsorted)
    
    n_2 = int(n/2)
    lpoints_xsorted = points_xsorted[:n_2]
    lpoints_ysorted = points_ysorted[:n_2]
    rpoints_xsorted = points_xsorted[n_2:]
    rpoints_ysorted = points_ysorted[n_2:]
    
    (p1, q1), dl = _closest_pair(lpoints_xsorted, lpoints_ysorted)  # Closest pair left
    (p2, q2), dr = _closest_pair(rpoints_xsorted, rpoints_ysorted)  # Closest pair right
    d = min(dl, dr)
    x_bar = lpoints_xsorted[-1][0]
    split_pair = closest_split_pair(points_xsorted, points_ysorted, x_bar, d)
    if split_pair != None:
        return split_pair
    else:
        return (p1, q1) if dl < dr else (p2, q2)

def closest_split_pair(points_xsorted, points_ysorted, x_bar, d):
    x_min = x_bar - d
    x_max = x_bar + d
    s_y = []
    for point in points_ysorted:
        if x_min < point[0] < x_max:
            s_y.append(point)
    
    # Check if strip has points
    if s_y == []:
        return None
    
    s_len = len(s_y)
    if s_len > 7:
        en = 7
    else:
        en = s_len - 1

    best_pair = None
    for i in range(s_len-en):
        for j in range(en):
            p, q = s_y[i], s_y[i+j+1]
            _d = dist(p, q)
            if _d < d:
                best_pair = (p, q)
                d = _d
    
    return best_pair

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def merge_sort(points, sort_by=0):
    n = len(points)
    
    if n == 1:
        return points
    
    n_2 = int(n/2)
    lpoints = points[:n_2]
    rpoints = points[n_2:]
    
    lpoints_sorted = merge_sort(lpoints, sort_by)
    rpoints_sorted = merge_sort(rpoints, sort_by)
    
    nl = len(lpoints_sorted)
    nr = len(rpoints_sorted)
    
    points_sorted = []
    i = 0
    j = 0
    while i<nl and j<nr:
        if lpoints_sorted[i][sort_by] <= rpoints_sorted[j][sort_by]:
            points_sorted.append(lpoints_sorted[i])
            i += 1
        else:
            points_sorted.append(rpoints_sorted[j])
            j += 1
    
    while i < nl:
        points_sorted.append(lpoints_sorted[i])
        i += 1
    
    while j < nr:
        points_sorted.append(rpoints_sorted[j])
        j += 1
    
    return points_sorted

def closest_pair_brute(points):
    p1, p2 = points[0], points[1]
    d = dist(p1, p2)
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            _p1, _p2 = points[i], points[j]
            dn = dist(_p1, _p2)
            if dn < d:
                d = dn
                p1, p2 = _p1, _p2
    
    return (p1, p2), d

if __name__ == '__main__':
    points = [(0.5, 2), (2, 1), (2.5, 2.1), (2.6, 2.2), (4, 2), (2.2, 4)]
    print(closest_pair(points))

    # Check with brute force
    min_p = points[0], points[1]
    d = dist(min_p[0], min_p[1])
    for point in points:
        for point1 in points:
            if point != point1:
                _d = dist(point, point1)
                if _d < d:
                    min_p = point, point1
                    d = _d
    
    print(min_p)
