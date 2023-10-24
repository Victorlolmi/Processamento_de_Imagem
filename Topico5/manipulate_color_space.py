import cv2


original_img = cv2.imread("Topico5\campo_de_flores.jpg")

gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

_,thresholded_img = cv2.threshold(gray_img.copy(), 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

mask = thresholded_img

result = cv2.bitwise_and(original_img, original_img, mask = mask)

cv2.imshow("Imagem limiarizada", result)

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()