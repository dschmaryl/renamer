#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_replace(old_name, find_string, replace_string):
    if find_string not in old_name:
        return None

    return old_name.replace(find_string, replace_string, 1)


def insert(old_name, insert_position, insert_string):
    if not insert_string:
        return None
    if insert_position:
        try:
            position_int = max(0, int(insert_position) - 1)
        except ValueError:
            return None
    else:
        position_int = 0

    return old_name[:position_int] + insert_string + old_name[position_int:]


def strip_chars(old_name, strip_position, strip_length):
    try:
        strip_int = max(0, int(strip_length))
    except ValueError:
        return None
    if strip_position:
        try:
            position_int = max(0, int(strip_position) - 1)
        except ValueError:
            return None
    else:
        position_int = 0

    return old_name[:position_int] + old_name[position_int+strip_int:]


def format_numbers(old_name, format_length, format_position):
    if format_length:
        try:
            format_length = min(max(2, int(format_length)), 6)
        except ValueError:
            return None
    else:
        format_length = 2
    if format_position:
        try:
            format_position = max(0, int(format_position) - 1)
        except ValueError:
            return None
    else:
        format_position = 0
    format_string = '%0' + str(format_length) + 'd'
    old_number = ''
    for i in range(format_length):
        if old_name[format_position:][i].isdigit():
            old_number += old_name[format_position:][i]
    try:
        new_number = format_string % int(old_number)
    except ValueError:
        return None

    return old_name.replace(old_number, new_number, 1)
