import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def rename_files_with_parent_dir(base_dir):
    renamed_files = []
    skipped_files = []

    for dirpath, dirnames, filenames in os.walk(base_dir):
        parent_dir_name = os.path.basename(dirpath)

        # Ignore the "_sort" folder
        if parent_dir_name == "_sort":
            continue

        for filename in filenames:
            file_extension = os.path.splitext(filename)[1]

            # Ignore Python files
            if file_extension == ".py":
                continue

            new_filename = f"{parent_dir_name}{file_extension}"
            new_filepath = os.path.join(dirpath, new_filename)

            # Rename only if the new filename doesn't exist
            if not os.path.exists(new_filepath):
                old_filepath = os.path.join(dirpath, filename)
                os.rename(old_filepath, new_filepath)

                # Convert to relative path for clean output
                relative_old = os.path.relpath(old_filepath, base_dir)
                relative_new = os.path.relpath(new_filepath, base_dir)

                renamed_files.append(f"{Fore.BLUE}{relative_old} {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}{relative_new}")
            else:
                relative_new = os.path.relpath(new_filepath, base_dir)
                skipped_files.append(f"{Fore.WHITE}{relative_new}")

    # Log output with separator
    if renamed_files:
        print(f"\n{Fore.GREEN}{'='*30} RENAMED FILES {'='*30}")
        print("\n".join(renamed_files))

    if skipped_files:
        print(f"\n{Fore.YELLOW}{'='*30} SKIPPED FILES {'='*30}")
        print("\n".join(skipped_files))

def move_folders_by_alphabet(base_dir):
    moved_folders = []
    skipped_folders = []

    # Collect existing A-Z and "-" folders to avoid moving them
    existing_sort_folders = set(f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and (f.isalpha() or f == "-"))

    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)

        # Check if it's a directory and not a sorting folder (A-Z, "-")
        if os.path.isdir(folder_path) and folder_name not in existing_sort_folders and folder_name not in ["_sort"]:
            first_char = folder_name[0].upper()

            # Numbers go to "-" folder
            if first_char.isdigit():
                target_folder = "-"
            elif first_char.isalpha():
                target_folder = first_char
            else:
                target_folder = "Other"

            target_dir = os.path.join(base_dir, target_folder)

            # Ensure the destination folder exists
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            # Move the folder only if it doesn’t already exist
            new_folder_path = os.path.join(target_dir, folder_name)
            if not os.path.exists(new_folder_path):
                os.rename(folder_path, new_folder_path)

                # Convert to relative path for clean output
                relative_old = os.path.relpath(folder_path, base_dir)
                relative_new = os.path.relpath(new_folder_path, base_dir)

                moved_folders.append(f"{Fore.BLUE}{relative_old} {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}{relative_new}")
            else:
                relative_new = os.path.relpath(new_folder_path, base_dir)
                skipped_folders.append(f"{Fore.LIGHTGREEN_EX}{relative_new}")

    # Log output with separator
    if moved_folders:
        print(f"\n{Fore.CYAN}{'='*30} MOVED FOLDERS {'='*30}")
        print("\n".join(moved_folders))

    if skipped_folders:
        print(f"\n{Fore.RED}{'='*30} SKIPPED FOLDERS {'='*30}")
        print("\n".join(skipped_folders))

# call
if __name__ == "__main__":
    print(f"{Fore.YELLOW}{Style.BRIGHT}MKV Rename and Sorting Tool{Style.RESET_ALL}\n")
    current_path = os.getcwd()
    
    # Rename files inside folders
    rename_files_with_parent_dir(current_path)

    # Move folders into alphabet-based subfolders
    move_folders_by_alphabet(current_path)

print("\n\n\n\n")
print(f"{Fore.CYAN}This window will stay open until you press Enter{Style.RESET_ALL}")
input(f"{Fore.YELLOW}Press Enter to close...{Style.RESET_ALL}")
