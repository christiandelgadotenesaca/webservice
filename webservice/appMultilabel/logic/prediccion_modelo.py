from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from sklearn.preprocessing import MultiLabelBinarizer
import tensorflow as tf

class PrediccionModelo():

    def __init__(self):
        pass

    #Funcion para cargar red neuronal
    def cargarModelo(self,nombreArchivo):
        try:
            print("TensorFlow version:", tf.__version__)
            # Cargar el modelo previamente guardado
            #loaded_model = load_model(nombreArchivo + ".h5")
            loaded_model = load_model(nombreArchivo + ".keras")
            print("Red Neuronal Cargada desde Archivo")
            return loaded_model
        except ImportError as ie:
            print(f"ImportError al cargar el modelo: {ie}")
            return None
        except IOError as ioe:
            print(f"IOError al cargar el modelo: {ioe}")
            return None
        except Exception as e:
            print(f"Error al cargar el modelo: {e}")
            return None

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
        labels = ['arbol', 'banca'], ['arbol', 'automovil'], ['automovil', 'persona'], ['persona', 'banca']
        return labels


    def predecirImagen(self, nueva_imagen_path):
        print('Entro a predecirImagen')
        labels = self.cargarLabels()
        # Codificación de etiquetas usando MultiLabelBinarizer
        mlb = MultiLabelBinarizer()
        mlb.fit_transform(labels)

        # Cargar la nueva imagen
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

    def predecirConImagen(self, nueva_imagen):
        try:
            print('Entro a predecirImagen')
            labels = self.cargarLabels()
            # Codificación de etiquetas usando MultiLabelBinarizer
            mlb = MultiLabelBinarizer()
            mlb.fit_transform(labels)

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
        except Exception as e:
            print(f"Error predecir con Imagen: {e}")
            return None
