import cv2
import numpy as np

# Læs billedet ind
image_path = 'C:\\Users\\josep\\PycharmProjects\\BBMiniProject\\King Domino dataset\\Cropped and perspective corrected boards\\1.jpg'
image = cv2.imread(image_path)

# Tjek om billedet blev indlæst korrekt
if image is None:
    print(f"Fejl: Kunne ikke åbne billedet. Tjek filstien: {image_path}")
else:
    # Tjek billedets størrelse (for at sikre det er 500x500 pixels)
    height, width, channels = image.shape
    print(f"Billedets størrelse: {width}x{height} pixels")

    if height == 500 and width == 500:
        # Slicer billedet op i 100x100 dele (5x5 felter)
        tile_size = 100
        margin = 10  # Margen mellem tiles
        num_tiles = height // tile_size  # Antal tiles i hver retning

        # Opretter et større billede til at rumme tiles med margin
        combined_height = num_tiles * tile_size + (num_tiles - 1) * margin
        combined_width = num_tiles * tile_size + (num_tiles - 1) * margin
        combined_image = np.zeros((combined_height, combined_width, channels), dtype=np.uint8)

        for row in range(num_tiles):
            for col in range(num_tiles):
                # Skær en tile (100x100 pixels) fra billedet
                tile = image[row * tile_size:(row + 1) * tile_size, col * tile_size:(col + 1) * tile_size]

                # Beregn positionen i det kombinerede billede
                y_pos = row * (tile_size + margin)
                x_pos = col * (tile_size + margin)

                # Indsæt tile i det kombinerede billede
                combined_image[y_pos:y_pos + tile_size, x_pos:x_pos + tile_size] = tile

        # Vis den kombinerede billede med alle tiles
        cv2.imshow("Combined Tiles", combined_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print(f"Antal tiles skåret ud: {num_tiles * num_tiles}")  # Udskriv det samlede antal tiles
    else:
        print(f"Billedet har ikke den forventede størrelse. Det er {height}x{width} pixels, ikke 500x500.")
