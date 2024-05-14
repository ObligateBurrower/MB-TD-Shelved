from PIL import Image, ImageDraw

# Create a new image with white background
size = 800  # Overall size of the image
grid_size = 40  # Number of cells in the grid
cell_size = size // grid_size
image = Image.new("RGB", (size, size), color="white")

# Create a draw object to draw on the image
draw = ImageDraw.Draw(image)

# Draw the grid
for i in range(grid_size + 1):
    # Draw vertical lines
    draw.line((i * cell_size, 0, i * cell_size, size), fill="black")
    # Draw horizontal lines
    draw.line((0, i * cell_size, size, i * cell_size), fill="black")

# Save the image
file_path = "../20x20_Grid.png"
image.save(file_path)
