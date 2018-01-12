from PIL import Image, ImageDraw

print("1 - открыть исходное изображение\n"
      "2 - серый\n"
      "3 - блюр\n")
choice = int(input())

if choice == 1:
    lena = Image.open("lena.bmp") 
    lena.show()
elif choice == 2:
    lena_g = Image.open("lena.bmp")
    draw = ImageDraw.Draw(lena_g)
    width = lena_g.size[0]
    height = lena_g.size[1]
    pix = lena_g.load()
    print(lena_g.size[0], "px")
    print(lena_g.size[1], "px")

    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            S = (r + g + b) // 3
            draw.point((i, j), (S, S, S))
    lena_g.save("lena_grey.png", "PNG")
    lena_g.show()

elif choice == 3:
    lena_b = Image.open("lena.bmp")
    draw = ImageDraw.Draw(lena_b)
    width = lena_b.size[0]
    height = lena_b.size[1]
    pix = lena_b.load()
    print(lena_b.size[0], "px")
    print(lena_b.size[1], "px")
    rad = 4
    i = rad + 1

    while i < width - (rad + 1):
        i += 1
        j = rad + 1
        while j < height - (rad + 1):
            r = float((pix[i - rad, j - rad][0] * 0.5 + pix[i - rad, j][0] * 0.5 + pix[i - rad, j + rad][0] * 0.5
                       + pix[i, j - rad][0] * 0.5 + pix[i, j][0] * 1 + pix[i, j + rad][0] * 0.5
                       + pix[i + rad, j - rad][0] * 0.5 + pix[i + rad, j][0] * 0.5 + pix[i + rad, j + rad][0]) * 0.5) // 3
            g = float((pix[i - rad, j - rad][0] * 0.5 + pix[i - rad, j][0] * 0.5 + pix[i - rad, j + rad][0] * 0.5
                       + pix[i, j - rad][0] * 0.5 + pix[i, j][0] * 1 + pix[i, j + rad][0] * 0.5
                       + pix[i + rad, j - rad][0] * 0.5 + pix[i + rad, j][0] * 0.5 + pix[i + rad, j + rad][0]) * 0.5) // 3
            b = float((pix[i - rad, j - rad][0] * 0.5 + pix[i - rad, j][0] * 0.5 + pix[i - rad, j + rad][0] * 0.5
                       + pix[i, j - rad][0] * 0.5 + pix[i, j][0] * 1 + pix[i, j + rad][0] * 0.5
                       + pix[i + rad, j - rad][0] * 0.5 + pix[i + rad, j][0] * 0.5 + pix[i + rad, j + rad][0]) * 0.5) // 3
            draw.point((i, j), (int(r), int(g), int(b)))
            j += 1
    lena_b.save("lena_blur.png", "PNG")
    lena_b.show()