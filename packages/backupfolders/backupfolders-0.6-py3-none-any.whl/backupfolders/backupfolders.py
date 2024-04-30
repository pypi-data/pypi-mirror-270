import os
import shutil
import datetime
import filecmp

class Backup:
    def backup(self, main_path, backup_folder_path, exclude_dirs=[]):
        # Create the backup folder if it doesn't exist
        if not os.path.exists(backup_folder_path):
            os.makedirs(backup_folder_path)

        # Get current date and time
        current_datetime = datetime.datetime.now()

        # Log statements
        log_messages = []

        # Log statement
        log_message_start = f"Backup of {os.path.basename(main_path)} started at: {current_datetime}"
        log_messages.append(log_message_start)
        print(log_message_start)  # Print to terminal

        # Create backup folder named after the desktop path
        main_folder_name = os.path.basename(main_path)
        main_backup_path = os.path.join(backup_folder_path, main_folder_name + "_backup")
        os.makedirs(main_backup_path, exist_ok=True)

        # Walk through the desktop directory
        for root, dirs, files in os.walk(main_path):
            # Exclude specified directories
            for exclude_dir in exclude_dirs:
                if exclude_dir in dirs:
                    dirs.remove(exclude_dir)

            # Get relative path to the desktop
            relative_path = os.path.relpath(root, main_path)

            # Create corresponding directory structure in the backup folder
            backup_subfolder = os.path.join(main_backup_path, relative_path)
            os.makedirs(backup_subfolder, exist_ok=True)

            # Check existing files and folders in the backup destination
            existing_files = os.listdir(backup_subfolder)
            existing_folders = [f for f in existing_files if os.path.isdir(os.path.join(backup_subfolder, f))]

            # Copy files to the backup folder
            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(backup_subfolder, file)

                # Check if file already exists in the backup destination
                if file in existing_files:
                    # Check if the file has been modified
                    if not filecmp.cmp(src_file, dest_file):
                        # File has been modified, replace it
                        shutil.copy2(src_file, dest_file)
                        log_message = f"Updated: {os.path.join(relative_path, file)}"
                        print(log_message)  # Print to terminal
                    else:
                        # File has not been modified, skip
                        log_message = f"Skipped: {os.path.join(relative_path, file)} (Not modified)"
                        print(log_message)  # Print to terminal
                else:
                    # File does not exist in the backup destination, copy it
                    shutil.copy2(src_file, dest_file)
                    log_message = f"Copied: {os.path.join(relative_path, file)}"
                    print(log_message)  # Print to terminal

            # Check for existing folders and files within those folders
            for folder in dirs:
                if folder in existing_folders:
                    # Folder already exists, skip
                    log_message = f"Skipped folder: {os.path.join(relative_path, folder)}"
                    print(log_message)  # Print to terminal
                else:
                    # Folder does not exist, create it
                    os.makedirs(os.path.join(backup_subfolder, folder), exist_ok=True)
                    log_message = f"Created folder: {os.path.join(relative_path, folder)}"
                    print(log_message)  # Print to terminal

        # Log completion
        completion_message = f"Backup of {os.path.basename(main_path)} completed at: {datetime.datetime.now()}"
        log_messages.append(completion_message)
        print(completion_message)  # Print to terminal

        # Write log messages to a text file
        log_file_path = os.path.join(backup_folder_path, "backup_log.txt")
        with open(log_file_path, "a") as log_file:
            for message in log_messages:
                log_file.write(message + "\n")
            log_file.write("\n")
