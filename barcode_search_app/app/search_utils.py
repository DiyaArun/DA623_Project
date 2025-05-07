def search_products(df, query, top_k=5):
    query = query.lower()
    scores = []

    for _, row in df.iterrows():
        content = f"{row['product_name']} {row.get('brands', '')} {row.get('ingredients_text', '')}".lower()
        if query in content:
            scores.append((row['code'], row['product_name'], row.get('ingredients_text', '')))

    return scores[:top_k]
