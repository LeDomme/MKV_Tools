# Rename and Sorting Tool

## Overview
This script renames files inside folders based on their parent directory name and organizes folders into alphabet-based subfolders.

## Features
- **Rename Files**: Renames files inside folders by using the parent folder's name (excluding `.py` files).
- **Sort Folders**: Moves folders into alphabetically labeled directories (`A-Z`), `-` for numeric names, and `Other` for special characters.
- **Color-Coded Output**: Uses `colorama` for enhanced terminal output.

## Installation
1. Clone the repository or download the script.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script in the directory where you want to rename and organize files:

```sh
python script.py
```

The script will:
1. Rename files inside subdirectories.
2. Move folders into categorized subfolders.
3. Display renamed/moved/skipped items with color-coded logs.

## Requirements
- Python 3.x
- `colorama` package

## Example Output
```sh
============================== RENAMED FILES ==============================
Movies/ExampleFile.mkv -> Movies/Movies.mkv

============================== MOVED FOLDERS ==============================
Movies -> M/Movies

============================== SKIPPED FILES ==============================
SkippedFile.txt
```

## Notes
- The script will **skip** renaming files if the new filename already exists.
- It will **not** move folders that are already sorted (`A-Z`, `-`).
- The script ensures smooth organization without overwriting existing files.

## License
This project is open-source and available under the MIT License.

