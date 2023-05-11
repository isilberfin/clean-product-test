import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os

def capture_image():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    # Capture an image from the camera
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    return frame


def save_image(image, folder, filename):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Save the image to the specified folder and filename
    filepath = os.path.join(folder, filename)
    cv2.imwrite(filepath, image)


def take_picture():
    # Capture an image from the camera
    image = capture_image()

    # Save the image to a file in the "test_folder" directory
    folder = 'test-img'
    filename = 'test_img.png'
    save_image(image, folder, filename)

    # Close the camera
    cap.release()
    root.destroy()


# Create the main window
root = tk.Tk()

# Open the default camera
cap = cv2.VideoCapture(0)

# Create a label for displaying the camera feed
label = tk.Label(root)
label.pack()

# Create a "Take Picture" button
button = tk.Button(root, text="Take Picture", command=take_picture)
button.pack()

def update_frame():
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Create an ImageTk object from the frame
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    # Update the label with the new frame
    label.imgtk = imgtk
    label.configure(image=imgtk)

    # Schedule the next update
    label.after(10, update_frame)

# Start updating the frame
update_frame()

# Start the GUI event loop
root.mainloop()