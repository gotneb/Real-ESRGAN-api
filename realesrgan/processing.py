import subprocess
from utils import get_timestamp, list_tmp_files

# Used by render
OUT_DIR = '/tmp'
BINARY_PATH = "binary/realesrgan-ncnn-vulkan"


def run_model(input_image, filename: str, scale="2"):
    if scale not in ["2", "3", "4"]:
        print(f'Invalid scale \"{scale}\" parameter!')
        return
    
    output_img = f"{OUT_DIR}/out_{filename}.jpg"
    cmd = [BINARY_PATH, "-i", input_image, "-o", output_img, "-s", scale]

    # Execute the binary
    try:
        print(f'Before:\n{list_tmp_files()}')
        print("Processing image...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Processing completed successfully!")
        print(f'After:\n{list_tmp_files()}')
        return output_img
    except subprocess.CalledProcessError as e:
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
    except e:
        print(f'Error in run_model:\n{e}')