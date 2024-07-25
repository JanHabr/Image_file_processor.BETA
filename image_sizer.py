import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def resize_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    img = Image.open(file_path)
    img_tk = ImageTk.PhotoImage(img)
    preview_label.config(image=img_tk)
    preview_label.image = img_tk

    def save_resized_image():
        width = int(width_entry.get())
        height = int(height_entry.get())
        resized_img = img.resize((width, height))
        
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*")])
        if save_path:
            resized_img.save(save_path)
            messagebox.showinfo("Success", "Image resized and saved successfully")

    resize_button.config(command=save_resized_image)

app = tk.Tk()
app.title("Image Resizer")

tk.Label(app, text="Width:").grid(row=1, column=0)
width_entry = tk.Entry(app)
width_entry.grid(row=1, column=1)

tk.Label(app, text="Height:").grid(row=2, column=0)
height_entry = tk.Entry(app)
height_entry.grid(row=2, column=1)

preview_label = tk.Label(app)
preview_label.grid(row=0, column=0, columnspan=2)

resize_button = tk.Button(app, text="Resize Image", command=resize_image)
resize_button.grid(row=3, column=0, columnspan=2)

app.mainloop()
