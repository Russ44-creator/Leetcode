from collections import defaultdict

class NearestCities:
    def binary_search(self, p_id, l, axis=1):  # axis 0 for x and 1 for y
        left, right = 0, len(l) - 1

        while left <= right:
            mid = left + (right-left)//2
            p_m = l[mid]
            if l[mid] == p_id:
                return mid
            elif self.points[p_m][axis] > self.points[p_id][axis]:
                right = mid - 1
            else:
                left = mid + 1

    def is_closest_point(self, p_id, k, l, closest_point, axis=1):
        if 0 <= k < len(l):
            p1 = l[k]
            print(p_id, p1)
            if abs(self.points[p1][axis] - self.points[p_id][axis]) < closest_point[1]:
                closest_point = [p1, abs(self.points[p1][axis] - self.points[p_id][axis]) ]

        return closest_point

    def set_close_point(self, p_id, i, j, x_points, y_points, result ):
            closest_point = [ None,  float('inf') ]
            # x left and right
            closest_point = self.is_closest_point(
                p_id, i-1, x_points,closest_point, axis=1)
            closest_point = self.is_closest_point(
                p_id, i+1, x_points,closest_point, axis=1)

            # y top and left
            closest_point = self.is_closest_point(
                p_id, j-1, y_points, closest_point, axis=0)
            closest_point = self.is_closest_point(
                p_id, j+1, y_points, closest_point, axis=0)

            print(p_id, closest_point)
            result.append(closest_point[0])

    def nearest_cities(self, pins, x_coordinates, y_coordinates, target_pins):
        self.points = defaultdict()
        x_pins = defaultdict(list)
        y_pins = defaultdict(list)

        result = []

        for p_id, x, y in zip(pins, x_coordinates, y_coordinates):
            self.points[p_id] = (x, y) # x和y的坐标
            x_pins[x].append(p_id) # 坐标为x的点的代号
            y_pins[y].append(p_id)

        for _, items in x_pins.items():
            items.sort(key=lambda p: self.points[p][1])
            # 按照y坐标排序

        for _, items in y_pins.items():
            items.sort(key=lambda p: self.points[p][0])

        # print(x_pins, y_pins, points)

        for p_id in target_pins:
            x, y = self.points[p_id]
            x_points = x_pins[x]
            y_points = y_pins[y]
        
            i = self.binary_search(p_id, x_points, axis=1) 
            j = self.binary_search(p_id, y_points, axis=0) 
            #print(i, j, p_id, x_points, y_points)

            self.set_close_point( p_id, i, j, x_points, y_points, result)

        return result


pins = ["a", "b", "c", "d", "e"]
x_coordinates = [50, 60, 100, 200, 300]
y_coordinates = [50, 60, 50, 200, 50]
target_pins = ["a", "b", "c", "d", "e"]
Output = ["c", "NONE", "a", "NONE", "c"]
print(NearestCities().nearest_cities(pins, x_coordinates, y_coordinates, target_pins))