def надрукувати(*арг, розд=' ', закінчення='\n', файл=None):
    """
    Друк значень до потоку, чи до sys.stdout через default


    Необов'язкові ключі-аргументи:

    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    print(*арг, sep=розд, end=закінчення, file=файл)
