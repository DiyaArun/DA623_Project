# 🧾 Barcode Recognition & Smart Food Search

This project combines **barcode decoding**, **product lookup**, and **semantic product search** using the [Open Food Facts](https://world.openfoodfacts.org/) dataset. Users can upload barcode images to retrieve nutritional info, or enter natural language queries to find matching food products. The system is built with `pyzbar`, `sentence-transformers`, and `FastAPI`.

---

## 📦 Features

- 📸 **Barcode Detection**: Upload a barcode image (PNG), decode it, and get product details.
- 🔍 **Semantic Search**: Use smart queries like “low sugar cereal” to find relevant foods.
- 💡 **Nutrition Info**: See carbohydrates, fat, protein, fiber, and sugar per 100g.
- 🌐 **Web Interface**: FastAPI-based web app with upload and search on one page.

---

## 🛠 Tech Stack

- `Python`, `Pandas`, `OpenCV`, `pyzbar`, `python-barcode`
- `sentence-transformers` for semantic embeddings
- `FastAPI` for backend
- `HTML + Jinja2` for frontend (`ipywidgets` in Jupyter)

---

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

3. **Open the app**:
   Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📁 Dataset

We use a subset of `en.openfoodfacts.org.products.tsv` with selected columns:
- `code`, `product_name`, `brands`, `ingredients_text`
- Nutrition per 100g: `carbohydrates`, `fat`, `fiber`, `proteins`, `salt`, `sugars`

---

## 📸 Sample Barcode

To test barcode decoding:
- Use generated EAN-13 barcodes for sample product codes.
- Or upload real product barcodes as `.png` files.

---

## 📚 Example Query

Try:  
- `"high protein snack"`  
- `"low sugar chocolate"`  
- `"gluten free bread"`

---

## 📜 License

Open source for educational use — based on Open Food Facts (ODBL).
