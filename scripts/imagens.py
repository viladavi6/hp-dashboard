import os
from rembg import remove
from PIL import Image, ImageEnhance, ImageFilter

# Defina as pastas
input_folder = r'C:\Users\DVILA\Downloads\hp-dashboard\characters'  # Pasta onde estão as imagens originais
output_folder = r'C:\Users\DVILA\Downloads\d'  # Pasta para salvar as imagens processadas

# Crie a pasta de saída se ela não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Processar cada imagem na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Verifique o formato da imagem
        img_path = os.path.join(input_folder, filename)
        
        try:
            # Abra a imagem
            with Image.open(img_path) as img:
                # Aumenta a resolução da imagem
                img = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)

                # Aplicar filtro de suavização (opcional)
                img = img.filter(ImageFilter.SMOOTH)

                # Ajustar brilho e contraste
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(1.1)  # Aumenta o brilho

                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(1.2)  # Aumenta o contraste

                # Remover o fundo
                output_image = remove(img)

                # Salve a imagem resultante
                output_path = os.path.join(output_folder, filename)
                output_image.save(output_path)

            print(f"Processado: {filename}")  # Mensagem de confirmação

        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")  # Captura e imprime erros

print("Processamento concluído! As imagens foram salvas em:", output_folder)
