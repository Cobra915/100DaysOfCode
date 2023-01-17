
input = input(f"Please input a score: ")
score = int(input)

def score_printer(score):
    if score < 80 and score > 70:
        print("A")
    elif score < 90 or score > 80:
        print("B")
    elif score > 60:
        print("C")
    else:
        print("D")

# Main function:
if __name__ == "__main__":
    score_printer(score)
