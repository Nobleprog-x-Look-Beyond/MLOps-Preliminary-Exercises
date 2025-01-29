import os


def main():
    user_name = os.getenv("USER_NAME", "Stranger")
    print(f"Hello, {user_name} from Docker!")


if __name__ == "__main__":
    main()
