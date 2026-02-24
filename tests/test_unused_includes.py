import os
import re
import sys

def get_all_includes():
    includes_dir = '_includes'
    if not os.path.exists(includes_dir):
        return []

    includes = []
    for root, dirs, files in os.walk(includes_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), includes_dir)
            includes.append(rel_path)
    return includes

def check_usage(include_file):
    # Escaped version for regex
    esc = re.escape(include_file)

    # Patterns for the file with extension
    # We ensure it's followed by space or the end of the tag to avoid prefix matches
    patterns = [
        re.compile(r'{%\s*include\s+"' + esc + r'"(\s+[^%]*|)\s*%}'),
        re.compile(r"{%\s*include\s+'" + esc + r"'(\s+[^%]*|)\s*%}"),
        re.compile(r'{%\s*include\s+' + esc + r'(\s+[^%]*|)\s*%}')
    ]

    # Patterns for the file without .html extension
    if include_file.endswith('.html'):
        base = re.escape(include_file[:-5])
        patterns.extend([
            re.compile(r'{%\s*include\s+"' + base + r'"(\s+[^%]*|)\s*%}'),
            re.compile(r"{%\s*include\s+'" + base + r"'(\s+[^%]*|)\s*%}"),
            re.compile(r'{%\s*include\s+' + base + r'(\s+[^%]*|)\s*%}')
        ])

    for root, dirs, files in os.walk('.'):
        # Skip some directories
        if any(skip in root for skip in ['.git', 'vendor', '_site', '.bundle']):
            continue

        for file in files:
            if file.endswith(('.html', '.md', '.scss', '.markdown')):
                filepath = os.path.join(root, file)
                # Don't check the file itself if it's in _includes
                if os.path.normpath(filepath) == os.path.normpath(os.path.join('_includes', include_file)):
                    continue
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        for pattern in patterns:
                            if pattern.search(content):
                                print(f"Found usage of {include_file} in {filepath}")
                                return True
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    return False

def main():
    includes = get_all_includes()
    unused_includes = []

    print(f"Checking {len(includes)} include files...")
    for include in includes:
        if not check_usage(include):
            unused_includes.append(include)
            print(f"UNUSED: {include}")
        else:
            print(f"USED: {include}")

    if unused_includes:
        print(f"\nFound {len(unused_includes)} unused include files.")
        return 1
    else:
        print("\nAll include files are used.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
