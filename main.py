import cv2
import threading
import colorsys


# creating point object for the start and end


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


rect_half_width = 2
no_of_points = 0  # how many points have been registered
start_point = Point()
end_point = Point()

# defining up, down, left and right directions
arr_points = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]


def breadth_first_search(start, end):
    global img_file, height, width
    const = 10000

    found = False
    q = []
    visited_array = [[0 for j in range(width)] for i in range(height)]  # 0 indicating not visited 1 for visited
    parent = [[Point() for j in range(width)] for i in range(height)]

    q.append(start)
    visited_array[start.y][start.x] = 1

    while len(q) > 0:
        p = q.pop(0)

        for d in arr_points:
            cell = p + d
            if (0 <= cell.x < width and 0 <= cell.y < height) and visited_array[cell.y][cell.x] == 0 and (img_file[cell.y][cell.x][0] != 0 or img_file[cell.y][cell.x][1] != 0 or img_file[cell.y][cell.x][2] != 0):
                q.append(cell)
                visited_array[cell.y][cell.x] = visited_array[p.y][p.x] + 1

                img_file[cell.y][cell.x] = list(reversed([i*255 for i in colorsys.hsv_to_rgb(visited_array[cell.y][cell.x] / const, 1, 1)]))

                parent[cell.y][cell.x] = p

                if cell == end:
                    found = True
                    del q[:]
                    break

    path = []
    if found:
        p = end
        while p != start:
            path.append(p)
            p = parent[p.y][p.x]
        path.append(p)

        path.reverse()

        for p in path:
            img_file[p.y][p.x] = [255, 255, 255]
        print("Path is Found!!")
    else:
        print("Path not Found!!")


def mouse_event(event, pointX, pointY, flags, params):
    global img_file, start_point, end_point, no_of_points
    # to check if we have left click
    if event == cv2.EVENT_LBUTTONUP:
        if no_of_points == 0:
            cv2.rectangle(img_file, (pointX - rect_half_width, pointY - rect_half_width),
                          (pointX + rect_half_width, pointY + rect_half_width),
                          (255, 0, 0), -1)
            start_point = Point(pointX, pointY)
            print("Start = ", start_point.x, start_point.y)
            no_of_points += 1

        elif no_of_points == 1:
            cv2.rectangle(img_file, (pointX - rect_half_width, pointY - rect_half_width),
                          (pointX + rect_half_width, pointY + rect_half_width),
                          (0, 255, 0), -1)
            end_point = Point(pointX, pointY)
            print("End = ", end_point.x, end_point.y)
            no_of_points += 1


def disp():
    global img_file
    cv2.imshow("Image One", img_file)
    cv2.setMouseCallback("Image One", mouse_event)
    while True:
        cv2.imshow("Image One", img_file)
        cv2.waitKey(1)


# loading the image
img_file = cv2.imread("images/maze_one.png", cv2.IMREAD_GRAYSCALE)

# converting gray scale into just black and white
some_obj, img_file = cv2.threshold(img_file, 120, 255, cv2.THRESH_BINARY)

# back to color image
img_file = cv2.cvtColor(img_file, cv2.COLOR_GRAY2BGR)

height, width = img_file.shape[:2]  # only use the height and width value

print("Select the starting and ending points: ")

threading_ = threading.Thread(target=disp, args=())
threading_.daemon = True
threading_.start()

while no_of_points < 2:
    pass

# Doing the BreathFirst Search Algorithm to fill the maze
breadth_first_search(start_point, end_point)


cv2.waitKey(0)
