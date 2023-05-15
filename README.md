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

3. Open the `timelapse_maker.py` file in your preferred text editor.

4. Modify the script to adjust the settings according to your requirements:

   - `num_hours`: Set the number of hours to capture screenshots (default is 2).
   - `fps`: Set the frames per second for the timelapse video (default is 15).

5. Save the changes.

6. Run the script using the following command:

   ```
   python timelapse_maker.py
   ```

7. The script will capture screenshots for the specified duration and save them in a directory with a timestamp.

8. After capturing the screenshots, the script will create a timelapse video by stitching the images together.

9. Once the video is created, it will be saved in the project directory with a timestamp.

## Notes

- The screenshots will be captured at one-second intervals by default. You can modify the interval by adjusting the `time.sleep()` function in the `capture_screenshots()` function.

- The timelapse video will be saved in the MP4 format with the specified frames per second (FPS).

- Make sure to have a sufficient amount of disk space as capturing screenshots and creating the video may require significant storage depending on the duration and frequency of screenshots.

- The script uses the current timestamp to generate unique directory and file names for each run, ensuring that previous results are not overwritten.

- Feel free to modify the code to suit your specific needs.

## License

This project is licensed under the [MIT License](LICENSE).