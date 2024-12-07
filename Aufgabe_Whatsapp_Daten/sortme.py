import re
import shutil
from datetime import datetime
from pathlib import Path
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

		# If the date was found, create the directory
		if date_str:
			# Extract the date from the match object
			date_str = date_str.group(1)
			date = datetime.strptime(date_str, "%Y%m%d")

			# Create the directory if it does not exist
			dir_path = path_sorted / date.strftime("%Y/%Y_%m")
			dir_path.mkdir(parents=True, exist_ok=True)

			# Move the file to the sorted directory using shutil
			shutil.move(file, dir_path / file.name)
		else:
			# Create a directory in the root of the sorted directory for files without a date
			path_sorted_root = path_sorted / "no_date"
			path_sorted_root.mkdir(parents=True, exist_ok=True)
			shutil.move(file, path_sorted_root / file.name)