#chaosgame :: creates a sirpinsky triangle


from PIL import Image, ImageDraw
import random

#get the length of the base
pixels = int(input("Gib Grundfläche des Dreiecks in Pixeln an: "))

#calculate the height
hoehe = int(round(((3 ** (1 / 2) * pixels / 2))))

#find the median approximately
median = int(round(pixels / 2))

#crte image width, haight
image = Image.new("RGB", (pixels, hoehe), "brown")
draw = ImageDraw.Draw(image)

#assign the points to tuple coordinates
A = (0, hoehe - 1)
B = (pixels - 1, hoehe - 1)
C = (median, 0)

xy = (0,hoehe - 1)

for i in range(0, 20000):
    # Determine the direction the dot is plotting to A, B, or C
    punkt = random.randint(0, 2)
    if punkt == 0:
        xtemp = int(round((xy[0] + A[0]) / 2))
        ytemp = int(round((xy[1] + A[1]) / 2))
        xy = (xtemp, ytemp)
        draw.point((xy), fill="black")
    elif punkt == 1:
        xtemp = int(round((xy[0] + B[0]) / 2))
        ytemp = int(round((xy[1] + B[1]) / 2))
        xy = (xtemp, ytemp)
        draw.point((xy), fill="black")
    else:
        xtemp = int(round((xy[0] + C[0]) / 2))
        ytemp = int(round((xy[1] + C[1]) / 2))
        xy = (xtemp, ytemp)
        draw.point((xy), fill="black")

#save image with original coordinates
image.save("triangle.png")
