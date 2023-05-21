'''
In this example, we have a sample user-item matrix representing the ratings of users for different items.
The cosine_similarity function calculates the cosine similarity between two users based on their ratings.
The generate_recommendations function takes a user ID, user-item matrix, and optional top_n parameter to generate
recommendations for the given user. It calculates the similarity between the user and other users, sorts them in
descending order, and returns the top recommended items that the user has not yet rated.

In the example usage, we generate recommendations for User 0 based on the provided user-item matrix.
The recommended items are printed out.

Note that this is a simplified implementation, and there are more advanced techniques and algorithms available
for building recommendation systems. Additionally, you can incorporate additional features, such as item metadata
or user preferences, to improve the quality of recommendations.

Collaborative filtering suggests items based on the preferences of similar users or the similarity of items.
Here's an example of how you can implement a basic collaborative filtering recommendation system using Python:
'''

import numpy as np

# Sample user-item matrix
user_item_matrix = np.array([
    [4, 5, 0, 0, 3],
    [5, 0, 4, 0, 4],
    [0, 3, 0, 4, 0],
    [4, 0, 4, 0, 4],
    [0, 4, 0, 5, 0]
])

# Function to calculate similarity between two users using cosine similarity
def cosine_similarity(user1, user2):
    dot_product = np.dot(user1, user2)
    norm_user1 = np.linalg.norm(user1)
    norm_user2 = np.linalg.norm(user2)
    return dot_product / (norm_user1 * norm_user2)

# Function to generate recommendations for a user
def generate_recommendations(user_id, user_item_matrix, top_n=3):
    user_ratings = user_item_matrix[user_id]
    similarities = []
    for user in user_item_matrix:
        similarity = cosine_similarity(user_ratings, user)
        similarities.append(similarity)
    
    similarities = np.array(similarities)
    sorted_indices = np.argsort(similarities)[::-1]  # Sort in descending order
    
    recommendations = []
    for i in range(top_n):
        similar_user_id = sorted_indices[i]
        similar_user_ratings = user_item_matrix[similar_user_id]
        recommended_items = np.where(similar_user_ratings > 0)[0]
        for item in recommended_items:
            if user_ratings[item] == 0:
                recommendations.append(item)
        if len(recommendations) >= top_n:
            break
    
    return recommendations

# Example usage:
user_id = 0
recommendations = generate_recommendations(user_id, user_item_matrix)
print("Recommendations for User", user_id)
for item in recommendations:
    print("Item", item)
