from PIL import Image
import os
import random


class Block:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"x={self.x}, y={self.y}"
    
    def __repr__(self):
        return f"(x={self.x}, y={self.y})"
    
def get_blocks_in_sphere(radius):
    # Create a large list of blocks
    all_blocks = []
    for x_range in range(radius_of_sphere*2):
        for y_range in range(radius_of_sphere*2):
            for z_range in range(radius_of_sphere*2):
                all_blocks.append(Block(x_range, y_range, z_range))

    outside_blocks = []
    inside_blocks = []    
    center_of_sphere = (radius_of_sphere, radius_of_sphere, radius_of_sphere)  # Position of the center of the sphere

    # Create a list of blocks inside the sphere/hemisphere

    for i, block in enumerate(all_blocks):
        if not hemisphere_only:
            if abs(block.x - center_of_sphere[0])**2 + abs(block.y - center_of_sphere[1])**2 + abs(block.z - center_of_sphere[2])**2 <= radius**2:
                inside_blocks.append(block)
            else:
                outside_blocks.append(block)
        else:
            if abs(block.x - center_of_sphere[0])**2 + abs(block.y - center_of_sphere[1])**2 + abs(block.z - center_of_sphere[2])**2 <= radius**2 and block.z >= center_of_sphere[2]:
                inside_blocks.append(block)
            else:
                outside_blocks.append(block)

    return outside_blocks, inside_blocks

def save_image(list_of_points, name):
    image = Image.new("RGB", (radius_of_sphere*2, radius_of_sphere*2), (0, 0, 0))
    for point in list_of_points:
        color = random.randint(85, 255)
        image.putpixel((point.x, point.y), (255, 255, 255))
    image.save(f"images/{name}.png")


# definitions
radius_of_sphere = 10
hemisphere_only = True

# Create lists of blocks
outside, inside = get_blocks_in_sphere(radius_of_sphere)

# print number of blocks in each list
print(f"Blocks inside:{len(inside)}, Blocks outside:{len(outside)}")

# Delete all old images in "images/" if they exist
for filename in os.listdir("images/"):
    file_path = os.path.join("images/", filename)

    if os.path.isfile(file_path):
        os.remove(file_path)

# Save each layer as an image
for layer in range(radius_of_sphere*2):
    current_layer_of_blocks = []
    for block in inside:
        if block.z == layer:
            current_layer_of_blocks.append(block)
    # only save an image if there is some blocks on that layer
    if len(current_layer_of_blocks) > 0:
        save_image(current_layer_of_blocks, f"layer{layer}")
