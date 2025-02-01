
"""
    Design a search autocomplete system for a search engine. Users may input
    a sentence (at least one word and end with a special character '#').

    You are given a string array sentences and an integer array times both
    of length n where sentences[i] is a previously typed sentence and
    times[i] is the corresponding number of times the sentence was typed.
    For each input character except '#', return the top 3 historical hot
    sentences that have the same prefix as the part of the sentence already
    typed.

    Here are the specific rules:

    The hot degree for a sentence is defined as the number of times a user
    typed the exactly same sentence before.
    The returned top 3 hot sentences should be sorted by hot degree (The
    first is the hottest one). If several sentences have the same hot
    degree, use ASCII-code order (smaller one appears first).
    If less than 3 hot sentences exist, return as many as you can.
    When the input is a special character, it means the sentence ends, and
    in this case, you need to return an empty list.
    Implement the AutocompleteSystem class:

    AutocompleteSystem(String[] sentences, int[] times) Initializes the
    object with the sentences and times arrays.
    List<String> input(char c) This indicates that the user typed the
    character c.
    Returns an empty array [] if c == '#' and stores the inputted sentence
    in the system.
    Returns the top 3 historical hot sentences that have the same prefix as
    the part of the sentence already typed. If there are fewer than 3
    matches, return them all.
"""

from collections import defaultdict
import heapq    

class AutocompleteSystem:
    def __init__(self, sentences: list, times: list):
        self.root = self.TrieNode()
        self.currentInput = ""
        self.currentNode = self.root
        self.sentenceFrequency = defaultdict(int)
        
        # Initialize sentence frequencies and build the Trie
        for sentence, time in zip(sentences, times):
            self.sentenceFrequency[sentence] += time
            self._addSentence(sentence, self.sentenceFrequency[sentence])

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.hotSentences = []

    def _addSentence(self, sentence: str, frequency: int):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
            self._updateHotSentences(node, sentence, frequency)

    def _updateHotSentences(self, node, sentence, frequency):
        # Remove the sentence if it already exists
        for i, (freq, s) in enumerate(node.hotSentences):
            if s == sentence:
                node.hotSentences.pop(i)
                break
        # Add the updated frequency
        heapq.heappush(node.hotSentences, (-frequency, sentence))
        # Keep only top 3
        if len(node.hotSentences) > 3:
            heapq.heappop(node.hotSentences)

    def input(self, c: str) -> list:
        if c == '#':
            self.sentenceFrequency[self.currentInput] += 1
            self._addSentence(self.currentInput, self.sentenceFrequency[self.currentInput])
            self.currentInput = ""
            self.currentNode = self.root
            return []
        
        self.currentInput += c
        if self.currentNode:
            self.currentNode = self.currentNode.children.get(c, None)
        
        if not self.currentNode:
            return []
        
        # Retrieve sorted hot sentences
        return sorted([(-freq, s) for freq, s in self.currentNode.hotSentences], 
                      key=lambda x: (-x[0], x[1]))[:3]


def main():
    # Initialize the AutocompleteSystem with given sentences and times
    sentences = ["i love you", "island", "ironman", "i love leetcode"]
    times = [5, 3, 2, 2]
    autocomplete = AutocompleteSystem(sentences, times)
    
    # Define a sequence of input characters
    input_sequence = ['i', ' ', 'a', '#']
    
    # Process each character and print the suggestions
    for char in input_sequence:
        suggestions = autocomplete.input(char)
        print(f"Input: '{char}' -> Suggestions: {suggestions}")
        
        
        # Define a sequence of input characters
    input_sequence = ['i', ' ', 'l', '#']
    
    # Process each character and print the suggestions
    for char in input_sequence:
        suggestions = autocomplete.input(char)
        print(f"Input: '{char}' -> Suggestions: {suggestions}")

if __name__ == "__main__":
    main()
