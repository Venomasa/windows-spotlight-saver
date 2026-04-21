# windows-spotlight-saver
Save the current Windows Spotlight or desktop wallpaper to your desktop

# Save Current Spotlight Wallpaper

A small Python utility to save the current Windows wallpaper or Spotlight image to the desktop.

## What it does

- Checks the active desktop wallpaper using Windows system settings.
- If no active wallpaper is found, it falls back to the Windows Spotlight assets folder.
- Copies the image to the desktop with a usable name and extension.

## Requirements

- Python 3.6+

## Usage

Open a terminal and run:

```powershell
python save_spotlight_wallpaper.py
```

The script will copy the current wallpaper or Spotlight image to your desktop.

## Notes

- If the desktop wallpaper is already set from a normal image file, the script saves that exact file.
- If it needs to use Spotlight assets, it picks the most recent valid image from the Spotlight folder.
  
## File locations

- Output: `current_wallpaper.*` or `current_spotlight.jpg` on the desktop
