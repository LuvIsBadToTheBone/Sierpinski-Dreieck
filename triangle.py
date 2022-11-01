from PIL import Image, ImageDraw

komplexitaet = []
eingabe = int(input("Give depth of Sierpiskie Triangle: "))

for i in range(eingabe):
	komplexitaet.append(i+1)

def line(out):
	zeile = 1
	image = Image.new("RGB", (eingabe, eingabe), "brown")
	draw = ImageDraw.Draw(image)
	for i in range(eingabe):
		for j in komplexitaet:
			draw.point((j|i,zeile), fill = "white")
		zeile = zeile + 1
	image.save(out)

if __name__ == "__main__":
	line("triangle.png")
