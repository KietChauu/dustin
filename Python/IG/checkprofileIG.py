import tkinter as tk
from tkinter import scrolledtext, messagebox
import instaloader
import threading

def fetch_profile():
    username = username_entry.get()
    if not username:
        messagebox.showerror("Lỗi", "Vui lòng nhập tên tài khoản Instagram!")
        return

    def fetch_data():
        loader = instaloader.Instaloader()

        try:
            result_text.delete(1.0, tk.END)  # Clear the text box
            result_text.insert(tk.END, "Đang tìm kiếm...\n")

            profile = instaloader.Profile.from_username(loader.context, username)

            result_text.delete(1.0, tk.END)  # Clear the text box again

            # Display profile information
            result_text.insert(tk.END, f"\n========= Thông tin tài khoản =========\n")
            result_text.insert(tk.END, f"Tên: {profile.full_name}\n")
            result_text.insert(tk.END, f"ID: {profile.userid}\n")
            result_text.insert(tk.END, f"Username: {profile.username}\n")
            result_text.insert(tk.END, f"Người theo dõi: {profile.followers}\n")
            result_text.insert(tk.END, f"Đang theo dõi: {profile.followees}\n")
            result_text.insert(tk.END, f"Bài đăng: {profile.mediacount}\n")
            result_text.insert(tk.END, f"Mô tả: {profile.biography}\n")
            result_text.insert(tk.END, f"Website: {profile.external_url}\n")
            result_text.insert(tk.END, f"Có xác thực: {profile.is_verified}\n")
            result_text.insert(tk.END, f"Tài khoản riêng tư: {profile.is_private}\n")
            result_text.insert(tk.END, f"\n========================================\n")
            result_text.insert(tk.END, "\nDanh sách URL ảnh:\n")

            # Display post URLs
            for post in profile.get_posts():
                result_text.insert(tk.END, f"{post.url}\n")

        except instaloader.exceptions.ProfileNotExistsException:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Không tìm thấy tài khoản!\n")
        except instaloader.exceptions.ConnectionException:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Không thể kết nối đến Instagram!\n")
        except Exception as e:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Đã xảy ra lỗi: {e}\n")

    threading.Thread(target=fetch_data).start()

# GUI Setup
root = tk.Tk()
root.iconbitmap("E:/Documents/CGK/Python/IG/favicon.ico")
root.title("Instagram Profile Viewer")
root.geometry("700x600")
root.configure(bg="#f2f2f2")

# Header
header_label = tk.Label(root, text="Instagram Profile Viewer", font=("Helvetica", 16, "bold"), bg="#f2f2f2", fg="#333")
header_label.pack(pady=10)

# Username input
frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

username_label = tk.Label(frame, text="Tên tài khoản Instagram:", font=("Helvetica", 12), bg="#f2f2f2", fg="#333")
username_label.grid(row=0, column=0, padx=5)

username_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
username_entry.grid(row=0, column=1, padx=5)
username_entry.focus()

# Fetch button
fetch_button = tk.Button(root, text="Lấy thông tin", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=fetch_profile, padx=10, pady=5)
fetch_button.pack(pady=10)

# Scrolled text for results
result_text = scrolledtext.ScrolledText(root, width=80, height=25, font=("Courier", 10))
result_text.pack(pady=10)

footer = tk.Frame(root, bg="#f1f1f1", height=30)
footer.pack(side=tk.BOTTOM, fill=tk.X)
footer_label = tk.Label(footer, text="© 2024 - Dustin", bg="#f1f1f1", font=("Helvetica", 10))
footer_label.pack(pady=5)

# Run the application
root.mainloop()