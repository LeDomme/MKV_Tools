# Rename and Sorting Tool

## Overview

This script organizes folders by moving them into alphabetically categorized directories and renaming specific `.mkv` files. It is particularly useful for structuring media files and cleaning up unnecessary folders and files.

## Features

- Moves folders into categorized directories based on their starting letter.
- Renames `.mkv` files from the `encode` subdirectory to match the parent folder name.
- Deletes all non-`.mkv` files and extra subdirectories.
- Provides a summary of moved, renamed, and skipped folders.
- Uses `colorama` for color-coded terminal output.

## Installation

1. Clone or download the script.
2. Install the required dependency:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script in the directory where your folders are located:

```sh
python rename_titles.py
```

## Dependencies

- Python 3.x
- `colorama` (for colored terminal output)

## Example

Assume the following directory structure:

```
base_directory/
    MovieA/
        encode/
            MovieA.mkv
        extra_file.txt
    FilmB/
        encode/
            FilmB.mkv
```

After running the script, the structure will be:

```
base_directory/
    M/
        MovieA/
            MovieA.mkv
    F/
        FilmB/
            FilmB.mkv
```

## Notes

- Folders named with a single character (A-Z) or "-" are skipped.
- If an `.mkv` file with the correct name already exists, the script will not overwrite it.
- All non-`.mkv` files and empty subdirectories are deleted.

## License

This project is licensed under the MIT License.
