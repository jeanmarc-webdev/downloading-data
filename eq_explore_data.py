from pathlib import Path
import json
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Check if the eq_data directory exists and list its contents
eq_data_dir = Path('eq_data')
if eq_data_dir.exists() and eq_data_dir.is_dir():
    print("Contents of eq_data directory:", list(eq_data_dir.iterdir()))
else:
    print(f"Directory not found: {eq_data_dir}")

# Use the correct filename that exists in the directory
path = eq_data_dir / 'eq_data_1_day_m1.geojson'

# Check if the file exists
if path.exists():
    # Specify the encoding when reading the file
    contents = path.read_text(encoding='utf-8')
    all_eq_data = json.loads(contents)
    # Create a more readable version of the data file.
    readable_path = eq_data_dir / 'readable_eq_data.geojson'
    readable_contents = json.dumps(all_eq_data, indent=4)
    readable_path.write_text(readable_contents, encoding='utf-8')
    print("File processed successfully.")
else:
    print(f"File not found: {path}")

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties'] ['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
