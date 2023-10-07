import cv2

# Load the video capture object
cap = cv2.VideoCapture(0)

# Get the first frame as the background
_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

while True:
    # Read the current frame
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the current frame and the first frame
    diff = cv2.absdiff(first_gray, gray)

    # Threshold the difference to create a binary image
    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Dilate the binary image to fill in holes
    diff = cv2.dilate(diff, None, iterations=2)

    # Find contours in the binary image
    _, cnts, _ = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for c in cnts:
        # If the contour is small, ignore it
        if cv2.contourArea(c) < 500:
            continue

        # Draw a bounding box around the contour
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Motion Detection", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
