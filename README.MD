# Скрипт для свапа токенов в сети Base

Этот скрипт на Python выполняет свап токенов в сети Base, используя API Jumper Exchange. Скрипт случайным образом выбирает количество эфира и токен из предварительно заданного списка, проверяет цену газа и затем выполняет транзакцию свапа.

## Предварительные требования

Перед запуском скрипта убедитесь, что у вас есть следующее:

- Python 3.7 или выше
- Файл `.env` с необходимыми переменными окружения
- Внутри файла `.env` создаем константы `BASE_RPC_URL`, `PRIVATE_KEY`,`ADDRESS`

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Установите необходимые Python-пакеты:**

     ```bash
    pip install -r requirements.txt
   ```
3. **Создайте файл .env в корневом каталоге проекта со следующими переменными:**

    ```bash
    BASE_RPC_URL=<your_base_rpc_url>
    PRIVATE_KEY=<your_private_key>
    ADDRESS=<your_wallet_address>
    ```

4. **Заполните файл settings.py. Пример:**

      ```bash
    TOKENS_TO = ['0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2', '0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913']
    MAX_AMOUNT = 0.1
    MIN_AMOUNT = 0.01
    MAX_GAS_PRICE = 50
    CHAIN_ID = 8453
    TOKEN_FROM = '0x4200000000000000000000000000000000000006'
    MAX_GAS_LIMIT = 200000
    ```
## Использование 
 **Для запуска скрипта выполните следующую команду**
```bash
python main.py
   ```
