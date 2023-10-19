def switch_new_line(text, max_line_length):
    lines = []
    current_line = ""

    for line in text.split("\n"):
        for word in line.split():
            if len(current_line + word) < max_line_length:
                current_line += word + ' '
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)
            current_line = ""

    return '\n'.join(lines)


str_ = "Это первый абзац, нужно сделать разделение\nЭто второй абзац, он должен быть отдельно от первого"
print(switch_new_line(str_, 20))