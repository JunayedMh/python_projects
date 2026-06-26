class WordAnalyzer:
    def __init__(self, text:str):
        self.text = text
        self.word_count = {}
    
    def is_empty(self):
        return not self.text.strip()
    def analyze(self):
        pun = ".,!?;:'\"-()[]{}/"
        for word in self.text.lower().split():
            clean = word.strip(pun)
            if clean not in self.word_count:
                self.word_count[clean] = 0
            self.word_count[clean] += 1
    def top_words(self, n=5):
        sorted_words = []

        for word, count in self.word_count.items():
            sorted_words.append((word,count))
        sorted_words.sort(key = lambda x:x[1], reverse=True)
        return sorted_words[:n]
    def report(self):
        if self.is_empty():
            print("No text entered.")
            return
        self.analyze()
        print("\nTop 5 Words: ")
        for word,count in self.top_words():
            print(f"{word}: {count}")
        print(f"\nTotal words: {sum(self.word_count.values())}")
        print(f"Unique words: {len(self.word_count)}")
if __name__ == "__main__":
    Text = WordAnalyzer(input("Enter your paragraph: "))
    Text.report()