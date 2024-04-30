import json
import random


def main():
    score = get_score()
    type = get_score_type(score)
    write_summary(score, type)


def get_score():
    # Sample numeric score (metric)
    return 80 + 5 * random.random()


def get_score_type(score):
    # Sample non-numeric classification (attribute)
    return "high" if score > 82 else "normal"


def write_summary(score, type):
    # Save summary.json with metrics and attributes
    print(f"score: {score}")
    print(f"type: {type}")
    with open("summary.json", "w") as f:
        json.dump(
            {
                "metrics": {"score": score},
                "attributes": {"type": type},
            },
            f,
        )


if __name__ == "__main__":
    main()
