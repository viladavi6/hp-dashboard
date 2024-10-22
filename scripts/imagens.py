import cv2
import os

# Definir os caminhos das pastas de entrada e saída
# Defina as pastas
input_folder = r'C:\Users\DVILA\Downloads\hp-dashboard\characters'  # Pasta onde estão as imagens originais
output_folder = r'C:\Users\DVILA\Downloads\d'  # Pasta para salvar as imagens processadas

# Verificar se a pasta de saída existe, caso contrário, criá-la
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Percorrer todos os arquivos da pasta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  # Considerar apenas arquivos de imagem
        # Construir o caminho completo da imagem de entrada
        input_path = os.path.join(input_folder, filename)

        # Carregar a imagem
        image = cv2.imread(input_path)

        # Verificar se a imagem foi carregada corretamente
        if image is not None:
            # Aplicar o filtro bilateral para suavizar a pixelização
            smoothed_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

            # Construir o caminho completo da imagem de saída
            output_path = os.path.join(output_folder, filename)

            # Salvar a imagem resultante na pasta de saída
            cv2.imwrite(output_path, smoothed_image)

            print(f'{filename} processada e salva em {output_path}')
        else:
            print(f'Erro ao carregar {filename}')

print('Processamento concluído!')