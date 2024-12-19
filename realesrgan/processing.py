import subprocess

BINARY_PATH = "binary/realesrgan-ncnn-vulkan"
OUT_DIR = '.outputs'

def run_model(input_image, filename: str, scale="2"):
    if scale not in ["2", "3", "4"]:
        print(f'Invalid scale \"{scale}\" parameter!')
        return
    
    output_img = f"{OUT_DIR}/{filename}.jpg"
    cmd = [BINARY_PATH, "-i", input_image, "-o", output_img, "-s", scale]

    # Execute the binary
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Processing completed successfully!")
        return output_img
    except subprocess.CalledProcessError as e:
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)