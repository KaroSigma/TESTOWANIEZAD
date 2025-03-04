import cv2
# Wczytanie obrazu z pliku
image = cv2.imread("example.jpg")
cv2.imshow("Wyświetlony obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_gray = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("example_gray.jpg", image_gray)
print("Obraz zapisano jako 'example_gray.jpg'.")
(h, w, c) = image.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
