import cv2
from ultralytics import YOLO


def process_video(video_path, output_path, model):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection
        results = model(frame)

        # Process results (e.g., draw bounding boxes, track objects)
        for result in results.xyxy[0]:  # assuming the first frame of results
            x1, y1, x2, y2, conf, cls = result
            label = model.names[int(cls)]
            # Draw bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            cv2.putText(
                frame,
                label,
                (int(x1), int(y1) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 0, 0),
                2,
            )

        # Write the frame with detected objects
        out.write(frame)

    cap.release()
    out.release()


# Load the trained model
model = YOLO("models/best.pt")

# Process a new video
process_video("videos/input/video1.mp4", "videos/output/video1_output.mp4", model)
