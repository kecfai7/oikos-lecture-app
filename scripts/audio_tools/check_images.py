import os
import cv2
import glob

output_dir = r"c:\Oikos Univ\files_analysis"
jpgs = sorted(glob.glob(os.path.join(output_dir, "*.jpg")))
print(f"Total JPG frames saved: {len(jpgs)}")
if jpgs:
    img = cv2.imread(jpgs[0])
    print(f"Sample image shape: {img.shape}")
