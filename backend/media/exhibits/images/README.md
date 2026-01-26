# Exhibit Images Folder

This folder is for storing exhibit images. 

## How to Use

### Method 1: Using JSON Seed Data (Recommended)

1. Place your image files (JPG, PNG, etc.) in this folder
2. In your `exhibits.json` seed file, add an `image_filename` field with just the filename:

```json
{
  "title": "Flood Risk Map Overconfidence",
  "domain": "Flooding",
  "image_filename": "flood-risk.jpg",
  ...
}
```

3. Run the seed command:
```bash
python manage.py seed_exhibits
```

The seed command will automatically find the image file and link it to the exhibit.

### Method 2: Django Admin Interface

1. Place your image files in this folder (optional - you can upload from anywhere)
2. When creating or editing an exhibit in the Django admin:
   - Use the image field to upload or select an image file
   - The image will be automatically saved to this folder

## Image Naming

You can name your images anything you like. When using `image_filename` in JSON, use just the filename (e.g., `"my-image.jpg"`), not the full path.

## Supported Formats

Common image formats are supported:
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- WebP (.webp)

## Notes

- Images uploaded through the admin interface will be stored here automatically
- The image path in the database will be relative to the media root (e.g., `exhibits/images/your-image.jpg`)
- Make sure to run `python manage.py migrate` after the model changes to update your database
- If an image filename in JSON doesn't exist, the seed command will show a warning but continue processing
