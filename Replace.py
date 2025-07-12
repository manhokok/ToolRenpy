import re
import os

def translate_rpy_file(txt_filepath, rpy_filepath, output_filepath):
    """
    Ghép nội dung từ file TXT vào file RPY dựa trên chỉ số dòng.

    Args:
        txt_filepath (str): Đường dẫn đến file TXT chứa các bản dịch.
        rpy_filepath (str): Đường dẫn đến file RPY gốc.
        output_filepath (str): Đường dẫn đến file RPY đầu ra đã dịch.
    """
    try:
        # Đọc nội dung từ file TXT và tạo một dictionary ánh xạ chỉ số dòng với bản dịch
        translations = {}
        with open(txt_filepath, 'r', encoding='utf-8') as f_txt:
            for line in f_txt:
                line = line.strip()
                if ':' in line:
                    parts = line.split(':', 1)
                    try:
                        line_num = int(parts[0].strip())
                        translation = parts[1].strip()
                        translations[line_num] = translation
                    except ValueError:
                        print(f"Bỏ qua dòng không hợp lệ trong file TXT: {line}")
                        continue

        # Đọc nội dung từ file RPY và thực hiện thay thế
        output_lines = []
        with open(rpy_filepath, 'r', encoding='utf-8') as f_rpy:
            rpy_lines = f_rpy.readlines()

        line_counter = 1  # Bắt đầu đếm dòng từ 1
        for line in rpy_lines:
            # Tìm kiếm các chuỗi trong dấu ngoặc kép
            # Regex này sẽ tìm kiếm các chuỗi bắt đầu và kết thúc bằng dấu ngoặc kép,
            # bao gồm cả trường hợp có thể có khoảng trắng hoặc ký tự khác bên trong.
            match = re.search(r'"([^"]*)"', line)
            if match:
                original_text = match.group(1)
                # Kiểm tra nếu chỉ số dòng hiện tại có trong các bản dịch
                if line_counter in translations:
                    translated_text = translations[line_counter]
                    # Thay thế nội dung bên trong dấu ngoặc kép
                    # Đảm bảo không thêm hoặc bớt dấu ngoặc kép
                    new_line = line.replace(f'"{original_text}"', f'"{translated_text}"', 1)
                    output_lines.append(new_line)
                else:
                    output_lines.append(line)
            else:
                output_lines.append(line)
            line_counter += 1

        # Ghi nội dung đã dịch ra file mới
        with open(output_filepath, 'w', encoding='utf-8') as f_out:
            f_out.writelines(output_lines)

        print(f"Đã ghép thành công và lưu vào: {output_filepath}")

    except FileNotFoundError:
        print("Lỗi: Không tìm thấy một trong các file.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn đến các file
base_path = '/storage/emulated/0/Tool'
txt_file = os.path.join(base_path, 'to_translate_trans.txt')
rpy_file = os.path.join(base_path, 'script.rpy')
output_file = os.path.join(base_path, 'script_translated.rpy')

# Gọi hàm để thực hiện việc ghép file
translate_rpy_file(txt_file, rpy_file, output_file)

