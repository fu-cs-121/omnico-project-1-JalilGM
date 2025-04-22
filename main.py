# =============================================================================
# OmniCo Confidential
# -------------------
# This source code contains proprietary information of OmniCo.
# Unauthorized use, duplication, or distribution is strictly prohibited.
# Violations may result in immediate action by the OmniCo Cybernetic Legal AI (CLAIR) system.
# By using this code, you agree to these terms across all possible timelines.
# Remember, at OmniCo, we're not just shaping the future—we own it.
# =============================================================================

def main():
    # Initialize the stats dictionary for each algorithm
    stats = {
        'JoyStream': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'SerenityFlow': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'DeepPulse': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        }
    }
    
    # Open the CSV file and read data
    with open('euphoria_data.csv', 'r') as file:
        # Skip the header line
        header = file.readline()
        
        # Read each line in the file
        for line in file:
            # Process each line here
            # print(line)  # This will print each line with newline characters

            # To remove whitespace and newline characters:
            clean_line = line.strip()
            # print(clean_line)
            # Remove any trailing whitespace characters like newline
            # line = line.strip()
            
            # Split the line into a list of values
            columns = line.split(',')
            
            # Assign each column to a variable
            user_id = columns[0]
            algorithm = columns[1]
            
            # TODO: Define session_duration and happiness_rating variables and convert them to integers
            session_duration = int(columns[2])
            happiness_rating = int(columns[3])
            
            # Update stats based on the algorithm
            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                # Handle any unexpected algorithm names
                print(f"Unknown algorithm: {algorithm}")
    
    # TODO: Calculate averages for each algorithm
    # For each algorithm in the stats dictionary:
    #   - Calculate avg_happiness = total_happiness / session_count
    #   - Calculate avg_duration = total_duration / session_count
    #   - Store these back into the stats dictionary under 'avg_happiness' and 'avg_duration'
    for algorithm, data in stats.items():
        if data['session_count'] > 0:  # Avoid division by zero
            data['avg_happiness'] = data['total_happiness'] / data['session_count']
            data['avg_duration'] = data['total_duration'] / data['session_count']
    # TODO: Determine the algorithm with the highest average happiness rating
    # Initialize  variables to keep track of the highest average happiness and the corresponding algorithm
    # Loop through stats to compare avg_happiness values
    joystream_happiness_avg = stats['JoyStream']['avg_happiness']
    serenityflow_happiness_avg = stats['SerenityFlow']['avg_happiness']
    deeppulse_happiness_avg = stats['DeepPulse']['avg_happiness']
    highest_happiness_avg = max(stats, key=lambda alg: stats[alg]['avg_happiness'])

   
    # TODO: Determine the algorithm with the longest average session duration
    # Initialize variables to keep track of the longest average duration and the corresponding algorithm
    # Loop through stats to compare avg_duration values
    joystream_duration_avg = stats['JoyStream']['avg_duration']
    serenityflow_duration_avg = stats['SerenityFlow']['avg_duration']
    deeppulse_duration_avg = stats['DeepPulse']['avg_duration']
    highest_duration_avg = max(stats, key=lambda alg: stats[alg]['avg_duration'])
    
    # TODO: Print the report
    # Use print statements to display the results in a formatted way
    # Follow the structure provided in the example output
    title ="Euphoria User Engagement Analysis Report"
    print(title)
    print("-" * int(len(title)))
    print("\nAverage Happiness Rating per Algorithm:")
    print(f"- JoyStream: {joystream_happiness_avg}")
    print(f"- SerenityFlow: {serenityflow_happiness_avg}")
    print(f"- DeepPulse: {deeppulse_happiness_avg}")

    print("\nTotal Number of Sessions per Algorithm:")
    print(f"- JoyStream: {stats['JoyStream']['session_count']}")
    print(f"- SerenityFlow: {stats['SerenityFlow']['session_count']}")
    print(f"- DeepPulse: {stats['DeepPulse']['session_count']}")

    print("\nAverage Session Duration per Algorithm:")
    print(f"- JoyStream: {joystream_duration_avg} minutes")
    print(f"- SerenityFlow: {serenityflow_duration_avg} minutes")
    print(f"- DeepPulse: {deeppulse_duration_avg} minutes")

    print("\nHighest Average Happiness Rating:")
    print(f"{highest_happiness_avg} with an average happiness rating of {stats[highest_happiness_avg]['avg_happiness']}")

    print("\nLongest Average Session Duration:")
    print(f"{highest_duration_avg} with an average session duration of {stats[highest_duration_avg]['avg_duration']} minutes")



if __name__ == "__main__":
    main()