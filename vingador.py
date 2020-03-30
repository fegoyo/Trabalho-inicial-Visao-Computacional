Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> chess = cv2.imread('D:\Trabalho do PS\Images\xadrez.png', cv2.IMREAD_GRAYSCALE)
#chess = cv2.imread('Images/DIP3E_Original_Images_CH03/Fig0316(3)(third_from_top).tif', cv2.IMREAD_GRAYSCALE)
#chess = cv2.cvtColor(chess, cv2.COLOR_RGB2GRAY)
_, chess = cv2.threshold(chess, 127, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(7,7))
plt.xticks([]), plt.yticks([])
plt.imshow(chess, cmap='gray')
plt.savefig('Results/7_original.png')
plt.show()

# Imagem Original
