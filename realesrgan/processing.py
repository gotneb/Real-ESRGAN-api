import subprocess

BINARY_PATH = "binary/realesrgan-ncnn-vulkan"

# Input and output image paths
# input_image = "inputs/input.jpg"


def run_model(input_image, filename: str, scale="2"):
    if scale not in ["2", "3", "4"]:
        print("Invalid scale parameter!")
        return
    
    output_image = f"outputs/{filename}.jpg"
    print(output_image)
    cmd = [BINARY_PATH, "-i", input_image, "-o", output_image, "-s", scale]

    # Execute the binary
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Processing completed successfully!")
    except subprocess.CalledProcessError as e:
        print("Error ocurred")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)