import cv2
import numpy as np
from pyzbar.pyzbar import decode
import pandas as pd
import os

# Load dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'products.tsv')
df = pd.read_csv(DATA_PATH, sep='\t', low_memory=False)
df = df[['code', 'product_name', 'brands', 'ingredients_text', 'carbohydrates_100g',
         'fat_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'sugars_100g']].dropna(subset=['code', 'product_name'])
df = df[df['code'].apply(lambda x: str(x).isdigit())]

def detect_barcode(image_bytes):
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    if img is None:
        return None
    barcodes = decode(img)
    if not barcodes:
        return None
    return barcodes[0].data.decode("utf-8")

def lookup_barcode(barcode):
    product = df[df['code'] == str(barcode)]
    return product.iloc[0].to_dict() if not product.empty else None
