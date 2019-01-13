import re
import sys

def cleanup_imports(filename):
    with open(filename) as f:
        lines = f.readlines()

    p = re.compile('\s*import .*')
    imports = [line for line in lines if p.match(line)]
    without_imports = [line for line in lines if not p.match(line)]
    for line in imports:
        class_name = re.compile('.*\.(\w+)\;').match(line).group(1);
        for without_import_line in without_imports:
            if class_name in without_import_line and re.compile('\s*//').match(without_import_line) is None:
                break
        else: # Not found
            lines.remove(line)
    
    with open(filename, 'w') as w:
        w.writelines(lines)
        
if len(sys.argv) < 2:
    sys.exit('Usage: python cleanup_imports.py [file ...]')

filenames = sys.argv[1:]
for filename in filenames:
    cleanup_imports(filename)
