import os

def list_folders():
    # Go 3 levels up from current working directory
    base_path = os.path.abspath(os.path.join(os.getcwd(), "../../.."))
    print(f"📂 Listing folders in: {base_path}\n")

    try:
        for item in os.listdir(base_path):
            full_path = os.path.join(base_path, item)
            if os.path.isdir(full_path):
                print(f"📁 {item}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    list_folders()