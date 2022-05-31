with open("text.txt", "r") as file:
    newline_break = ""
    for readline in file: 
        line_strip = readline.strip()
        newline_break += ' ' +line_strip
    print(newline_break)