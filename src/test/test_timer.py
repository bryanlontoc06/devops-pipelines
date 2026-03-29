import threading

print("Starting tests...")


def test_my_function():
    print("\nStarting test...")
    results: list[bool] = []

    def my_function():
        print("3 seconds have passed!")
        results.append(True)

    # Setup timer
    timer = threading.Timer(3.0, my_function)
    timer.start()

    print("Timer started, waiting...")
    timer.join()

    assert len(results) == 1
    assert results[0] is True
    print("Timer finished successfully.")
