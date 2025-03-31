import cv2 

image = cv2.imread("example.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

    
    print(f'DLA KOLORU: ')
    h, w, c = image.shape

    print(f'width: {w} pixels')
    print(f'height: {h} pixels')
    print(f'channels: {c}')

    cv2.namedWindow("Wyswietlony obraz", cv2.WINDOW_NORMAL)
    cv2.imshow("Wyswietlony obraz", image)  

    print('\n')

    image_gray = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)
    print(f'DLA SZAREGO: ')
    h1, w1 = image_gray.shape

    print(f'width: {w1} pixels')
    print(f'height: {h1} pixels')
    print(f'channels: 1')

    cv2.imwrite("example_gray.jpg", image_gray)
    print(f'Obraz w szarosciach zapisano')

    cv2.namedWindow("Obraz w skali szarosci", cv2.WINDOW_NORMAL)
    cv2.imshow("Obraz w skali szarosci", image_gray)

    cv2.waitKey()
    cv2.destroyAllWindows()
