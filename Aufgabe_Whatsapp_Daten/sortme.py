import re
from datetime import datetime
from pathlib import Path
from glob import glob
from typing import Sequence

def get_files_recursive(path: Path, file_ext:Sequence[str] = ["jpg", "jpeg", "mp4", "png", "gif"]) -> list[Path]:
	"""Get all files recursively in a directory with a specific file extension"""
	files = [file for ext in file_ext for file in path.glob(f'**/*.{ext}')]
	return files

# Main code
if __name__ == "__main__":
	# Path configuration
	path_unsorted = Path("./Aufgabe_Whatsapp_Daten/whatsapp-data/unsorted")
	path_sorted = Path("./Aufgabe_Whatsapp_Daten/whatsapp-data/sorted")

	# Get all files in the unsorted directory
	files = get_files_recursive(path_unsorted)

	# Move files to the sorted directory
	for file in files:
		# Extract creation date from the file name
		name = file.name
		date_str = re.search(r"-(\d{8})-", name)
		if date_str:
			date_str = date_str.group(1)
			date = datetime.strptime(date_str, "%Y%m%d")

			print(date.year, date.month)
		
		# Create the directory if it does not exist
