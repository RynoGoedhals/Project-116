import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Mercury",
    (120, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.3,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Sun",
    (20, 300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Venus",
    (200, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Earth",
    (275, 180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Mars",
    (400, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Jupiter",
    (600, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Saturn",
    (775, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Uranus",
    (975, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0, 0, 0)
)

cv2.putText(
    img,
    "Neptune",
    (1100, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.imshow("output", img)

cv2.waitKey(0)