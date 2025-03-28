import os
import subprocess
import re
from colorama import Fore, Style, init
from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

def extract_subtitles(root_dir):
    # Walk through all directories and files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip folders and their subdirectories that start with "_"
        dirnames[:] = [d for d in dirnames if not d.startswith('_')]
        
        for filename in filenames:
            if filename.endswith(".mkv"):
                mkv_file = os.path.join(dirpath, filename)
                print(f"{Fore.CYAN}Processing: {Fore.YELLOW}{mkv_file}{Style.RESET_ALL}")
                
                # Get subtitle track IDs and formats
                result = subprocess.run(["mkvmerge", "-i", mkv_file], capture_output=True, text=True)
                tracks = []
                
                for line in result.stdout.split('\n'):
                    match = re.search(r'Spur ID (\d+): (subtitles) \(([^)]+)\)', line, re.IGNORECASE)
                    if match:
                        track_id = match.group(1)
                        subtitle_format = match.group(3).lower()
                        ext = "srt" if "subrip" in subtitle_format else "sup"  # Default to .sup if not SRT
                        tracks.append((track_id, ext))
                
                if not tracks:
                    print(f"{Fore.RED}No subtitle tracks found in: {Fore.YELLOW}{mkv_file}{Style.RESET_ALL}")
                    continue
                
                # Counter is now outside the extraction loop
                counter = 1  # Start counter for each file
                for track, ext in tracks:
                    output_file = os.path.join(dirpath, f"{counter}-{os.path.splitext(filename)[0]}.track.{ext}")
                    
                    # Skip extraction if file already exists
                    if os.path.exists(output_file):
                        print(f"{Fore.MAGENTA}Subtitle track {counter} already exists, skipping...{Style.RESET_ALL}")
                    else:
                        print(f"\n{Fore.GREEN}Extracting subtitle track {track} to {output_file}{Style.RESET_ALL}")
                        # Show progress bar for extraction
                        with tqdm(total=100, desc=f"Extracting track {track}", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed} < {remaining}]") as pbar:
                            subprocess.run(["mkvextract", "tracks", mkv_file, f"{track}:{output_file}"])
                            pbar.update(100)  # Simulate completion of extraction
                    
                    # Increment the counter for the next subtitle track
                    counter += 1

if __name__ == "__main__":
    print(f"{Fore.YELLOW}{Style.BRIGHT}MKV Subtitle Extraction Tool{Style.RESET_ALL}\n")
    extract_subtitles(".")
    print(f"\n{Fore.GREEN}Subtitle extraction completed!{Style.RESET_ALL}")

# Fancy closing message
print("\n\n\n\n")
print(f"{Fore.CYAN}This window will stay open until you press Enter{Style.RESET_ALL}")
input(f"{Fore.YELLOW}Press Enter to close...{Style.RESET_ALL}")
