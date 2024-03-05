
# a function that takes a txt file and removes the empty lines
def clean_txt_file(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file, "r", encoding="ISO-8859-1") as f:
            lines = f.readlines()

    with open(file, "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip() != "":
                f.write(line)

clean_txt_file('u.txt')