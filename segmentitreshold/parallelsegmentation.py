import os
import cv2
import numpy as np
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt

# ----- CONFIG -----
INPUT_FOLDER = "C:/Users/milic/OneDrive/Desktop/fak/master/SEM2/paralelni/segmentitreshold/xraydataset/input"
OUTPUT_FOLDER = "./xraydataset/output"
VISUALIZE = True
NUM_IMAGES = 100  # br slika za procesovanje
SEED_THRESHOLD = (100, 150) 
# -------------------

def select_seeds(image, threshold=(100, 150)):
    
    seeds = np.argwhere((image >= threshold[0]) & (image <= threshold[1]))
    return seeds.tolist()

def region_growing(image, seeds, threshold=15):
    height, width = image.shape
    segmented = np.zeros((height, width), dtype=np.int32)
    visited = np.zeros((height, width), dtype=bool)
    
    region_id = 1
    for seed in seeds:
        x0, y0 = seed
        if visited[x0, y0]:
            continue
        seed_intensity = image[x0, y0]
        stack = [(x0, y0)]

        while stack:
            x, y = stack.pop()
            if visited[x, y]:
                continue
            visited[x, y] = True
            diff = abs(int(image[x, y]) - int(seed_intensity))
            if diff < threshold:
                segmented[x, y] = region_id
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < height and 0 <= ny < width and not visited[nx, ny]:
                        stack.append((nx, ny))

        region_id += 1

    return segmented

def extract_features(labeled_segmented):
    features = []
    unique_labels = np.unique(labeled_segmented)
    for label in unique_labels:
        if label == 0:
            continue
        mask = (labeled_segmented == label).astype(np.uint8)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            x, y, w, h = cv2.boundingRect(cnt)
            features.append({'label': label, 'area': area, 'bounding_box': (x, y, w, h)})
    return features


def visualize(image, labeled_segmented, image_name):
    color_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    unique_labels = np.unique(labeled_segmented)
    for label in unique_labels:
        if label == 0:
            continue  # background
        mask = labeled_segmented == label
        color = np.random.randint(0, 255, size=3).tolist()
        color_image[mask] = color

    # Plot original vs colored regions
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title("Original")

    axes[1].imshow(color_image)
    axes[1].set_title("Segmented (Labeled Colors)")

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

    seeds = select_seeds(image, SEED_THRESHOLD)
    segmented = region_growing(image, seeds)
    features = extract_features(segmented)

    if VISUALIZE:
        visualize(image, segmented, image_name)

    return {
        "image_name": image_name,
        "features": features
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
            print(f"{result['image_name']}: {len(result['features'])} region(s) found.")

if __name__ == "__main__":
    main()
