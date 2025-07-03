import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Initialize root
root = tk.Tk()
root.title("Symbolic Link Helper")

# --- Mode Selection ---
mode_var = tk.StringVar(value="folder")

tk.Label(root, text="Select Mode:").grid(row=0, column=0, sticky="e")
tk.Radiobutton(root, text="Folder", variable=mode_var, value="folder").grid(row=0, column=1, sticky="w")
tk.Radiobutton(root, text="File", variable=mode_var, value="file").grid(row=0, column=2, sticky="w")

# --- Entry and Buttons ---
def browse_source():
    path = filedialog.askopenfilename() if mode_var.get() == "file" else filedialog.askdirectory()
    if path:
        src_entry.delete(0, tk.END)
        src_entry.insert(0, path)

def browse_target():
    path = filedialog.askopenfilename() if mode_var.get() == "file" else filedialog.askdirectory()
    if path:
        dst_entry.delete(0, tk.END)
        dst_entry.insert(0, path)

def create_symlink():
    source = src_entry.get()
    target = dst_entry.get()
    try:
        os.symlink(source, target)
        messagebox.showinfo("Success", f"Symbolic link created:\n{target} → {source}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create symlink:\n{e}")

# --- Input Fields ---
tk.Label(root, text="Source Path:").grid(row=1, column=0, sticky="e")
src_entry = tk.Entry(root, width=50)
src_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_source).grid(row=1, column=2)

tk.Label(root, text="Link Path:").grid(row=2, column=0, sticky="e")
dst_entry = tk.Entry(root, width=50)
dst_entry.grid(row=2, column=1)
tk.Button(root, text="Browse", command=browse_target).grid(row=2, column=2)

# --- Final Action Button ---
tk.Button(root, text="Create Link", command=create_symlink, width=20).grid(row=3, column=1, pady=10)

root.mainloop()