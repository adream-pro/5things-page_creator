import os
from datetime import datetime

def rename_file(page_info,html):
    new_file_name = f"{page_info['sujet']}_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.html"
    with open(new_file_name, "w") as f:
        f.write(html)
    print(f"File created with name {new_file_name}")