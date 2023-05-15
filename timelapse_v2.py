import os
import time
import imageio
import numpy as np
from PIL import Image
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionOnScreenOnly, kCGWindowImageDefault, CGWindowListCreateImage, CGRectNull

# Directory to save screenshots
SAVE_DIR = './screenshots'

# Number of screenshots to capture
NUM_SCREENSHOTS = 60

# Time interval between screenshots (in seconds)
INTERVAL = 1

# Width and height of the screen
SCREEN_WIDTH = CGWindowListCreateImage(CGRectNull, kCGWindowListOptionOnScreenOnly, kCGNullWindowID, kCGWindowImageDefault).size[0]
SCREEN_HEIGHT = CGWindowListCreateImage(CGRectNull, kCGWindowListOptionOnScreenOnly, kCGNullWindowID, kCGWindowImageDefault).size[1]

def capture_screenshot():
    """Captures a screenshot of the main display and returns a PIL Image object."""
    screenshot = CGWindowListCreateImage(
        CGRectNull,
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID,
        kCGWindowImageDefault
    )
    width, height = screenshot.size
    data = screenshot.tobytes()
    return Image.frombytes('RGB', (width, height), data, 'raw', 'RGBX', 0, 1)

if __name__ == '__main__':
    # Create directory to save screenshots if it doesn't exist
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    # Capture screenshots
    for i in range(NUM_SCREENSHOTS):
        # Capture screenshot
        image = capture_screenshot()

        # Save screenshot to file
        filename = f'{SAVE_DIR}/screenshot_{i:04d}.png'
        image.save(filename)

        # Wait for the specified interval before capturing the next screenshot
        time.sleep(INTERVAL)

    # Load screenshots and create timelapse video
    images = []
    for i in range(NUM_SCREENSHOTS):
        filename = f'{SAVE_DIR}/screenshot_{i:04d}.png'
        images.append(np.array(Image.open(filename)))

    # Save timelapse video to file
    video_filename = 'timelapse.mp4'
    imageio.mimsave(video_filename, images, fps=30)

    print(f'Timelapse video saved to {video_filename}.')
