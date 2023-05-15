import os
import time
from Quartz import (
    CGWindowListCreateImage,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID,
    CGContextRef,
    CGImageDestinationCreateWithURL,
    kUTTypeJPEG,
    CGImageDestinationAddImage,
    CGImageDestinationFinalize,
    CGMainDisplayID,
    CGImageGetWidth,
    CGImageGetHeight,
    CGImageGetBitsPerPixel,
    CGDataProviderCopyData,
    CFDataGetBytes,
)
from PIL import Image
print('imported')