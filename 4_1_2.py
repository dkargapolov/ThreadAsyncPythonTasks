import asyncio
from datetime import datetime
from termcolor import colored
from pynput import keyboard

async def show_time():
    while True:
        date_str = colored(datetime.now().strftime('%Y-%m-%d'), 'blue')
        time_str = colored(datetime.now().strftime('%H:%M:%S'), 'green')
        print(f"\r{date_str} {time_str}", end="")
        await asyncio.sleep(1)

def on_press(key):
    if key == keyboard.Key.esc:
        print("\nВыход из программы по нажатию Esc.")
        return False  # Прекращаем слушать нажатия клавиш

async def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    try:
        await show_time()
    except asyncio.CancelledError:
        print("Завершение программы.")
    finally:
        listener.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа остановлена через Ctrl+C.")
