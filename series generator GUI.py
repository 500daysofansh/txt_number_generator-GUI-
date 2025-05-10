import tkinter as tk
from tkinter import messagebox, filedialog
import os

def generate_number_lists(start, end, directory):
    """
    Generates 10 files containing lists of 10-digit numbers
    from start to end (inclusive) and writes them to text files.

    :param start: Starting number (inclusive)
    :param end: Ending number (inclusive)
    :param directory: Directory to save the output files
    """
    # Validate that start and end are 10-digit numbers
    if not (1000000000 <= start <= 9999999999) or not (1000000000 <= end <= 9999999999):
        raise ValueError("Both start and end must be 10-digit numbers.")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

    # Fixed range for each file
    range_per_file = (end - start + 1) // 10  # Calculate the range for each file

    current_start = start

    for file_index in range(10):  # Create 10 files
        current_end = current_start + range_per_file - 1
        
        # Ensure we do not exceed the end limit for the last file
        if file_index == 9:  # Last file
            current_end = end
        
        # Generate the filename based on start and end numbers
        filename = f"number_list_{current_start}_{current_end}.txt"
        full_path = os.path.join(directory, filename)
        
        with open(full_path, "w") as file:
            for number in range(current_start, current_end + 1):
                file.write(f"{number}\n")
        
        print(f"File saved as {full_path}")
        current_start += range_per_file

def on_generate():
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())
        
        # Ask for the directory to save files
        directory = filedialog.askdirectory(title="Select Directory to Save Files")
        if not directory:
            raise ValueError("No directory selected.")
        
        generate_number_lists(start, end, directory)
        messagebox.showinfo("Success", "Files generated successfully!")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Number List Generator")

# Create and place labels and entries
tk.Label(root, text="Start Number:").grid(row=0, column=0)
start_entry = tk.Entry(root)
start_entry.grid(row=0, column=1)

tk.Label(root, text="End Number:").grid(row=1, column=0)
end_entry = tk.Entry(root)
end_entry.grid(row=1, column=1)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Files", command=on_generate)
generate_button.grid(row=2, columnspan=2)

# Start the GUI event loop
root.mainloop()
