import re

# Đường dẫn file đầu vào và đầu ra
input_path = "/storage/emulated/0/Tool/script.rpy"
output_path = "/storage/emulated/0/Tool/to_translate.txt"

# Regex để tìm dòng có văn bản trong dấu ngoặc kép
text_line_pattern = re.compile(r'^\s*(\d+)?\s*.*?"(.*?)"')

# Danh sách các từ khóa để loại trừ
exclusion_keywords = [
    "asset/", "http", "https", ".ttf", "#000", "#ff", ".png", ".jpg", "{color", ".svg", "*", ".mp3", "audio/", ".ogg"
]

def is_valid_line(text):
    text_lower = text.lower()
    return not any(keyword in text_lower for keyword in exclusion_keywords)

# Xử lý và trích xuất
with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for lineno, line in enumerate(infile, start=1):
        match = text_line_pattern.search(line)
        if match:
            text = match.group(2).strip()
            if text and is_valid_line(text):
                outfile.write(f"{lineno}:{text}\n")

print("Hoàn tất! Văn bản đã được lưu vào to_translate.txt.")