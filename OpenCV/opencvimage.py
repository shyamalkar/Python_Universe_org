import cv2
import numpy as np

# Read image
img = cv2.imread("/Users/shyamalkar/Desktop/Python_project/OpenCVPracticals-Shyamal/12239.jpg")

# Display original image
cv2.imshow("Original", img)

# Save image
cv2.imwrite("saved_image.jpg", img)

# Resize
resize = cv2.resize(img, (500, 400))
cv2.imshow("Resized", resize)

# Flip
horizontal = cv2.flip(img, 1)
vertical = cv2.flip(img, 0)
both = cv2.flip(img, -1)

cv2.imshow("Horizontal Flip", horizontal)
cv2.imshow("Vertical Flip", vertical)
cv2.imshow("Both Flip", both)

# Draw line
line = img.copy()
cv2.line(line, (50, 50), (400, 50), (255, 0, 0), 3)

# Draw polygon
points = np.array([[100, 100], [200, 50], [300, 100], [200, 200]])
cv2.polylines(line, [points], True, (0, 255, 0), 3)

# Add text
cv2.putText(line, "OpenCV", (100, 300),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Shapes and Text", line)

# Translation using warpAffine
M = np.float32([[1, 0, 100], [0, 1, 50]])
translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Translated", translated)

# Rotation
center = (img.shape[1] // 2, img.shape[0] // 2)
M = cv2.getRotationMatrix2D(center, 45, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Rotated", rotated)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold", threshold)

# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Gaussian Blur", gaussian)

# Median Blur
median = cv2.medianBlur(img, 5)
cv2.imshow("Median Blur", median)

# Tophat
kernel = np.ones((5, 5), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Tophat", tophat)

# Blackhat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Blackhat", blackhat)

# Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Canny Edges", edges)

# Save some outputs
cv2.imwrite("resized.jpg", resize)
cv2.imwrite("rotated.jpg", rotated)
cv2.imwrite("edges.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()