#!/usr/bin/env python3

import shutil
import subprocess
import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Generate video from frames in a directory"
    )
    parser.add_argument("output", help="Output video filename")
    parser.add_argument(
        "--input-folder",
        default="ignore_render",
        help="Input folder containing PNG frames (default: ignore_render)",
    )
    parser.add_argument(
        "--reverse", action="store_true", help="Reverse the frame order (descending)"
    )
    parser.add_argument(
        "--fps", type=int, default=30, help="Frames per second (default: 30)"
    )

    args = parser.parse_args()

    # Check if input directory exists
    input_dir = Path(args.input_folder)
    if not input_dir.is_dir():
        print(f"Error: {input_dir} directory not found!")
        sys.exit(1)

    # Get original directory
    original_dir = Path.cwd()

    # Create temporary directory
    temp_dir = input_dir / "temp_frames"

    try:
        print(
            f"Creating video from frames in {'descending' if args.reverse else 'ascending'} order..."
        )

        temp_dir.mkdir(exist_ok=True)

        # Get all PNG files and sort them numerically
        png_files = list(input_dir.glob("*.png"))
        if not png_files:
            print("Error: No PNG files found in directory!")
            sys.exit(1)

        # Sort by numeric value in filename
        png_files.sort(key=lambda x: int(x.stem), reverse=args.reverse)

        # Copy files to temp directory with sequential names
        for i, png_file in enumerate(png_files):
            dst = temp_dir / f"frame_{i:04d}.png"
            shutil.copy2(png_file, dst)

        print(f"Total files processed: {len(png_files)}")
        print(f"Frame order: {png_files[0].name} -> {png_files[-1].name}")

        # Generate video using ffmpeg
        print("Generating video...")
        output_path = original_dir / args.output

        cmd = [
            "ffmpeg",
            "-y",
            "-r",
            str(args.fps),
            "-i",
            str(temp_dir / "frame_%04d.png"),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-vf",
            "scale=trunc(iw/2)*2:trunc(ih/2)*2",
            str(output_path),
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error running ffmpeg: {result.stderr}")
            sys.exit(1)

        # Check if video was created successfully
        if output_path.exists():
            print(f"Video created successfully: {output_path}")
            file_size = output_path.stat().st_size
            print(f"File size: {file_size / (1024 * 1024):.1f} MB")
        else:
            print("Error: Failed to create video")
            sys.exit(1)

    finally:
        # Clean up temp directory if it exists
        if temp_dir.exists():
            shutil.rmtree(temp_dir)


if __name__ == "__main__":
    main()
