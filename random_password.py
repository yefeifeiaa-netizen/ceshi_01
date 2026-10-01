import argparse
import secrets
import string


def generate_password(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main() -> None:
    parser = argparse.ArgumentParser(description="生成一个随机密码")
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=3,
        help="要生成的密码数量，默认为 3",
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=16,
        help="每个密码的长度，默认为 16",
    )
    args = parser.parse_args()

    if args.number < 1 or args.length < 1:
        parser.error("数量和长度都必须大于 0")

    for index in range(args.number):
        print(f"{index + 1}. {generate_password(args.length)}")


if __name__ == "__main__":
    main()
