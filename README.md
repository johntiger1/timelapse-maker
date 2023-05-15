# Timelapse Maker

This is a Python code snippet that captures screenshots at regular intervals and then stitches them together to create a timelapse video. It uses the `pyautogui` library for capturing screenshots and the `cv2` library for video processing.

## Requirements

- Python 3.x
- `pyautogui` library
- `cv2` library

## Usage

1. Clone the repository and navigate to the project directory.

2. Install the required dependencies using the following command:
   ```
   pip install pyautogui opencv-python
   ```

3. The script accepts the following command-line arguments:
   - `--num_hours`: Number of hours to capture screenshots (default is 2).
   - `--fps`: Frames per second for the timelapse video (default is 15).

4. Run the script using the following command:
   ```
   python timelapse_maker.py --num_hours <hours> --fps <fps>
   ```
   Replace `<hours>` with the desired number of hours for capturing screenshots, and `<fps>` with the desired frame rate for the timelapse video.

5. The script will capture screenshots for the specified duration and save them in a directory with a timestamp.

6. After capturing the screenshots, the script will create a timelapse video by stitching the images together.

7. Once the video is created, it will be saved in the project directory with a timestamp.

## Notes

- The screenshots will be captured at one-second intervals by default. You can modify the interval by adjusting the `time.sleep()` function in the `capture_screenshots()` function.

- The timelapse video will be saved in the MP4 format with the specified frames per second (FPS).

- Make sure to have a sufficient amount of disk space as capturing screenshots and creating the video may require significant storage depending on the duration and frequency of screenshots.

- The script uses the current timestamp to generate unique directory and file names for each run, ensuring that previous results are not overwritten.

- Feel free to modify the code to suit your specific needs.

## License

This project is licensed under the [MIT License](LICENSE).
