import sys


"""
<1000   - B Red
<2000   - B Green
<3000   - B Yellow
<4000   - B Blue
<5000   - B Purple
<6000   - B Light Blue
<7000   - B White
<8000   - Red
<9000   - Green
<10000  - Yellow
"""

ansi = {
    "r": "\033[91m",
    "g": "\033[92m",
    "y": "\033[93m",
    "l": "\033[94m",
    "m": "\033[95m",
    "c": "\033[96m",
    "w": "\033[97m",

    "br": "\033[101m",
    "bg": "\033[102m",
    "by": "\033[103m",
    "bl": "\033[104m",
    "bm": "\033[105m",
    "bc": "\033[106m",
    "bw": "\033[107m",

    "rs": "\033[0m",
}

help_cmd    = ["help", "h", "?"]
clear_cmd   = ["clear", "cls", "clc", "c"]
quit_cmd    = ["quit", "exit", "ex", "q"]

watch_cmd   = ["watch", "wtch", "w"]
next_cmd    = ["next", "nxt", "n"]
watched_cmd = ["watched", "seen", "s"]


def clear() -> None:
    sys.stdout.write("\033[H\033[2J")


def cstr(l, col:str) -> str:
    return ansi[col] + str(l) + "\033[0m"


def getc(id_) -> str:
    if id_ < 1000:
        return "br"
    elif id_ < 2000:
        return "bg"
    elif id_ < 3000:
        return "by"
    elif id_ < 4000:
        return "bl"
    elif id_ < 5000:
        return "bm"
    elif id_ < 6000:
        return "bc"
    elif id_ < 7000:
        return "bw"
    elif id_ < 8000:
        return "r"
    elif id_ < 9000:
        return"g"
    else:
        return "y"


def vprint(id_:int, v_name:str) -> None:
    print(f"{cstr('Video id', 'g')}: { cstr(id_, getc(id_)) }\t||\t{cstr(v_name, 'y')}")


def logstd(prefix:str, c:str, out:str) -> None:
    print(f"({cstr(prefix, c)}) {out}")

