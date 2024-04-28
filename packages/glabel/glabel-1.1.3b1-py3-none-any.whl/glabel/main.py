# Step 2: Create the FastAPI app with undo functionality in `main.py`

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
import os
import random
import shutil
from typing import List, Dict, Optional

app = FastAPI()

# Global variables to track the image folder, classes, and last classification
image_folder = ""
image_classes = []
last_classified = None  # To keep track of the last classification for undoing

@app.get("/", response_class=HTMLResponse)
async def home():
    """Homepage with a single form to set the image folder and classes."""
    html_content = """
    <h1>Image Classification App</h1>
    <form action="/set-folder-and-classes/" method="post">
      <label for="folder">Set Image Folder:</label>
      <input type="text" id="folder" name="folder" placeholder="Enter folder path">
      <label for="classes">Enter Classes (comma-separated):</label>
      <input type="text" id="classes" name="classes" placeholder="e.g. cat, dog, bird">
      <button type="submit">Submit</button>
    </form>
    """
    return html_content


@app.post("/set-folder-and-classes/", response_class=HTMLResponse)
async def set_folder_and_classes(
    folder: str = Form(...),
    classes: str = Form(...)
):
    """Endpoint to set the image folder and classes in a single form submission."""
    global image_folder
    global image_classes
    
    # Sanitize the folder path (remove leading/trailing double quotes)
    folder = folder.strip('"')
    
    # Validate and set the image folder
    if not os.path.isdir(folder):
        return HTMLResponse(f"<p>Error: {folder} is not a valid directory.</p>")
    
    image_folder = folder
    
    # Set the classes from a comma-separated string
    image_classes = [cls.strip() for cls in classes.split(",") if cls.strip()]
    
    if not image_classes:
        return HTMLResponse(f"<p>No valid classes were entered.</p>")
    
    # Return a confirmation with a link to start classification
    return HTMLResponse(f"<p>Folder set to '{folder}'. Classes set: {', '.join(image_classes)}. <a href='/classify/'>Go to Classify</a></p>")


@app.get("/classify/", response_class=HTMLResponse)
async def classify_image():
    """Display the next image for classification with class buttons and undo option."""
    global last_classified

    if not image_folder or not os.path.isdir(image_folder):
        return HTMLResponse("<p>Error: Image folder not set or invalid.</p>")

    # List all images in the folder
    images = [f for f in os.listdir(image_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    
    if not images:
        return HTMLResponse("<p>No images found in the folder.</p>")

    # Randomly select an image
    image_name = random.choice(images)
    image_path = os.path.join(image_folder, image_name)

    # Container styles to maintain consistent button location
    html_content = f"""
    <style>
    .image-container {{
        width: 500px;
        height: 500px;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        /* Flex property that ensures content is centered in all directions */
    }}

    .classification-buttons {{
        text-align: center;
        margin-top: 20px;
    }}

    img {{
        /* Ensures the image doesn't distort the layout */
        max-width: 100%;
        max-height: 100%;
        object-fit: contain; /* This ensures that the image retains its aspect ratio */
    }}
    </style>

    <h2>Classify the Image</h2>
    <div class="image-container">
        <img src="/image/{image_name}" alt="Image for classification" />
    </div>
    <form action="/move-image/" method="post" class="classification-buttons">
        <input type="hidden" name="image_name" value="{image_name}"/>
    """
    
    # Generate buttons for each class
    for cls in image_classes:
        html_content += f"<button type='submit' name='class_name' value='{cls}'>{cls}</button> "

    # Add undo button if the last_classified has a valid image and class
    if last_classified:
        html_content += f"<button type='submit' formaction='/undo-classification/'>Undo Last Classification</button> "

    html_content += """
    </form>
    """
    
    return HTMLResponse(html_content)


@app.post("/move-image/", response_class=HTMLResponse)
async def move_image(image_name: str = Form(...), class_name: str = Form(...)):
    """Move the image to the specified class folder, then display the next image."""
    global last_classified
    if not image_folder or not os.path.isdir(image_folder):
        return HTMLResponse("<p>Error: Image folder not set or invalid.</p>")

    # Ensure the class folder exists
    class_folder = os.path.join(image_folder, class_name)
    if not os.path.isdir(class_folder):
        os.makedirs(class_folder)

    # Move the image to the class folder
    src_path = os.path.join(image_folder, image_name)
    dest_path = os.path.join(class_folder, image_name)
    shutil.move(src_path, dest_path)

    # Record the last classification for undoing
    last_classified = {"image_name": image_name, "class_name": class_name}

    # Load the next image for classification
    return await classify_image()


@app.post("/undo-classification/", response_class=HTMLResponse)
async def undo_classification():
    """Undo the last image classification and return to the previous state."""
    global last_classified
    if not last_classified:
        return HTMLResponse("<p>No previous classification to undo.</p>")

    image_name = last_classified["image_name"]
    class_name = last_classified["class_name"]

    # Move the image back to the original folder
    class_folder = os.path.join(image_folder, class_name)
    src_path = os.path.join(class_folder, image_name)
    dest_path = os.path.join(image_folder, image_name)

    shutil.move(src_path, dest_path)

    # Clear the last classified record after undoing
    last_classified = None

    return await classify_image()


@app.get("/image/{image_name}", response_class=FileResponse)
async def serve_image(image_name: str):
    """Endpoint to serve image files for display."""
    image_path = os.path.join(image_folder, image_name)
    if not os.path.isfile(image_path):
        return HTMLResponse("<p>Image not found.</p>")
    return FileResponse(image_path, media_type="image/jpeg")
