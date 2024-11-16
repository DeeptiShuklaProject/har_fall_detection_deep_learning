import os
import requests
import zipfile
import tarfile

# Define paths
RAW_DATA_PATH = "data/raw/"
os.makedirs(RAW_DATA_PATH, exist_ok=True)

def download_file(url, output_path):
    """
    Download a file from a URL and save it locally.
    """
    print(f"Downloading from {url}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded to {output_path}")
    else:
        print(f"Failed to download from {url}. Status code: {response.status_code}")
        return None

def extract_file(file_path, extract_to):
    """
    Extract ZIP or TAR.GZ files to the specified directory.
    """
    print(f"Extracting {file_path}...")
    if file_path.endswith(".zip"):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    elif file_path.endswith(".tar.gz"):
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_to)
    else:
        print(f"Unknown file type for extraction: {file_path}")
        return
    print(f"Extracted to {extract_to}")

def download_kinetics():
    """
    Download and extract the Kinetics dataset.
    """
    kinetics_url = "https://example.com/kinetics-dataset.tar.gz"  # Replace with actual URL
    kinetics_file = os.path.join(RAW_DATA_PATH, "kinetics-dataset.tar.gz")
    download_file(kinetics_url, kinetics_file)
    extract_file(kinetics_file, RAW_DATA_PATH)

def download_urfd():
    """
    Download and extract the URFD dataset.
    """
    urfd_url = "https://example.com/urfd-dataset.zip"  # Replace with actual URL
    urfd_file = os.path.join(RAW_DATA_PATH, "urfd-dataset.zip")
    download_file(urfd_url, urfd_file)
    extract_file(urfd_file, RAW_DATA_PATH)

if __name__ == "__main__":
    print("Starting dataset download...")
    download_kinetics()
    download_urfd()
    print("All datasets downloaded and extracted.")
