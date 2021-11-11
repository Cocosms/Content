import csv
import datetime
import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter.ttk import Progressbar

root = Tk()


def parse_gate_log(filename):
    parsing_log_path = str(filename).strip("['']")
    print(parsing_log_path)
    check_file_arr = parsing_log_path.rsplit('/', 6)
    check_file = check_file_arr[-1]
    parsed_path = parsing_log_path.strip(check_file)
    parsed_file_arr = check_file.split('.')
    parsed_file_name = parsed_file_arr[0].split('-')
    print(parsed_file_arr, parsed_file_name)
    parsed_ext = '.' + parsed_file_arr[-1]
    parsed_file = check_file.strip(parsed_ext) + '_parsed'
    print(parsed_file)
    gate_parsing(parsing_log_path,parsed_file,parsed_ext,parsed_path)


def parse_oth_log(filename):
    parsing_log_path = str(filename).strip("['']")
    print(parsing_log_path)
    check_file_arr = parsing_log_path.rsplit('/', 6)
    check_file = check_file_arr[-1]
    parsed_path = parsing_log_path.strip(check_file)
    parsed_file_arr = check_file.split('.')
    parsed_ext = '.' + parsed_file_arr[-1]
    parsed_file = check_file.strip(parsed_ext) + '_parsed'
    print(parsed_file)
    oth_parsing(parsing_log_path,parsed_file,parsed_ext,parsed_path)


def parse_pamm_log(filename):
    parsing_log_path = str(filename).strip("['']")
    print(parsing_log_path)
    check_file_arr = parsing_log_path.rsplit('/', 6)
    check_file = check_file_arr[-1]
    parsed_path = parsing_log_path.strip(check_file)
    parsed_file_arr = check_file.split('.')
    parsed_file_name = parsed_file_arr[0].split('-')
    print(parsed_file_arr, parsed_file_name)
    parsed_ext = '.' + parsed_file_arr[-1]
    parsed_file = check_file.strip(parsed_ext) + '_parsed'
    print(parsed_file)
    pamm_parsing(parsing_log_path,parsed_file,parsed_ext,parsed_path)


def gate_parsing(parsing_log_path,parsed_file,parsed_ext,parsed_path):
    date = datetime.date.today()
    file_path = str(parsed_path) + str(parsed_file) + str(parsed_ext)
    i = 1
    while os.path.isfile(file_path):
        parsed_file = parsed_file + f'({i})'
        file_path = str(parsed_path) + str(parsed_file) + str(parsed_ext)
        parsed_file = parsed_file.rstrip(f'({i})')
        i += 1
    else:
        pass
    print(parsed_file, file_path)
    with open(parsing_log_path) as r_file, \
            open(file_path, mode="w+", encoding='utf-8') as w_file:
        reader = csv.reader(r_file, delimiter=';')
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        line_count = 0
        for row in reader:
            try:
                if 'Warn' in row or 'WARN' in row or 'ERR' in row or 'Error' in row or '8' in row[3] or '30' in row[3]\
                        or '1' in row[3] or '5' in row[3] or '6' in row[3] or '7' in row[3]:
                    if 'Depth' not in row[4]:
                        file_writer.writerow(row)
                        line_count += 1
                else:
                    pass
            except Exception:
                string = str(row).strip("['']")
                if 'at' in string:
                    if 'Feeder:' in string or 'aggregated volumes' in string or 'S:' in string:
                        pass
                    else:
                        line_count += 1
                        file_writer.writerow(row)
                else:
                    pass
        w_file.close()
    r_file.close()
    print(f'Processed {line_count} lines.')


