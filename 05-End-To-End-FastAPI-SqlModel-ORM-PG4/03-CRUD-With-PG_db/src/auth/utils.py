from passlib.context import CryptContext

password_context = CryptContext(
    schemes=["bcrypt"]
)

def generate_password_hash(password: str) -> str:
    hash = password_context.hash(password)
    print(hash)

    return hash


def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)


if __name__ == "__main__":
    generate_password_hash("alamin")