import os
import cv2

# Define the path and frame numbers to skip
path = '/data/teja/output_bw_render_paper'
numbers_to_skip = set([
    5, 16, 27, 38, 49, 56, 61, 72, 83, 94, 105, 116, 127, 138, 149, 160,
    167, 172, 183, 194, 205, 216, 227, 238, 249, 260, 271, 278, 283, 294,
    305, 316, 327, 338, 349, 356, 361, 372, 383, 394, 405, 416, 427, 438,
    449, 460, 467, 472, 483, 494, 505, 516, 527, 538, 549, 560, 571, 578,
    583, 594, 605, 616, 627, 638, 649, 660, 671, 682, 689, 694, 705,
    727, 738, 749, 755, 761, 772, 783, 794, 801, 806, 817, 828, 839, 850,
    861, 872, 883, 894, 905, 912, 917, 928, 939, 950, 961, 972, 983,
    994, 1005, 1016, 1023, 1028, 1039, 1050, 1061, 1072, 1083, 1094, 1105,
    1117, 1127, 1134, 1139, 1150, 1161, 1172, 1183, 1194, 1205, 1216, 1227,
    1238, 1245, 1250, 1261, 1272, 1283, 1294
])


from tqdm import tqdm

# Create videos for each folder
# for subfolder in os.listdir(path):
for subfolder in tqdm(os.listdir(path)):
    subfolder_path = os.path.join(path, subfolder, "images")
    
    if not os.path.exists(subfolder_path) or not os.path.isdir(subfolder_path):
        continue
    
    # Collect all frame filenames
    frames = sorted([f for f in os.listdir(subfolder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])
    
    if not frames:
        continue
    
    # Define video output path
    output_video_path = os.path.join( f"{subfolder}.mp4")
    
    # Get frame size
    first_frame_path = os.path.join(subfolder_path, frames[0])
    frame = cv2.imread(first_frame_path)
    height, width, _ = frame.shape

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))
    
    # Process frames and write to video
    for frame_filename in frames:
        frame_number = int(os.path.splitext(frame_filename)[0])  # Assuming filename is a number
        if frame_number in numbers_to_skip:
            continue
        
        frame_path = os.path.join(subfolder_path, frame_filename)
        frame = cv2.imread(frame_path)
        video_writer.write(frame)
    
    video_writer.release()
    print(f"Video created: {output_video_path}")
