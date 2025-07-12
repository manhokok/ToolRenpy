import re

def main():
    # Bước 1: Yêu cầu đường dẫn file
    file_path = input("Nhập đường dẫn tới file .txt: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Không tìm thấy file. Vui lòng kiểm tra lại đường dẫn.")
        return

    # Bước 2: Nhập mẫu kí tự cần tìm (ví dụ: [*])
    pattern_input = input("Nhập mẫu ký tự cần tìm (ví dụ: [*]): ").strip()

    # Kiểm tra định dạng mẫu
    if pattern_input.count('*') != 1:
        print("Mẫu không hợp lệ. Cần chứa đúng một dấu * để đại diện cho văn bản cần thay.")
        return

    # Tạo regex từ pattern
    pattern_escaped = re.escape(pattern_input)
    pattern_regex = pattern_escaped.replace('\\*', '(.*?)')  # non-greedy

    # Bước 3: Nhập văn bản thay thế
    replacement = input("Nhập văn bản thay thế cho phần nằm trong dấu [ ]: ").strip()

    # Bước 4: Thực hiện thay thế
    def replace_match(match):
        full = match.group(0)
        # Lấy ký tự đầu và cuối làm dấu bao quanh
        prefix = full[0]
        suffix = full[-1]
        return f"{prefix}{replacement}{suffix}"

    new_content = re.sub(pattern_regex, replace_match, content)

    # Ghi đè hoặc tạo file mới
    output_path = input("Nhập tên file để lưu kết quả (nhấn Enter để ghi đè file cũ): ").strip()
    if not output_path:
        output_path = file_path

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Đã thay thế xong. Kết quả được lưu vào '{output_path}'.")

if __name__ == "__main__":
    main()