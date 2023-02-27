import user_interface as ui

def main():
    ui.print_help()
    while ui.still_running(): pass

if __name__ == '__main__':
    main()

# TODO
# logger.py
# удаление пустых строк # DONE
# проверок на корректность ввода