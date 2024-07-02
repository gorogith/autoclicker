from pynput.mouse import Button, Controller
from pynput import keyboard
import time
import threading

mouse = Controller()
clicking = False
running = True

def on_press(key):
    global clicking, running
    if key == keyboard.Key.f8:
        clicking = not clicking
        print("Clicking " + ("dimulai" if clicking else "dihentikan"))
    elif key == keyboard.Key.esc:
        running = False
        return False  # Menghentikan listener

def clicker(interval):
    global clicking
    while running:
        if clicking:
            mouse.click(Button.left)
        time.sleep(interval)

def main():
    try:
        interval = float(input("Masukkan interval klik dalam detik: "))
        print("Bot siap. Tekan 'F8' untuk memulai/menghentikan klik, 'ESC' untuk keluar program.")
        
        click_thread = threading.Thread(target=clicker, args=(interval,))
        click_thread.start()
        
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        
        click_thread.join()
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk interval.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
