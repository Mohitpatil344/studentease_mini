from tkinter import *

def open_new_page(image_index):
    # Destroy the current window
    root.destroy()
    import lectno

    

    # Add a label to display the index of the clicked image
    label = Label(new_window, text="Clicked Image Index: " + str(image_index))
    label.pack()

    # Run the new window main loop
    new_window.mainloop()

def image_click(event):
    # Find the item that was clicked (returns tags as a tuple)
    item = event.widget.find_withtag(CURRENT)
    if item:
        tags = event.widget.gettags(item)
        if tags:
            # Extract the index from the tag
            index = int(tags[0].split("_")[1])
            open_new_page(index)

root = Tk()
root.geometry("935x588")
root.title("D10C")

canvas = Canvas(root, width=935, height=788)
canvas.pack()

# Define the width and height of each rectangle
rectangle_width = 201
rectangle_height = 200

# Define the gap between each rectangle
gap = 50

# Initial coordinates for the first rectangle in the top row
x1_top = 50
y1_top = 50

# Image paths for the top row
top_image_paths = [
    "CN IMG.png",
    "t2.png",
    "PYTN.png"
]

# Create a list to store PhotoImage objects for the top row
top_photo_images = []

# Create 3 rectangles in the top row and add images
for i, image_path in enumerate(top_image_paths):
    image = PhotoImage(file=image_path)
    top_photo_images.append(image)
    x2_top = x1_top + rectangle_width
    y2_top = y1_top + rectangle_height
    # Create a unique tag for each rectangle
    tag = "top_" + str(i)
    canvas.create_rectangle(x1_top, y1_top, x2_top, y2_top, fill="blue", tags=tag)
    canvas.create_image((x1_top + x2_top) // 2, (y1_top + y2_top) // 2, image=image)
    # Bind the click event to the rectangle
    canvas.tag_bind(tag, "<Button-1>", image_click)
    x1_top = x2_top + gap

# Increased vertical spacing for the bottom row
y1_bottom = y1_top + rectangle_height + gap

# Initial coordinates for the first rectangle in the bottom row
x1_bottom = 50

# Image paths for the bottom row
bottom_image_paths = [
    "t4.png",
    "t5.png",
    "t6.png"
]

# Create a list to store PhotoImage objects for the bottom row
bottom_photo_images = []

# Create 3 rectangles in the bottom row and add images
for i, image_path in enumerate(bottom_image_paths):
    image = PhotoImage(file=image_path)
    bottom_photo_images.append(image)
    x2_bottom = x1_bottom + rectangle_width
    y2_bottom = y1_bottom + rectangle_height
    # Create a unique tag for each rectangle
    tag = "bottom_" + str(i)
    canvas.create_rectangle(x1_bottom, y1_bottom, x2_bottom, y2_bottom, fill="yellow", tags=tag)
    canvas.create_image((x1_bottom + x2_bottom) // 2, (y1_bottom + y2_bottom) // 2, image=image)
    # Bind the click event to the rectangle
    canvas.tag_bind(tag, "<Button-1>", image_click)
    x1_bottom = x2_bottom + gap

root.mainloop()
