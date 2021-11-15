def main():
    scores = get_scores()

    total_scores = get_total(scores)

    lowest_score = min(scores)

    total_scores -= lowest_score

    average = total_scores/(len(scores)-1)
    print("Average is:", average)


def get_scores():
    score_list = []

    again = 'y'
    while again == 'y':
        value = float(input("Enter a score:"))
        score_list.append(value)

        again = input("Do you want to add another number?")

    return score_list

def get_total(scores):
    total = 0

    for values in scores:
        total += values

    return total


main()
