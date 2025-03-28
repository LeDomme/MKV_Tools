import os
import shutil
from colorama import Fore, Style, Back, init

# Initialize Colorama
init(autoreset=True)

def move_to_corresponding_folder(folder_path, base_dir, moved_folders, skipped_folders):
    folder_name = os.path.basename(folder_path)
    if folder_name.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or folder_name == "-":
        skipped_folders.append(f"{Fore.YELLOW}{folder_path} (reserved folder){Style.RESET_ALL}")
        return
    
    first_char = folder_name[0].upper()
    dest_folder = os.path.join(base_dir, first_char if first_char.isalpha() else "-")
    os.makedirs(dest_folder, exist_ok=True)
    
    dest_folder_path = os.path.join(dest_folder, folder_name)
    shutil.move(folder_path, dest_folder_path)
    moved_folders.append(f"{Fore.GREEN}{Style.DIM}{folder_path} -> {dest_folder_path}{Style.RESET_ALL}")

def process_folders(base_dir):
    moved_folders, skipped_folders, renamed_files = [], [], []

    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            continue
        
        if folder.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or folder == "-":
            skipped_folders.append(f"{Fore.YELLOW}{Style.DIM}{folder_path} (reserved folder){Style.RESET_ALL}")
            continue

        print(f"{Fore.YELLOW}Processing: {folder_path}{Style.RESET_ALL}")
        encode_path = os.path.join(folder_path, "encode")
        
        if os.path.exists(encode_path) and os.path.isdir(encode_path):
            mkv_files = [f for f in os.listdir(encode_path) if f.endswith(".mkv")]
            if mkv_files:
                mkv_file = mkv_files[0]
                src_path = os.path.join(encode_path, mkv_file)
                dest_path = os.path.join(folder_path, mkv_file)
                shutil.move(src_path, dest_path)
                
                new_filename = f"{folder}.mkv"
                new_filepath = os.path.join(folder_path, new_filename)
                if not os.path.exists(new_filepath):
                    os.rename(dest_path, new_filepath)
                    renamed_files.append(f"{Fore.CYAN}{Style.DIM}{dest_path} -> {new_filepath}{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}Renamed: {dest_path} -> {new_filepath}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}File already exists: {new_filepath}{Style.RESET_ALL}")
        
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path) or not item.endswith(".mkv"):
                try:
                    if os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                    else:
                        os.remove(item_path)
                    print(f"{Fore.RED}Deleted: {item_path}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.YELLOW}Error deleting {item_path}: {e}{Style.RESET_ALL}")
        
        move_to_corresponding_folder(folder_path, base_dir, moved_folders, skipped_folders)
    
    print(f"\n{Fore.CYAN}================================= SUMMARY ================================={Style.RESET_ALL}")
    if moved_folders:
        print(f"\n{Fore.GREEN}============================== MOVED FOLDERS =============================={Style.RESET_ALL}")
        print("\n".join(moved_folders))
    if renamed_files:
        print(f"\n{Fore.CYAN}============================== RENAMED FILES =============================={Style.RESET_ALL}")
        print("\n".join(renamed_files))
    if skipped_folders:
        print(f"\n{Fore.YELLOW}============================== SKIPPED FILES =============================={Style.RESET_ALL}")
        print("\n".join(skipped_folders))
    
if __name__ == "__main__":
    print(f"{Fore.WHITE}{Style.BRIGHT}{Back.YELLOW}Rename and Sorting Tool{Style.RESET_ALL}\n")
    base_directory = os.getcwd()
    process_folders(base_directory)

# Fancy closing message
print("\n\n\n\n")
print(f"{Fore.CYAN}This window will stay open until you press Enter{Style.RESET_ALL}")
input(f"{Fore.YELLOW}Press Enter to close...{Style.RESET_ALL}")
