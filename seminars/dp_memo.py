import time

# Кеш для хранения уже вычисленных значений fib(k)
memo_fib = {0: 0, 1: 1}

def fib_memo(n):
    """Вычисляет числа Фибоначчи с использованием мемоизации (явный кеш)."""
    print(f"Попытка вычислить fib_memo({n})")

    if n < 0:
        raise ValueError("N должно быть >= 0")

    # 1. Проверка кеша
    if n in memo_fib:
        value = memo_fib[n]
        print(f"Нашли fib({n})={value} в кеше!")
        return value
    # 3. Рекурсивный шаг (если не в кеше и не базовый случай)
    print(f"Вычисляем fib({n})")
    number = fib_memo(n - 1) + fib_memo(n - 2)
    # 4. Сохранение в кеш ПЕРЕД возвратом
    print(f"Сохраняем fib({n}) = {number} в кеш")
    memo_fib[n] = number

    # 5. Возврат
    return number

if __name__ == "__main__":
    n_val = 5
    print(f"\n--- Вычисляем fib({n_val}) с мемоизацией ---")
    start_time = time.perf_counter()
    result_memo = fib_memo(n_val)
    end_time = time.perf_counter()
    print(f"fib({n_val}) = {result_memo}")
    print(f"Время выполнения: {end_time - start_time:.6f} сек")  # Должно быть МГНОВЕННО!

    # Посмотрим на кеш после вычислений (для интереса)
    print(f"\nСодержимое кеша memo_fib после вычисления fib({n_val}):")
    print(memo_fib)

    # Повторный вызов должен быть еще быстрее, т.к. всё уже в кеше
    print(f"\n--- Повторный вызов fib({n_val}) ---")
    start_time = time.perf_counter()
    result_memo_again = fib_memo(n_val)
    end_time = time.perf_counter()
    print(f"fib({n_val}) = {result_memo_again}")
    print(f"Время выполнения повторного вызова: {end_time - start_time:.6f} сек")
