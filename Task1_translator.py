import tkinter as tk
from tkinter import messagebox, ttk
from deep_translator import GoogleTranslator


def translate_text():
    text_to_translate = text_entry.get("1.0", tk.END).strip()

    # Get the selection directly and convert to lowercase
    source_lang = src_lang_combo.get().strip().lower()
    target_lang = dest_lang_combo.get().strip().lower()

    # Handle the "auto" case for the source language
    if "auto" in source_lang:
        source_lang = "auto"

    if not text_to_translate:
        messagebox.showwarning("Input Error", "Please enter some text to translate.")
        return

    try:
        # Send text to API and get translated response
        translated = GoogleTranslator(
            source=source_lang, target=target_lang
        ).translate(text_to_translate)

        # Display the translated text clearly
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")


# Fulfills requirement: Create a user interface
root = tk.Tk()
root.title("CodeAlpha - Language Translation Tool")
root.geometry("500x450")

# Language choices mapping
languages = ["Auto / English", "English", "Spanish", "French", "German", "Hindi"]

# UI Elements
tk.Label(root, text="Enter Text:", font=("Arial", 10, "bold")).pack(pady=5)
text_entry = tk.Text(root, height=5, width=55)
text_entry.pack()

# Source and Target Selection
lang_frame = tk.Frame(root)
lang_frame.pack(pady=10)

tk.Label(lang_frame, text="From:").grid(row=0, column=0, padx=5)
src_lang_combo = ttk.Combobox(lang_frame, values=languages, width=15)
src_lang_combo.grid(row=0, column=1, padx=5)
src_lang_combo.set("Auto / English")

tk.Label(lang_frame, text="To:").grid(row=0, column=2, padx=5)
dest_lang_combo = ttk.Combobox(lang_frame, values=languages, width=15)
dest_lang_combo.grid(row=0, column=3, padx=5)
dest_lang_combo.set("Spanish")

# Translate Button
translate_btn = tk.Button(
    root, text="Translate", command=translate_text, bg="#4CAF50", fg="white"
)
translate_btn.pack(pady=5)

tk.Label(root, text="Translated Text:", font=("Arial", 10, "bold")).pack(pady=5)
output_text = tk.Text(root, height=5, width=55)
output_text.pack()

# Optional: Copy Button feature for better usability
copy_btn = tk.Button(root, text="Copy Result", command=copy_to_clipboard)
copy_btn.pack(pady=10)

root.mainloop()