#!/bin/bash

# Script to generate video from frames in ignore_render directory
# Usage: ./make_video.sh [output_filename]

# Set default output filename if not provided
OUTPUT_FILE=${1:-"reverse_animation.mp4"}

# Check if ignore_render directory exists
if [ ! -d "ignore_render" ]; then
    echo "Error: ignore_render directory not found!"
    exit 1
fi

# Change to ignore_render directory
cd ignore_render

echo "Creating video from frames in descending order..."

# Create temporary directory
mkdir -p temp_frames

# Copy and rename frames in descending order
python3 -c "
import os
import shutil

# Get all PNG files and sort them numerically in descending order
files = [f for f in os.listdir('.') if f.endswith('.png')]
files.sort(key=lambda x: int(x.split('.')[0]), reverse=False)

# Copy files to temp directory with sequential names
for i, file in enumerate(files):
    src = file
    dst = f'temp_frames/frame_{i:04d}.png'
    shutil.copy2(src, dst)

print(f'Total files processed: {len(files)}')
print(f'Frame order: {files[0]} -> {files[-1]}')
"

# Generate video using ffmpeg
echo "Generating video..."
ffmpeg -y -r 30 -i temp_frames/frame_%04d.png -c:v libx264 -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" "$OUTPUT_FILE"

# Clean up temporary files
rm -rf temp_frames

# Check if video was created successfully
if [ -f "$OUTPUT_FILE" ]; then
    echo "Video created successfully: $OUTPUT_FILE"
    ls -lh "$OUTPUT_FILE"
else
    echo "Error: Failed to create video"
    exit 1
fi