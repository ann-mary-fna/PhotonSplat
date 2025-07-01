import cv2
import os

# Define the path where videos are stored
videos = [
    "bunchfruits_3drecon.mp4",
    "flowers_3drecon.mp4",
    "objects_3drecon.mp4",
    "teddybear_3drecon.mp4",
    "toys_3drecon.mp4",
]

# Function for contrast enhancement
def enhance_contrast(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # do it using min and max
    min_val = frame.min()
    max_val = frame.max()

    # convert to grayscale

    # Normalize the frame
    enhanced_frame = (frame - min_val) * (255 / (max_val - min_val))
    enhanced_frame = enhanced_frame.astype('uint8')

    # convert to rgb
    enhanced_frame = cv2.cvtColor(enhanced_frame, cv2.COLOR_GRAY2BGR)

    return enhanced_frame

# Process each video
for video_name in videos:
    video_path = video_name
    output_video_path = f"enhanced_{video_name}"
    
    # Open the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        continue
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    # Initialize the video writer
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    # Process frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Enhance the contrast of the frame
        enhanced_frame = enhance_contrast(frame)
        
        # Write the enhanced frame to the output video
        out.write(enhanced_frame)
    
    # Release resources
    cap.release()
    out.release()
    print(f"Enhanced video saved: {output_video_path}")
