"""Lib for work with csv files"""
import csv


def read_csv(filename):
    """Func for read csv file. Return fields and rows"""
    with open(filename, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)
    return fields, rows


def write_csv(filename, fields, rows) -> bool:
    """Func for write csv file. Get filename, fields and rows. Return bool"""
    with open(filename, 'w', newline='', encoding='UTF-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    return True


def insert_csv_row(filename, row, index=None) -> bool:
    """Func insert row by index. Return true"""
    fields, rows = read_csv(filename)
    if index:
        rows.insert(index + 1, row)
    else:
        rows.append(row)
    return write_csv(filename, fields, rows)


def delete_csv_row(filename, index=None):
    """Func delete row by index. Return true"""
    fields, rows = read_csv(filename)
    if not index is None:
        index = index - 1 if index > 0 else 0
        rows.pop(index)
    else:
        rows.pop()
    return write_csv(filename, fields, rows)


def print_csv(filename):
    fields, rows = read_csv(filename)
    for col in fields:
        print("%15s" % col, end='')
    print()
    for row in rows:
        for col in row:
            print("%15s" % col, sep='', end='')
        print()