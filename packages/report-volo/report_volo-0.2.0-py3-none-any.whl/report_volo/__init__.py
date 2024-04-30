from .report import Record, FileNotFound, ReportInvalidOrder


def dict_init(records_dict=None):
    return Record.dict_init(records_dict)


def read_file(path, insert_file):
    return Record.read_file(path, insert_file)


def read_abbr(path, records_dict=None, abbr_file="abbreviations.txt"):
    return Record.read_abbr(path, records_dict, abbr_file)


def file_name(insert_file):
    return Record.file_name(insert_file)


def read_logs(path, records_dict=None, start_file="start.log", end_file="end.log"):
    return Record.read_logs(path, records_dict, start_file, end_file)


def build_report(path, order="asc"):
    return Record.build_report(path, order)


def print_report(good_records, bad_records, border_line: int = 15):
    return Record.print_report(good_records, bad_records)


def cli(args_list=None):
    return Record.cli(args_list)


__all__ = [
    "FileNotFound",
    "ReportInvalidOrder",
    "Record",
    "dict_init",
    "read_file",
    "read_abbr",
    "file_name",
    "read_logs",
    "print_report",
    "cli",
    "build_report",
]
