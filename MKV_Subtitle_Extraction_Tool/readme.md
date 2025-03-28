# Subtitle Extraction Tool

## Overview
This script extracts subtitle tracks from `.mkv` video files using `mkvmerge` and `mkvextract` (part of MKVToolNix). It scans through a directory and processes all `.mkv` files, extracting subtitles into separate files.

## Features
- Automatically detects and extracts subtitle tracks
- Skips directories starting with `_`
- Skips already extracted subtitles to avoid duplication
- Supports progress indication with `tqdm`
- Uses `colorama` for colored output

## Prerequisites
- Install [MKVToolNix](https://mkvtoolnix.download/) (required for `mkvmerge` and `mkvextract`)
- Python 3.x

## Installation
1. Clone or download this repository:
   ```sh
   git clone https://github.com/your-repo/subtitle-extractor.git
   cd subtitle-extractor
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script in the directory containing your `.mkv` files:
```sh
python script.py
```

The script will process all `.mkv` files in the current directory and its subdirectories, extracting subtitle tracks.

## Example Output
```
Processing: example.mkv
Extracting subtitle track 1 to 1-example.track.srt
Extracting subtitle track 2 to 2-example.track.sup
Subtitle extraction completed!
```

## Notes
- Subtitle files are named using the format: `X-filename.track.ext` where `X` is the track number, and `ext` is `srt` or `sup`.
- If no subtitle tracks are found, the script will notify you and skip the file.
- The script will prompt you to press Enter before closing.

## License
This project is open-source and available under the MIT License.

---
Happy extracting! 🎥

