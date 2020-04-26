#!/usr/bin/python3
import sys
import re
import os.path
import subprocess

def add_indent(text):
    if not text:
        return []
    text = text.split("\n")
    result = []
    for line in text:
        s = line.strip()
        # do ot strip big indent, but strip small
        if len(s) > len(line) - 4:
            line = s
        result.append("    " + line)
    return result

def replace_note(text):
    result = ["", "", ".. note::"]
    result += add_indent(match.group(1))
    result += ["", ""]
    return "\n".join(result)


def replace_task(match):
    result = ["", "", ".. task::"]
    if match.group(1):
        result += ["    :name: " + match.group(1)[1:]]
    result += [""]
    for i in range(2, 5):
        result += add_indent(match.group(i)) + ["    |"]
    result += ["", ""]
    return "\n".join(result)

def replace_image(match):
    filename = match.group(3)
    initial_filename = filename
    while filename != "" and not os.path.exists(filename):
        new_filename = filename[filename.find("/") + 1:]
        if new_filename == filename:
            break
        filename = new_filename
    if not os.path.exists(filename):
        raise Exception("Can't find file {}".format(filename))
    resultname = filename + ".png"
    print("filename=", filename)
    subprocess.check_call("gs -dSAFER -dBATCH -dNOPAUSE -dEPSCrop -r600 -sDEVICE=pngalpha".split() + ["-sOutputFile=" + resultname, filename])
    return match.group(0).replace(initial_filename, resultname)
    

if ".tmp." in sys.argv[1]:
    sys.exit(0)

print("Process ", sys.argv[1])
with open(sys.argv[1], "r") as f:
    data = f.read()

data = re.sub(r"(\\(\w*)header(\w*)\{(.*?)\})(\s*" + "\n" + r")*(\\label\{(.*?)\})", "\\6\n\\1", data)

replacements = [
    ("\"=", "-"),
    ("\"-", "-"),
    ("\"---", "—"),
    ("<<", "«"),
    (">>", "»"),
    ("\"<", "«"),
    ("\">", "»"),
    ("\hm", ""),
    ("\mbox", ""),
    ("`", "'"),
    ("\header{", "\subsection{"),
    ("\lheader{", "\paragraph{"),
    ("\lheadernd{", "\paragraph{"),
    ("\\task", "||task"),
    ("\\note", "||note"),
    ("ulist", "itemize")
]

for r in replacements:
    data = data.replace(*r)

data = re.sub(r"\\tt\s*(.*?)\}", r"\\texttt{\1}}", data)
data = re.sub(r"\\includegraphics(\[(.*)\])?\{(.*?)\}", replace_image, data)
data = re.sub(r"\\(label|ref)\{(.*?)\}", r"||\1|\2|", data)

tempfile = sys.argv[1] + ".tmp.tex" 
with open(tempfile, "w") as f:
    f.write(data)

basename, ext = os.path.splitext(sys.argv[1])
result_file = basename + ".rst"

subprocess.check_call(["pandoc", "-f", "latex", "-t", "rst", tempfile, "-o", result_file])

with open(result_file, "r") as f:
    data = f.read()

data = re.sub(r"\\\|\\\|label\\\|(.*?)\\\|", r"\n\n.. _\1:\n\n", data)
data = re.sub(r"\\\|\\\|ref\\\|(.*?)\\\|", r":ref:`\1`", data)
data = re.sub("\\\\\\|\\\\\\|task(n[^|]*)?\\\\\\|([^|]*)\\\\\\|\\s*\\\\\\|([^|]*)\\\\\\|\\s*\\\\\\|([^|]*)\\\\\\|\\s*", 
              replace_task, data)

with open(result_file, "w") as f:
    f.write(data)