import cv2

# Open video
cap = cv2.VideoCapture("/Users/shyamalkar/Desktop/Python_project/OpenCVPracticals-Shyamal/13062.mp4")

# Video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create output video
out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Convert video to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert back to BGR for video writing
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    cv2.imshow("Video", gray)

    out.write(gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()