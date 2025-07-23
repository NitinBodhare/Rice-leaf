import pathlib
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
list_of_files = [ 
    "src/__init__.py",
    "src/helper.py",
    ".env",           
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]
# Create directories and files
for file in list_of_files:
    file_path = pathlib.Path(file)
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created file: {file}")
    else:
        logging.info(f"File already exists: {file}")
    