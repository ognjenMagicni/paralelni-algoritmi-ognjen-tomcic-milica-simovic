import os
import cv2
import numpy as np
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt

# ----- CONFIG -----
INPUT_FOLDER = "./flowerdataset/tinput"
OUTPUT_FOLDER = "./flowerdataset/toutput"
VISUALIZE = True
NUM_IMAGES = 100  # broj slika za obradu
MIN_REGION_SIZE = 50  # smanjeno radi bolje preciznosti
# -------------------

def global_thresholding(region):
    previous_threshold = 0
    threshold = np.mean(region)
    while abs(threshold - previous_threshold) > 1:
        below = region[region < threshold]
        above = region[region >= threshold]
        if len(below) == 0 or len(above) == 0:
            break
        mean1 = np.mean(below)
        mean2 = np.mean(above)
        previous_threshold = threshold
        threshold = (mean1 + mean2) / 2
    return (region >= threshold).astype(np.uint8) * 255

def quadtree_segment(region):
    h, w = region.shape
    if h <= MIN_REGION_SIZE or w <= MIN_REGION_SIZE or np.std(region) < 5:
        return global_thresholding(region)

    mid_h, mid_w = h // 2, w // 2
    top_left = quadtree_segment(region[:mid_h, :mid_w])
    top_right = quadtree_segment(region[:mid_h, mid_w:])
    bottom_left = quadtree_segment(region[mid_h:, :mid_w])
    bottom_right = quadtree_segment(region[mid_h:, mid_w:])

    top = np.hstack((top_left, top_right))
    bottom = np.hstack((bottom_left, bottom_right))
    return np.vstack((top, bottom))

def visualize(original, segmented, image_name):

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original, cmap='gray')
    axes[0].set_title("Original")
    axes[1].imshow(segmented, cmap='gray')
    axes[1].set_title("Segmented")
    for ax in axes:
        ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, f"{image_name}_comparison.png"))
    plt.close()

def process_image(image_path):
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Failed to load {image_path}")
        return None

    segmented = quadtree_segment(image)

    kernel = np.ones((3, 3), np.uint8)
    segmented = cv2.morphologyEx(segmented, cv2.MORPH_OPEN, kernel)

    if VISUALIZE:
        visualize(image, segmented, image_name)

    return {
        "image_name": image_name,
        "status": "Done"
    }

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    image_files = [os.path.join(INPUT_FOLDER, f) for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    image_files = image_files[:NUM_IMAGES]
    print(f"Found {len(image_files)} images to process.")
    if not image_files:
        print("No images found in the input folder.")
        return

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_image, image_files)

    for result in results:
        if result:
            print(f"{result['image_name']}: {result['status']}")

if __name__ == "__main__":
    main()
