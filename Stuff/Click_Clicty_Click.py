import keyboard  # External library for keyboard control

def on_key_event(event):
    """Callback function to handle key events."""
    print(f"Key: {event.name} | Event Type: {event.event_type}")

try:
    print("Press ESC to stop...")
    # Hook all keyboard events
    keyboard.hook(on_key_event)

    # Wait until 'esc' is pressed
    keyboard.wait('esc')

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except Exception as e:
    print(f"Error: {e}")