import json
import os
import uuid
import time
from colorama import init, Fore, Style
os.system("title Cursor Ai Trail Reset")
os.system("cls")
# Initialize colorama
init()

def generate_new_id():
    # Generate a new UUID
    return str(uuid.uuid4())

def update_ids_in_json():
    # Dynamically get the file path for the current user
    user_folder = os.path.expanduser('~')  # This will give the current user's home directory
    file_path = os.path.join(user_folder, 'AppData', 'Roaming', 'Cursor', 'User', 'globalStorage', 'storage.json')

    # Check if the file exists
    if not os.path.exists(file_path):
        print(Fore.RED + f"[ERROR] File {file_path} does not exist!" + Style.RESET_ALL)
        return

    try:
        # Open the JSON file and load its content
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print(Fore.YELLOW + f"\n[INFO] Successfully loaded {file_path}" + Style.RESET_ALL)
        time.sleep(1)  # Add 1-second delay

        # Function to recursively find and update IDs
        def update_ids(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    # Check if the value is a string and looks like a UUID (length 36)
                    if isinstance(value, str) and len(value) == 36 and value.count('-') == 4:
                        print(Fore.CYAN + f"[INFO] Found UUID: {value}" + Style.RESET_ALL)
                        time.sleep(1)  # Add 1-second delay
                        obj[key] = generate_new_id()  # Replace with a new UUID
                        print(Fore.GREEN + f"[INFO] Replaced with: {obj[key]}" + Style.RESET_ALL)
                        time.sleep(1)  # Add 1-second delay
                    else:
                        update_ids(value)
            elif isinstance(obj, list):
                for item in obj:
                    update_ids(item)

        # Update IDs in the loaded data
        update_ids(data)

        # Save the updated data back to the file with 'w' mode to write string data
        with open(file_path, 'w', encoding='utf-8') as file:
            # Ensure the file object is treated as a string writer
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(Fore.GREEN + f"\n[SUCCESS] All IDs regenerated and saved successfully in {file_path}" + Style.RESET_ALL)
        time.sleep(1)  # Add 1-second delay before exit

    except Exception as e:
        print(Fore.RED + f"[ERROR] Error processing the file: {e}" + Style.RESET_ALL)

# Clear the console for a clean start
os.system('cls' if os.name == 'nt' else 'clear')

# Show a welcome message
print(Fore.MAGENTA + "*******************************************" + Style.RESET_ALL)
print(Fore.MAGENTA + "       UUID Regenerator for Cursor App     " + Style.RESET_ALL)
print(Fore.MAGENTA + "*******************************************" + Style.RESET_ALL)

# Run the function to update IDs
update_ids_in_json()

# Wait for the user to press Enter before exiting
input(Fore.YELLOW + "\nPress Enter to exit..." + Style.RESET_ALL)
