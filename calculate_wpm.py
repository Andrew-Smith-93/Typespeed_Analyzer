import csv

def calculate_wpm(words, time_seconds):
    words_per_minute = (len(words) / 5) / (time_seconds / 60)
    return words_per_minute

def main(csv_file_path):
    wpm_values = []
    total_words = 0
    total_time = 0

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter='|')  # Specify delimiter
        for row in csv_reader:
            wpm = float(row["wpm"])
            words = row["quoteLength"].split()
            time_seconds = float(row["testDuration"]) / 1000  # Convert milliseconds to seconds

            total_words += len(words)
            total_time += time_seconds
            wpm_values.append(wpm)

    # Calculate the average WPM for every 100 words
    average_wpm_per_100_words = []
    current_sum = 0
    current_count = 0

    for wpm in wpm_values:
        current_sum += wpm
        current_count += 1

        if current_count == 100:
            average_wpm = current_sum / 100
            average_wpm_per_100_words.append(average_wpm)
            current_sum = 0
            current_count = 0

    print("Average WPM per 100 words:")
    for i, average_wpm in enumerate(average_wpm_per_100_words, start=1):
        print(f"Test {i}: {average_wpm:.2f} WPM")

if __name__ == "__main__":
    csv_file_path = "results.csv"  # Replace with your CSV file name
    main(csv_file_path)

