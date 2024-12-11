import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--your_name', required=TRUE, help="Give us your name!  As a string, please.")
    args = parser.parse_args()

    runner_name = args.your_name
    
    print("Hello ", runner_name, "!")
    print("For more information on Itential Automation Service, check out:")
    print("https://docs.itential.com/itential-cloud/docs/announcements")

if __name__ == "__main__":
    main()
