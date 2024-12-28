import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os
import argparse
import subprocess

def run_detection(source, weights, img_size, conf_thres, iou_thres, device, view_img, save_txt, save_img, classes, agnostic_nms, augment):
    command = [
        "python", "detect_and_track.py",
        "--source", source,
        "--weights", weights,
        "--img-size", str(img_size),
        "--conf-thres", str(conf_thres),
        "--iou-thres", str(iou_thres),
        "--device", device,
    ]
    if view_img:
        command.append("--view-img")
    if save_txt:
        command.append("--save-txt")
    if save_img:
        command.append("--save-img")
    if classes:
        command.extend(["--classes"] + [str(c) for c in classes])
    if agnostic_nms:
        command.append("--agnostic-nms")
    if augment:
        command.append("--augment")

    subprocess.run(command)

def start_detection():
    source = source_entry.get()
    weights = weights_entry.get()
    img_size = int(img_size_entry.get())
    conf_thres = float(conf_thres_entry.get())
    iou_thres = float(iou_thres_entry.get())
    device = device_entry.get()
    view_img = view_img_var.get()
    save_txt = save_txt_var.get()
    save_img = save_img_var.get()
    classes = classes_entry.get().split(",") if classes_entry.get() else []
    agnostic_nms = agnostic_nms_var.get()
    augment = augment_var.get()

    detection_thread = threading.Thread(target=run_detection, args=(source, weights, img_size, conf_thres, iou_thres, device, view_img, save_txt, save_img, classes, agnostic_nms, augment))
    detection_thread.start()

def browse_source():
    file_path = filedialog.askopenfilename()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, file_path)

def browse_weights():
    file_path = filedialog.askopenfilename()
    weights_entry.delete(0, tk.END)
    weights_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("YOLOv7 Object Detection and Tracking")

# Create and place the widgets
tk.Label(root, text="Source:").grid(row=0, column=0, sticky=tk.W)
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_source).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Weights:").grid(row=1, column=0, sticky=tk.W)
weights_entry = tk.Entry(root, width=50)
weights_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_weights).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Image Size:").grid(row=2, column=0, sticky=tk.W)
img_size_entry = tk.Entry(root, width=10)
img_size_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
img_size_entry.insert(0, "640")

tk.Label(root, text="Confidence Threshold:").grid(row=3, column=0, sticky=tk.W)
conf_thres_entry = tk.Entry(root, width=10)
conf_thres_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
conf_thres_entry.insert(0, "0.25")

tk.Label(root, text="IOU Threshold:").grid(row=4, column=0, sticky=tk.W)
iou_thres_entry = tk.Entry(root, width=10)
iou_thres_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
iou_thres_entry.insert(0, "0.45")

tk.Label(root, text="Device:").grid(row=5, column=0, sticky=tk.W)
device_entry = tk.Entry(root, width=10)
device_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
device_entry.insert(0, "")

view_img_var = tk.BooleanVar()
tk.Checkbutton(root, text="View Image", variable=view_img_var).grid(row=6, column=0, sticky=tk.W)

save_txt_var = tk.BooleanVar()
tk.Checkbutton(root, text="Save TXT", variable=save_txt_var).grid(row=6, column=1, sticky=tk.W)

save_img_var = tk.BooleanVar()
tk.Checkbutton(root, text="Save Image", variable=save_img_var).grid(row=6, column=2, sticky=tk.W)

tk.Label(root, text="Classes (comma-separated):").grid(row=7, column=0, sticky=tk.W)
classes_entry = tk.Entry(root, width=50)
classes_entry.grid(row=7, column=1, padx=5, pady=5)

agnostic_nms_var = tk.BooleanVar()
tk.Checkbutton(root, text="Agnostic NMS", variable=agnostic_nms_var).grid(row=8, column=0, sticky=tk.W)

augment_var = tk.BooleanVar()
tk.Checkbutton(root, text="Augmented Inference", variable=augment_var).grid(row=8, column=1, sticky=tk.W)

tk.Button(root, text="Start Detection", command=start_detection).grid(row=9, column=0, columnspan=3, pady=10)

# Start the main loop
root.mainloop()