import os
import shutil

BOOKS_DIR = "books"

def delete_data_folders():
    count = 0
    for item in os.listdir(BOOKS_DIR):
        item_path = os.path.join(BOOKS_DIR, item)
        if item.endswith("_data") and os.path.isdir(item_path):
            print(f"Deleting {item_path} ...")
            shutil.rmtree(item_path)
            count += 1
    print(f"Deleted {count} data folders.")

if __name__ == "__main__":
    delete_data_folders()
