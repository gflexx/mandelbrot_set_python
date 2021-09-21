from PIL import Image

# plotting points
x1 = -2.0
y1 = -1.5
x2 = 1.0
y2 = 1.5

# number of iterations
max_iter = 360

# image height
h_x  = 720
h_y = 720
img = Image.new("RGB", (h_x, h_y))

# plotting and iterations
print("Generating art...")
for y in range(h_y):
    # plot y
    zy = y * (y2 - y1) / (h_y - 1) + y1

    # plot x
    for x in range(h_x):
        zx = x * (x2 - x1) / (h_x - 1) + x1
        z = zx + zy * 1j
        c = z

        # combine inputs to plot image points
        for i in range(max_iter):
            if abs(z) > 2.0: break
            z = z * z + c
        img.putpixel(
            (x, y),
            (i % 4 * 64, i % 8 * 32, i % 16 * 16)
        )
print('Ploting Done! Saving image...')
# save plotted image
img.save("mandelbrot_image.png")
print('Image saved!')
