def justify_paragraph_string(paragraph, page_width):
    words = paragraph.split()
    lines = []
    current_line = []

    current_length = 0
    for word in words:
        if current_length + len(word) + len(current_line) <= page_width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(current_line)

    justified_string_lines = []
    for line in lines:
        if len(line) == 1:
            justified_string_lines.append(line[0])
        else:
            total_spaces = page_width - sum(len(word) for word in line)
            spaces_between_words = total_spaces // (len(line) - 1)
            extra_spaces = total_spaces % (len(line) - 1)

            justified_line = line[0]
            for i in range(1, len(line)):
                spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
                justified_line += ' ' * spaces + line[i]

            justified_string_lines.append(justified_line)

    return justified_string_lines

# Example usage
paragraph = "This is a simple text but a complicated problem to be solved, so we are adding more text to see that it actually works."
page_width = 20
justified_txt_output = justify_paragraph_string(paragraph, page_width)

for i, line in enumerate(justified_txt_output, 1):
    print(f"Array [{i}] = \"{line}\"")
