# rgbz

![nologo](path_to_your_logo_or_banner.png)

Mapping elevation data to 24-bit RGB in PNG tiles.

## Description

`rgbz` encodes elevation (z-axis) data into the RGB channels of PNG images for efficient storage and intuitive visualization.

## Features

- Encode elevation data into RGB PNG tiles.
- Decode RGB PNG to extract elevation data.
- Render elevation using color gradients.

## Installation

```bash
git clone https://github.com/your_username/rgbz.git
cd rgbz
pip install -r requirements.txt
```

## Usage

# Encode elevation data
python rgbz.py encode --input elevation_data.txt --output encoded_image.png

# Decode RGB PNG
python rgbz.py decode --input encoded_image.png --output elevation_data.txt

# Contributing
Pull requests are welcome. For major changes, open an issue first.

# References

- [Mapbox Terrain-DEM v1](https://docs.mapbox.com/data/tilesets/reference/mapbox-terrain-dem-v1/) 
is a raster digital elevation model that provides high-resolution, global elevation data encoded into RGB values within PNG tiles for Mapbox's mapping platform.

# License
[MIT](https://choosealicense.com/licenses/mit/)
