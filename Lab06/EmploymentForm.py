import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class EmploymentFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employment")
        self.root.configure(bg="#b0d9e4")  # Light blue background

        # Placeholder for image
        self.photo = ImageTk.PhotoImage(Image.new('RGB', (100, 100), 'gray'))
        self.img_label = tk.Label(root, image=self.photo, bg="#b0d9e4")
        self.img_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.browse_btn = tk.Button(root, text="Browse", command=self.browse_image)
        self.browse_btn.grid(row=0, column=2, padx=10, pady=10)

        # Form fields
        fields = ['Full Name:', 'ID:', 'Phone:', 'Salary:']
        self.entries = {}
        for i, field in enumerate(fields, start=1):
            tk.Label(root, text=field, bg="#b0d9e4").grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
            entry = tk.Entry(root)
            entry.grid(row=i, column=2, padx=5, pady=5)
            self.entries[field] = entry

        # Team radio buttons
        tk.Label(root, text="Team:", bg="#b0d9e4").grid(row=5, column=1, sticky=tk.E, padx=5, pady=5)
        self.team_var = tk.StringVar(value="Analysis")
        teams = ["Analysis", "Dev", "Testing"]
        for i, team in enumerate(teams):
            tk.Radiobutton(root, text=team, variable=self.team_var, value=team, bg="#b0d9e4").grid(row=5, column=2+i, padx=2, pady=5, sticky=tk.W)

        # File to be saved
        tk.Label(root, text="File to be saved:", bg="#b0d9e4").grid(row=6, column=1, sticky=tk.E, padx=5, pady=5)
        self.file_entry = tk.Entry(root, width=25)
        self.file_entry.grid(row=6, column=2, padx=5, pady=5)
        self.open_btn = tk.Button(root, text="Open", command=self.select_file)
        self.open_btn.grid(row=6, column=3, padx=5)

        # Submit button
        self.submit_btn = tk.Button(root, text="Submit", command=self.submit_form)
        self.submit_btn.grid(row=7, column=2, pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
        if file_path:
            img = Image.open(file_path).resize((100, 100))
            self.photo = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.photo)

    def select_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def submit_form(self):
        data = {label: entry.get() for label, entry in self.entries.items()}
        data["Team"] = self.team_var.get()
        data["File"] = self.file_entry.get()

        try:
            with open(data["File"], "w") as f:
                for key, value in data.items():
                    f.write(f"{key}: {value}\n")
            messagebox.showinfo("Success", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmploymentFormApp(root)
    root.mainloop()
