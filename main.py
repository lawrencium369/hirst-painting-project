# import colorgram


# colors_in_image = colorgram.extract("image.jpg", 30)
# color_rgb = []

# for color in colors_in_image:
#     current_color = color.rgb
#     r = current_color.r
#     g = current_color.g
#     b = current_color.b 
#     color_rgb.append((r, g, b))
import turtle as t
import random

t.colormode(255)
t.speed("fastest")
fred = t.Turtle()
fred.penup()
fred.hideturtle()

color = [(236, 232, 223), (229, 233, 239), (239, 230, 235), (227, 235, 230), (194, 164, 111), (68, 90, 123), (142, 168, 186), (132, 93, 54), (215, 205, 133), (142, 66, 87), (30, 38, 64), (185, 142, 158), (122, 32, 55), (76, 14, 33), (138, 180, 150), (161, 152, 58), (44, 55, 98), (174, 97, 111), (53, 33, 22), (67, 117, 102), 
(219, 176, 189), (102, 118, 161), (178, 186, 212), (93, 151, 116), (180, 104, 88), (172, 204, 173), (165, 201, 212), (89, 144, 153), (82, 71, 35), (223, 177, 168)]
fred.right(135)
fred.fd(300)
fred.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    chosen_color = random.choice(color)
    fred.dot(20, chosen_color)
    fred.forward(50)

    if dot_count % 10 == 0:
        fred.left(90)
        fred.fd(50)
        fred.left(90)
        fred.fd(500)
        fred.setheading(0)


    






screen = t.Screen()
screen.exitonclick()