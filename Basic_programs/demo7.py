###
# program to find area of the circle
###

def area_circle(radius):
    area = 22/7 * pow(radius, 2)
    area_round = round(area, 2)
    print("Area of the circle:", area_round)


if __name__ == "__main__":
    print("Radius of a circle:")
    radius = int(input())
    area_circle(radius)