import os

# Define website directory
website_dir = "terraform_static_site/website"
assets_dir = os.path.join(website_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)

# HTML content
index_html = """<!DOCTYPE html>
<html>
<head>
    <title>My Static Website</title>
    <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
    <h1>Welcome to My Static Website!</h1>
    <p>This website is hosted on <strong>Amazon S3</strong> and served via <strong>CloudFront</strong>.</p>
    <script src="assets/app.js"></script>
</body>
</html>
"""

error_html = """<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Oops! Looks like the page you're looking for doesn't exist.</p>
</body>
</html>
"""

# CSS content
styles_css = """body {
    font-family: Arial, sans-serif;
    margin: 40px;
    background-color: #f4f4f4;
    color: #333;
}
h1 {
    color: #007acc;
}
"""

# JavaScript content
app_js = """console.log("Website loaded successfully!");"""

# Write files
with open(os.path.join(website_dir, "index.html"), "w") as f:
    f.write(index_html)

with open(os.path.join(website_dir, "error.html"), "w") as f:
    f.write(error_html)

with open(os.path.join(assets_dir, "styles.css"), "w") as f:
    f.write(styles_css)

with open(os.path.join(assets_dir, "app.js"), "w") as f:
    f.write(app_js)

# List the created files
created_files = []
for root, dirs, files in os.walk(website_dir):
    for name in files:
        created_files.append(os.path.relpath(os.path.join(root, name), "terraform_static_site"))

import pandas as pd
df = pd.DataFrame(created_files, columns=["Website Files"])
import ace_tools as tools; tools.display_dataframe_to_user(name="Static Website Files", dataframe=df)

