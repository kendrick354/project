import os
import sys
import pymongo.server_api
import config
import pymongo
import pandas as pd
import gridfs


mongo_uri = "mongodb+srv://admin:ZmQvsr76Dkk3oyPU@cluster0.92giasc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# connects to the connection_url
myclient = pymongo.MongoClient(mongo_uri, server_api=pymongo.server_api.ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    myclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# create a database
db = myclient["patient_data"]


fs = gridfs.GridFS(db)


def load_csv_to_mongodb(csv_file, collection_name):
    """
    Reads a csv file and creates a collection for it.
    """
    try:
        df = pd.read_csv(csv_file)
        print(df.info())

        data = df.to_dict(orient="records")

        collection = db[collection_name]

        result = collection.insert_many(data)
        print(len(result.inserted_ids))
    except FileNotFoundError:
        print("Error: The file wasn't found")
    except pd.errors.EmptyDataError:
        print("The file is empty or cannot be read")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def load_images_to_mongodb(image_folder):
    """
    Loads gets all images & uploads them to mongodb
    """
    if not os.path.exists(image_folder):
        print(f"Error: The folder {image_folder} does not exist.")
        return

    if not os.path.isdir(image_folder):
        print(f"Error: {image_folder} is not a directory.")
        return

    files = os.listdir(image_folder)
    if not files:
        print(f"The folder {image_folder} is empty.")
        return
    for image_name in os.listdir(image_folder):
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder,image_name)

            # Open the image file and store it in GridFS 
            # rb = read binary "images != text"
            with open(image_path, 'rb') as image_file:
                fs.put(image_file, filename=image_name)
            print(f"Uploaded image: {image_name}")


back_end_dir = r'C:\Users\ashpr\OneDrive\Documents\WebDevelopment\dot_plot\back-end'
database_dir = os.path.join(back_end_dir, 'database')

patient_path = os.path.join(database_dir, 'Patients.csv')
scan_path    = os.path.join(database_dir, 'US_scans.csv')
folder_path = os.path.join(database_dir, 'US_scans')

load_csv_to_mongodb(patient_path, 'patients')
load_csv_to_mongodb(scan_path, 'US_scans')

load_images_to_mongodb(folder_path)

myclient.close()

print("CSV data and images have been successfully loaded into MongoDB.")
