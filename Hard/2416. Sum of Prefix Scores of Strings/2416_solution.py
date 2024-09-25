class TrieNode:
    def __init__(self):
        self.children = {}  # Each node points to its child nodes (the next characters)
        self.prefix_count = 0  # This keeps track of how many words share this prefix


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Start with an empty root node

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root  # Start at the root of the Trie
        for char in word:
            # If the character doesn't exist as a child, create a new node for it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the next node (child corresponding to this character)
            node = node.children[char]
            # Every time we pass through this node, increment the prefix count
            node.prefix_count += 1

    # Calculate the total prefix score for a given word
    def calculate_prefix_score(self, word):
        node = self.root  # Start at the root of the Trie
        total_score = 0  # This will store the sum of prefix scores for the word
        for char in word:
            if char in node.children:
                node = node.children[char]
                # Add the prefix count of the current node to the total score
                total_score += node.prefix_count
            else:
                break  # If the character doesn't exist, no need to continue
        return total_score


def sum_prefix_scores(words):
    trie = Trie()  # Create a Trie data structure

    # Step 1: Insert all words into the Trie
    for word in words:
        trie.insert(word)  # Insert each word into the Trie

    answer = []  # This will store the result for each word

    # Step 2: Calculate the score for each word
    for word in words:
        score = trie.calculate_prefix_score(word)
        answer.append(score)

    return answer


# Example 1:
words = ["abc", "ab", "bc", "b"]
print(sum_prefix_scores(words))  # Output: [5, 4, 3, 2]

# Example 2:
words = ["abcd"]
print(sum_prefix_scores(words))  # Output: [4]
