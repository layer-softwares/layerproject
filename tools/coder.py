import curses

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    line_no = 1
    current_line = ""
    stdscr.addstr(0, 0, f"{line_no} : ")
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == 10:  # Enter key
            line_no += 1
            current_line += '\n'
            stdscr.addstr(f"\n{line_no} : ")
        elif key == curses.KEY_BACKSPACE or key == 127:  # Backspace key
            y, x = stdscr.getyx()
            if x > len(f"{line_no} : "):
                stdscr.delch(y, x - 1)
                current_line = current_line[:-1]
            else:
                if y > 0:
                    stdscr.move(y - 1, len(f"{line_no - 1} : "))
                    stdscr.deleteln()
                    line_no -= 1
        elif key == 27:  # Escape key to exit and save
            save_to_file("output.py", current_line)
            break
        else:
            current_line += chr(key)
            stdscr.addstr(chr(key))
    
    curses.curs_set(1)  # Show cursor after exiting

if __name__ == "__main__":
    curses.wrapper(main)
