import os
import time
import pyautogui
import cv2

# Step 1: Capture screenshots and save them in a directory
def capture_screenshots(duration, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    start_time = time.time()
    counter = 1

    while time.time() - start_time < duration:
        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.join(output_dir, f'screenshot_{counter:04d}.png'))
        counter += 1
        time.sleep(0.1)

# Step 2: Stitch the screenshots together to form a video
def create_timelapse_video(input_dir, output_file, fps):
    images = [img for img in os.listdir(input_dir) if img.endswith(".png")]
    images.sort()

    frame = cv2.imread(os.path.join(input_dir, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(input_dir, image)))

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    # specify in hours

    duration = 3600*2  # Duration of the screen capture in seconds
    fps = 30

    # Create a new directory with a unique name for the screenshots and video
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_dir = f"screenshots_{timestamp}"
    output_file = f"timelapse_{timestamp}.mp4"

    print("Capturing screenshots...")
    capture_screenshots(duration, output_dir)

    print("Creating timelapse video...")
    create_timelapse_video(output_dir, output_file, fps)

    print("Timelapse video created!")
