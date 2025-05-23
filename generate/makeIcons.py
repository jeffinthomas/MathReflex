from PIL import Image
import os
import zipfile

# Define the sizes and the output directory
icon_sizes = [72, 96, 128, 144, 152, 192, 384, 512]
output_dir = "icons_output"
os.makedirs(output_dir, exist_ok=True)

# Create a base image (e.g., a simple solid color square) to simulate the icons
# Replace this with your actual source image if you have one
base_image = Image.new("RGBA", (512, 512), color="#48bb78")  # green background

# Create resized icons
icon_paths = []
for size in icon_sizes:
    resized_image = base_image.resize((size, size), Image.LANCZOS)
    filename = f"icon-{size}x{size}.png"
    filepath = os.path.join(output_dir, filename)
    resized_image.save(filepath, format="PNG")
    icon_paths.append(filepath)

# Create a ZIP file with the icons
zip_filename = "math_blitz_icons.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file_path in icon_paths:
        zipf.write(file_path, os.path.basename(file_path))

print(f"ZIP file created: {zip_filename}")
