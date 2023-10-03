import cv2

# Carregue a imagem principal (imagem maior)
imagem_principal = cv2.imread('Topico4\imgs\Mountain 4K.jpg')

# Carregue a marca d'água (imagem menor)
marca_dagua = cv2.imread('Topico4\imgs\marcadagua.png', cv2.IMREAD_UNCHANGED)

# Obtenha as dimensões da imagem da marca d'água
altura_marca_dagua, largura_marca_dagua, _ = marca_dagua.shape

# Defina a posição onde você deseja inserir a marca d'água na imagem principal
posicao_x = 50
posicao_y = 50

# Extraia o canal alfa (transparência) da marca d'água
canal_alpha = marca_dagua[:, :, 3] / 255.0

# Copie a região da imagem principal onde a marca d'água será inserida
regiao_insercao = imagem_principal[posicao_y:posicao_y+altura_marca_dagua, posicao_x:posicao_x+largura_marca_dagua]

# Aplique a marca d'água à região de inserção usando o canal alfa
for c in range(0, 3):
    regiao_insercao[:, :, c] = regiao_insercao[:, :, c] * (1 - canal_alpha) + marca_dagua[:, :, c] * canal_alpha

# Atualize a região de inserção na imagem principal
imagem_principal[posicao_y:posicao_y+altura_marca_dagua, posicao_x:posicao_x+largura_marca_dagua] = regiao_insercao

# Salve a imagem resultante
cv2.imwrite('imagem_com_marca_dagua.jpg', imagem_principal)

# Exiba a imagem resultante
cv2.imshow('Imagem com Marca d\'Água', imagem_principal)
cv2.waitKey(0)
cv2.destroyAllWindows()