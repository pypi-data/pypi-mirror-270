import pandas as pd
import re # optional
import matplotlib.pyplot as plt
import seaborn as sns

# Load the tweet data from CSV
tweet_data = pd.read_csv('tweet_data.csv')

# List of keywords to approximate locations
location_keywords = [
    'New York', 'London', 'Paris', 'Tokyo', 'Los Angeles', 'Berlin',
    'Chicago', 'San Francisco', 'Dubai', 'Toronto', 'Boston', 'Portland', 'Denver'
]

# Function to find keywords in text
def find_locations(text, keywords):
    found_locations = []
    tweet_words = text.split()
    # Search for keywords in the text (case-insensitive)
    for keyword in keywords:
        # regular expression method:
        # if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
        #     found_locations.append(keyword)
        if keyword in tweet_words:
            found_locations.append(keyword)
    return found_locations


# Extract all locations from tweets using the keyword list
all_locations = []
for tweet in tweet_data['text']:  # Adjust column name as needed
    locations = find_locations(tweet, location_keywords)
    all_locations.extend(locations)

# Create a DataFrame from the extracted locations
locations_df = pd.DataFrame(all_locations, columns=['Location'])

# Count the frequency of each location using value_counts
location_counts = locations_df['Location'].value_counts()
print(location_counts)

# sort
location_counts = location_counts.sort_values(ascending=False)

# Get the top 10 most mentioned locations
top_locations = location_counts.head(10)
print(top_locations)

# Convert to a DataFrame for easier plotting
top_locations_df = top_locations.reset_index()
top_locations_df.columns = ['Location', 'Count']

# Plotting the top locations
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Location', data=top_locations_df, palette="viridis")
plt.xlabel('Number of Mentions')
plt.ylabel('Location')
plt.title('Top Locations Mentioned in Tweets')
plt.show()
