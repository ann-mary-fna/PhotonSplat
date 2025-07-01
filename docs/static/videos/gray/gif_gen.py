import os

import imageio
# imageio.plugins.ffmpeg.download()

from moviepy.editor import VideoFileClip

# List all files in the current directory
files = os.listdir()

# Filter for .mp4 files
mp4_files = [file for file in files if file.endswith('.mp4')]

# Create output directory for GIFs
output_dir = "gifs"
os.makedirs(output_dir, exist_ok=True)

# Convert each .mp4 file to a .gif
for mp4_file in mp4_files:

    if not mp4_file == "enhanced_teddybear_3drecon.mp4":
        continue

    try:
        # Load the video file
        video = VideoFileClip(mp4_file).subclip(3.5, 5.1)  # First 3 seconds
        
        # Set output filename
        gif_filename = os.path.join(output_dir, os.path.splitext(mp4_file)[0] + ".gif")
        
        # Write the GIF file
        video.write_gif(gif_filename, fps=30)
        print(f"Converted {mp4_file} to {gif_filename}")
    except Exception as e:
        print(f"Failed to convert {mp4_file}: {e}")
