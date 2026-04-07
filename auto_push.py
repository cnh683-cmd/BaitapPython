import subprocess

print(" Đang khởi động quá trình đẩy code tự động...")

try:
    print("-> Đang gom các file...")
    subprocess.run(["git", "add", "."], check=True)
    
    print("-> Đang tạo commit...")
    commit_message = "Cập nhật bài tập Python"
    subprocess.run(["git", "commit", "-m", commit_message]) 
    
    print("-> Đang đẩy lên GitHub...")
    subprocess.run(["git", "push"], check=True)
    
    print(" Tuyệt vời! Toàn bộ code đã được cập nhật trên GitHub thành công.")

except subprocess.CalledProcessError as e:
    print("\n Có lỗi khi đẩy code (push).")
    print(f"Chi tiết lỗi hệ thống: {e}")