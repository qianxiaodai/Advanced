# -*- coding: utf-8 -*-


def my_read_lines(f, newline):
    buf = ""
    while True:
        while newline in buf:  # 读入的文件过长，包含两个buffer
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096 * 10)
        if not chunk:
            # 如果已经读到文件结尾
            yield buf
            break
        buf += chunk


with open("input.txt") as f:
    for line in my_read_lines(f, "{|}"):
        print(line)


