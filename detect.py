import cv2
from ultralytics import YOLO

# Load the YOLOv8-Pose model
model = YOLO("C:/Users/omerf/Desktop/STAJ/pose_detection/runs/segment/yolov8_custom_seg/weights/best.pt")  # You can change to a larger model if needed, e.g., yolov8m-pose.pt, yolov8l-pose.pt

# Load an image
image_path = "C:/Users/omerf/Desktop/sunum/apple_detect/images.jpg"
image = cv2.imread(image_path)

# Perform inference
results = model(image)

# Visualize results
annotated_frame = results[0].plot()

# Display the output
cv2.imshow("YOLOv8 Segmantion", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally, save the output
output_path = "path_to_save_output.jpg"
cv2.imwrite(output_path, annotated_frame)