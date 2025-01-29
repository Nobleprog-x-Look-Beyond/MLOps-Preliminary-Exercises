import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def do_something():
    logging.info("Starting something...")
    try:
        # Fake operation
        result = 10 / 2
        logging.debug(f"Result: {result}")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
    else:
        logging.info("Operation completed successfully!")


if __name__ == "__main__":
    logging.info("Application started")
    do_something()
    logging.info("Application finished")
