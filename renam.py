import os

def rename_items(root_path, target_str, replace_str):
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
        # Đổi tên file
        for filename in filenames:
            if target_str in filename:
                old_path = os.path.join(dirpath, filename)
                new_name = filename.replace(target_str, replace_str)
                new_path = os.path.join(dirpath, new_name)
                os.rename(old_path, new_path)
                print(f"Đổi tên file: {old_path} -> {new_path}")

        # Đổi tên thư mục
        for dirname in dirnames:
            if target_str in dirname:
                old_path = os.path.join(dirpath, dirname)
                new_name = dirname.replace(target_str, replace_str)
                new_path = os.path.join(dirpath, new_name)
                os.rename(old_path, new_path)
                print(f"Đổi tên thư mục: {old_path} -> {new_path}")

def main():
    root = input("📁 Nhập đường dẫn tới thư mục gốc: ").strip()
    if not os.path.isdir(root):
        print("❌ Đường dẫn không hợp lệ.")
        return

    target = input("🔍 Tên/ký hiệu cần tìm trong tên file hoặc thư mục (ví dụ: x-): ").strip()
    if not target:
        print("❌ Bạn chưa nhập chuỗi cần tìm.")
        return

    replace = input("✏️ Chuỗi thay thế (để trống nếu muốn xóa): ")

    print("\n⚙️ Bắt đầu đổi tên...\n")
    rename_items(root, target, replace)
    print("\n✅ Đã hoàn tất!")

if __name__ == "__main__":
    main()