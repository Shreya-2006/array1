def main():
    scores = [35, 50, 65, 85, 90]
    total = sum(scores)
    average = total / len(scores)
    print("== main/master output ==")
    print(f"total: {total}")
    print(f"average: {average}")
    print(f"minimun:{min(scores)}")
    print(f"maximum:{max(scores)}")

if __name__ == "__main__":
    main()
