import sys

# -------------------- UTILITY FUNCTIONS -------------------- #

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def calculate_rank(word):
    word = list(word)
    length = len(word)
    rank = 1

    for i in range(length):
        smaller_chars = set()

        for j in range(i + 1, length):
            if word[j] < word[i]:
                smaller_chars.add(word[j])

        for ch in smaller_chars:
            temp = word[i:].copy()
            temp.remove(ch)

            freq = {}
            for char in temp:
                freq[char] = freq.get(char, 0) + 1

            numerator = factorial(len(temp))

            denominator = 1
            for count in freq.values():
                denominator *= factorial(count)

            rank += numerator // denominator

    return rank


def is_yes(inp):
    return inp.strip().lower() in ["yes", "y", "yeah", "yo", "ofc"]


def is_no(inp):
    return inp.strip().lower() in ["no", "n", "nope", "nah"]


# -------------------- UI FUNCTIONS -------------------- #

def print_header():
    print("\n" + "=" * 70)
    print("📘 DICTious — Dictionary Rank Finder".center(70))
    print("=" * 70)


def print_footer():
    print("\n" + "=" * 70)
    print("✨ Thank you for using DICTious ✨".center(70))
    print("=" * 70 + "\n")


# -------------------- MAIN LOOP -------------------- #

def main():
    print_header()

    while True:
        print("\n" + "-" * 70)
        word = input("🔤 Enter a word: ").strip().lower()

        if not word.isalpha():
            print("⚠️  Please enter a valid word (alphabets only).")
            continue

        rank = calculate_rank(word)

        print("\n" + "-" * 70)
        print(f"📊 Rank of '{word}' in dictionary order: {rank}".center(70))
        print("-" * 70)

        while True:
            choice = input("\n🔁 Try another word? (y/n): ")

            if is_yes(choice):
                break
            elif is_no(choice):
                print_footer()
                sys.exit()
            else:
                print("🤨 bro type properly... (y/n only)")


if __name__ == "__main__":
    main()
