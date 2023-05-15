import os
import time
import subprocess
from PIL import Image
from moviepy.editor import ImageSequenceClip

# Set up variables for capturing screenshots
SCREENSHOT_DIR = '/path/to/screenshots'
SCREENSHOT_INTERVAL = 1  # in seconds
NUM_SCREENSHOTS = 60  # number of screenshots to capture

# Set up variables for creating time-lapse video
VIDEO_FPS = 10  # frames per second for time-lapse video
VIDEO_FILENAME = '/path/to/timelapse.mp4'

# Create directory for screenshots
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Capture screenshots
for i in range(NUM_SCREENSHOTS):
    # Capture screenshot and convert to PIL Image
    image = Image.frombuffer(
        'RGB',
        (CGDisplayPixelsWide(kCGDirectMainDisplay),
         CGDisplayPixelsHigh(kCGDirectMainDisplay)),
        CGDisplayCreateImage(kCGDirectMainDisplay),
        'raw',
        'RGBX',
        0,
        1
    )

    # Save screenshot to directory
    filename = os.path.join(
        SCREENSHOT_DIR,
        f'screenshot_{i:04d}.jpg'
    )
    image.save(filename, quality=95)

    # Wait for specified interval before capturing next screenshot
    time.sleep(SCREENSHOT_INTERVAL)

# Create time-lapse video
image_files = sorted(os.listdir(SCREENSHOT_DIR))
clip = ImageSequenceClip([os.path.join(SCREENSHOT_DIR, f) for f in image_files], fps=VIDEO_FPS)
clip.write_videofile(VIDEO_FILENAME)

# Open time-lapse video in media player
subprocess.call(['open', VIDEO_FILENAME])
