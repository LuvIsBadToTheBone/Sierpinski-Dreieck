from PIL import Image, ImageDraw

eingabe = int(input("Give depth of Sierpisky Triangle: "))

image = Image.new("RGB", (eingabe, eingabe), "brown")
draw = ImageDraw.Draw(image)
for i in range(eingabe):
	for j in range(eingabe):
		draw.point((j|i,i), fill = "white")
image.save("triangle.png")
