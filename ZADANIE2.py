import cv2

image = cv2.imread("example.jpg")
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b)) #Pixel at (0, 0) - Red: 146, Green: 140, Blue: 142
(h, w) = image.shape[:2]
image[h - 1, w - 1] = (0, 0, 255)
(cX, cY) = (w // 2, h // 2)
print(f"Środek obrazu: X = {cX}, Y = {cY}") #Środek obrazu: X = 240, Y = 266
(b, g, r) = image[cY, cX]
print("Pixel srodek - Red: {}, Green: {}, Blue: {}".format(r, g, b)) #Pixel srodek - Red: 137, Green: 120, Blue: 94
startX = cX - 50
startY = cY - 50
endX = cX + 50
endY = cY + 50
image[startY:endY, startX:endX] = (0, 0, 255)
image[99, :] = (0, 255, 0) 
image[50:100, 50:100] = (255, 255, 255)

(px1_r, px1_g, px1_b) = image[50, 50]
(px2_r, px2_g, px2_b) = image[200, 200]

print(f"Pixel (50,50) - R: {px1_r}, G: {px1_g}, B: {px1_b}")
print(f"Pixel (200,200) - R: {px2_r}, G: {px2_g}, B: {px2_b}")

diff_r = abs(int(px1_r) - int(px2_r))
diff_g = abs(int(px1_g) - int(px2_g))
diff_b = abs(int(px1_b) - int(px2_b))
print(f"Roznice RGB R: {diff_r}, G: {diff_g}, B: {diff_b}") #Roznice RGB R: 201, G: 162, B: 140

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

print(f"Najjasniejszy piksel znajduje się w: {maxLoc} z jasnoscia: {maxVal}")

print("Podaj x:")
x = int(input())
print("Podaj y:")
y = int(input())
if x >= w or x < 0 or y >= h or y<0:
    print("Za duza liczba x albo y")
else:
    print("Dobrze podane")
image[y, x] = (0, 0, 0)
cv2.imshow("Changed", image)
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
image[0:cY, 0:cX] = (255, 0, 0)
cv2.imshow("Top-Left Corner", tl)
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
third_h = h // 3
third_w = w // 3
center = image[third_h:2*third_h, third_w:2*third_w]
cv2.imshow("Srodkowy fragment", center)
cv2.waitKey()
cv2.destroyAllWindows()