def oth_parsing(parsing_log_path,parsed_file,parsed_ext,parsed_path):
    date = datetime.date.today()
    file_path = str(parsed_path) + str(parsed_file) + str(parsed_ext)
    i = 1
    while os.path.isfile(file_path):
        parsed_file = parsed_file + f'({i})'
        file_path = str(parsed_path) + str(parsed_file) + str(parsed_ext)
        parsed_file = parsed_file.rstrip(f'({i})')
        i += 1
    else:
        pass
    print(parsed_file, file_path)
    with open(parsing_log_path) as r_file, \
            open(file_path, mode="w+", encoding='utf-8') as w_file:
        reader = csv.reader(r_file, delimiter='|')
        file_writer = csv.writer(w_file, delimiter="|", lineterminator="\r")
        line_count = 0
        for row in reader:
            try:
                if 'WARN' in row[0] or 'ERR' in row[0] or 'WARN' in row[1] or 'ERR' in row[1]:
                    if 'Depth' not in row[4]:
                        file_writer.writerow(row)
                        line_count += 1
                else:
                    pass
            except Exception:
                string = str(row).strip("['']")
                if 'at' in string:
                    if 'Feeder:' in string or 'aggregated volumes' in string or 'S:' in string:
                        pass
                    else:
                        line_count += 1
                        file_writer.writerow(row)
                else:
                    pass
        w_file.close()
    r_file.close()
    print(f'Processed {line_count} lines.')


def pamm_parsing(parsing_log_path,parsed_file,parsed_ext,parsed_path):
    date = datetime.date.today()
    file_path = str(parsed_path) + str(parsed_file) + str(parsed_ext)
    i = 1
    while os.path.isfile(file_path):
        parsed_file = parsed_file + f'({i})'
        file_path = str(parsed_path) + str(parsed_file) + str(parsed_ext)
        parsed_file = parsed_file.rstrip(f'({i})')
        i += 1
    else:
        pass
    print(parsed_file, file_path)
    with open(parsing_log_path) as r_file, \
            open(file_path, mode="w+", encoding='utf-8') as w_file:
        reader = csv.reader(r_file, delimiter='|')
        file_writer = csv.writer(w_file, delimiter="|", lineterminator="\r")
        line_count = 0
        for row in reader:
            try:
                if 'WARN_LVL' in row or 'ERR__LVL' in row:
                    if 'Depth' not in row[4]:
                        file_writer.writerow(row)
                        line_count += 1
                else:
                    pass
            except Exception:
                string = str(row).strip("['']")
                if 'at' in string:
                    if 'Feeder:' in string or 'aggregated volumes' in string or 'S:' in string:
                        pass
                    else:
                        line_count += 1
                        file_writer.writerow(row)
                else:
                    pass
        w_file.close()
    r_file.close()
    print(f'Processed {line_count} lines.')


def selectfile():
    filename = filedialog.askopenfilename()
    filename_new = filename.replace("\\", "/")
    selected_path.insert(0, filename_new)


def fileopen():
    txt = str(selected_path.get()).replace("\\", "/")
    bar['value'] = 100
    if log_type.get() == 'Gate':
        parse_gate_log(txt)
    elif log_type == 'Other':
        parse_oth_log(txt)
    else:
        parse_pamm_log(txt)


def exitcall():
    root.destroy()


root.geometry('600x400')
root.title("Добро пожаловать в приложение Parsing-Gate_Logs")
log_type = str
main_menu = Menu(root)
open_file = Menu(main_menu, tearoff=0)
open_file.add_command(label='Новый', command=selectfile)
main_menu.add_cascade(label='Файл', menu=open_file)
root.config(menu=main_menu)
frame1 = Frame(root)
frame1.pack(fill=BOTH, expand=True)
frame2 = Frame(root)
frame2.pack(fill=BOTH, expand=True)
frame3 = Frame(root)
frame3.pack(fill=BOTH, expand=True)
frame4 = Frame(root)
frame4.pack(fill=BOTH, expand=True)
log_type = Combobox(frame1, state='readonly')
log_type['values'] = ('Gate','Other','PAMM')
log_type.current(0)
log_type.pack(side=TOP, pady=10)
lbl1 = Label(frame2, text='Choose the file: ', width=15)
lbl1.pack(side=LEFT, padx=5, pady=5)
selected_path = Entry(frame2, width=65)
selected_path.pack(side=LEFT, anchor='w')
button_to_view = Button(frame2, text='View', command=selectfile, width=10)
button_to_view.pack(side=RIGHT, padx=10, pady=25)
bar = Progressbar(frame3, length=200)
bar.pack(side=TOP, pady=15)
button_to_exit = Button(frame4, text='Exit', command=exitcall)
button_to_exit.pack(side=RIGHT, padx=15)
button_to_apply = Button(frame4, text='Apply', command=fileopen)
button_to_apply.pack(side=RIGHT, padx=15)
btn = Button(root, text="Apply", command=selectfile)
root.mainloop()
