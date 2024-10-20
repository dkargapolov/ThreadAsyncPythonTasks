import threading
import time

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()  # Создание объекта Lock для синхронизации

    def deposit(self, amount):
        with self.lock:  # Захватываем блокировку перед внесением изменений
            print(f"Depositing {amount}...")
            initial_balance = self.balance
            time.sleep(0.1)  # Симулируем задержку операции
            self.balance = initial_balance + amount
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:  # Захватываем блокировку перед внесением изменений
            if self.balance >= amount:
                print(f"Withdrawing {amount}...")
                initial_balance = self.balance
                time.sleep(0.1)  # Симулируем задержку операции
                self.balance = initial_balance - amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print(f"Not enough balance to withdraw {amount}. Current balance: {self.balance}")

# Функция для потоков, которая выполняет несколько операций
def banking_operations(account):
    for _ in range(5):
        account.deposit(100)
        account.withdraw(50)

if __name__ == "__main__":
    account = BankAccount(500)  # Создаем счет с начальным балансом 500

    # Создаем два потока, которые будут выполнять банковские операции
    thread1 = threading.Thread(target=banking_operations, args=(account,))
    thread2 = threading.Thread(target=banking_operations, args=(account,))

    # Запускаем потоки
    thread1.start()
    thread2.start()

    # Дожидаемся завершения потоков
    thread1.join()
    thread2.join()

    print(f"Final balance: {account.balance}")
