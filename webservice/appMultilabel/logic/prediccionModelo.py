from PIL import Image
import numpy as np
import tensorflow as tf
from PIL import Image
from sklearn.preprocessing import MultiLabelBinarizer
from appMultilabel.logic import prediccionModelo

class prediccionModelo():
    #Funcion para cargar red neuronal
    def cargarModelo(self,nombreArchivo):
        # Cargar el modelo previamente guardado
        loaded_model = tf.keras.models.load_model(nombreArchivo+".h5")
        print("Red Neuronal Cargada desde Archivo") 
        return loaded_model

    def cargarLabels(self):
        # Directorio principal que contiene subcarpetas
        #dataset_dir = 'imagenesMultilabel/imagenesEntrenamiento'
        # Listas para almacenar etiquetas
        #labels = []
        # Recorrer cada carpeta en el directorio principal
        #for folder in os.listdir(dataset_dir):
        #    folder_path = os.path.join(dataset_dir, folder)

            # Ignorar archivos que no son carpetas
        #    if not os.path.isdir(folder_path):
        #        continue

        #    folder_labels = folder.split(', ')
        #    print(f"folder_labels:", folder_labels)

        #    labels.append(folder_labels)
        labels = ['arbol', 'banca'], ['arbol', 'letrero'], ['automovil', 'persona'], ['patos', 'arbol'], ['patos','estanque'], ['perro', 'pelota'], ['persona', 'bicicleta'], ['persona', 'pelota']
        return labels


    def predecirImagen(self):
        labels = self.cargarLabels()
        # Codificación de etiquetas usando MultiLabelBinarizer
        mlb = MultiLabelBinarizer()
        mlb.fit_transform(labels)

        # Cargar la nueva imagen
        nueva_imagen_path = "imagenesMultilabel/imagenes_Nuevas/test001.jpg"  # Reemplaza con la ruta de tu imagen
        nueva_imagen = Image.open(nueva_imagen_path)

        # Ajustar el tamaño de la imagen según el tamaño que utilizaste durante el entrenamiento
        imagen_width, imagen_height = 128, 128
        nueva_imagen = nueva_imagen.resize((imagen_width, imagen_height))

        # Convertir la imagen a un array de NumPy y normalizar
        nueva_imagen_array = np.array(nueva_imagen) / 255.0

        # Expandir las dimensiones para que coincidan con la forma de entrada del modelo
        nueva_imagen_array = np.expand_dims(nueva_imagen_array, axis=0)

        loaded_model = self.cargarModelo('resources/modeloMultilabel')

        # Realizar la predicción con el modelo cargado
        prediccion_nueva_imagen = loaded_model.predict(nueva_imagen_array)

        # Obtener las etiquetas correspondientes a las predicciones
        etiquetas_predichas = mlb.inverse_transform(prediccion_nueva_imagen.round())

        # Visualizar la predicción y las etiquetas
        print("Categorias predichas:", prediccion_nueva_imagen.round())
        print("Etiquetas predichas:", etiquetas_predichas)
        return etiquetas_predichas

