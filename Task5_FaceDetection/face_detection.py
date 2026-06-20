import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read image
image = cv2.imread("sample_face.jpg")

if image is None:
    print("Error: sample_face.jpg not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=8,
    minSize=(80, 80)
)

# Remove very small detections
filtered_faces = []

for (x, y, w, h) in faces:
    area = w * h

    if area > 8000:
        filtered_faces.append((x, y, w, h))

print(f"\nNumber of faces detected: {len(filtered_faces)}")

# Draw rectangles
for i, (x, y, w, h) in enumerate(filtered_faces):

    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )

    cv2.putText(
        image,
        f"Person {i+1}",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

# Save output
cv2.imwrite("output_face.jpg", image)

print("Output saved as output_face.jpg")

# Display image
cv2.imshow("Face Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()