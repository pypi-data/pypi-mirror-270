import os 
from jimmyskitchen.resources import get_data_folder, get_pngs_folder

def main():
    data_folder = get_data_folder()
    pngs_folder = get_pngs_folder()

    # Now you can access your data and image files using these folder paths
    # For example:
    data_file_path = os.path.join(data_folder, 'symbols/NVDA.csv')
    image_file_path = os.path.join(pngs_folder, 'returnsfull.png')

if __name__ == "__main__":
    main()


from jimmyskitchen.git_utils import get_latest_commit_message

def main():
    latest_commit_message = get_latest_commit_message()
    print(f"Latest commit message: {latest_commit_message}")

if __name__ == "__main__":
    main()