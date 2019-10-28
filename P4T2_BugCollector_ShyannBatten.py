#Program keeps a running total of bugs.
#10/09/19
#CTI-110 P4T2 - Bug Collector
#Shyann Batten
#

# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 6):
    # Prompt the user.
    print('Enter the bugs collected on day', day)
    # Input the number of bugs.
    bugs = int(input())
    # Add bugs to total.
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')


