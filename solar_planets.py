import cv2 # biblioteca OpenCV

# Carrega a imagem original do sistema solar
img = cv2.imread('solar-system.jpg')

# Sol
cv2.putText(img,
            'Sol',
            (40, 80),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (0, 255, 255)
            ) # Código BGR
# Mercúrio
cv2.putText(img,
            'Mercurio',
            (35, 200),
            cv2.FONT_HERSHEY_DUPLEX,
            0.4,
            (255, 0, 0)
            )
# Vênus
cv2.putText(img,
            'Venus',
            (75, 140),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (220, 245, 245)
            )
# Terra
cv2.putText(img,
            'Terra',
            (130, 200),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (0, 255, 0)
            )
# Marte
cv2.putText(img,
            'Marte',
            (170, 150),
            cv2.FONT_HERSHEY_DUPLEX,
            0.4,
            (0, 0, 255)
            )
# Júpiter
cv2.putText(img,
            'Jupiter',
            (210, 260),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (0, 0, 255)
            )
# Saturno
cv2.putText(img,
            'Saturno',
            (310, 100),
            cv2.FONT_HERSHEY_DUPLEX,
            0.9,
            (0, 165, 255)
            )
# Urano
cv2.putText(img,
            'Urano',
            (445, 125),
            cv2.FONT_HERSHEY_DUPLEX,
            0.7,
            (255, 255, 0)
            )
# Netuno
cv2.putText(img,
            'Netuno',
            (515, 220),
            cv2.FONT_HERSHEY_DUPLEX,
            0.7,
            (255, 255, 0)
            )

# Exibe a imagem e mantém a janela aberta
cv2.imshow('resultado', img)
cv2.waitKey(0)

# Salva a imagem editada como arquivo JPEG
new_img = cv2.imwrite('Solar_systemwithname.jpg', img)
print(new_img)