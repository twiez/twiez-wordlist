import itertools


def generate_password_wordlist(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    chars = ""
    
    if use_lowercase:
        chars += "abcdefghijklmnopqrstuvwxyz"
    if use_uppercase:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_digits:
        chars += "0123456789"
    if use_special_chars:
        chars += "!@#$%^&*()_-+=<>?"

    if not chars:
        print("En az bir karakter tipi seçmelisiniz.")
        return

    password_generator = itertools.product(chars, repeat=length)
    wordlist = [''.join(password) for password in password_generator]

    with open("password_wordlist.txt", "w") as file:
        for password in wordlist:
            file.write(password + '\n')

    print(f"Wordlist başarıyla oluşturuldu: password_wordlist.txt")

def main():
    print ("Twiez Wordlist")
    print("--------------------------------")

    length = int(input("Şifre uzunluğunu girin: "))
    use_lowercase = input("Küçük harf kullanılsın mı? (Y/n): ").lower() == 'e'
    use_uppercase = input("Büyük harf kullanılsın mı? (Y/n): ").lower() == 'e'
    use_digits = input("Sayı kullanılsın mı? (E/H): ").lower() == 'e'
    use_special_chars = input("Özel karakterler kullanılsın mı? (Y/n): ").lower() == 'e'

    generate_password_wordlist(length, use_lowercase, use_uppercase, use_digits, use_special_chars)

if __name__ == "__main__":
    main()