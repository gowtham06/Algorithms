class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.endOfWord=False

class Trie:

    def __init__(self):
        self.root=self.getNode()

    def getNode(self):
        return TrieNode()

    def char2Index(self,char):
        return ord(char)-ord('a')

    def insert_word(self,word):
        curr_node=self.root
        for item in word:
            item_index=self.char2Index(item)
            if(not curr_node.children[item_index]):
                curr_node.children[item_index]=self.getNode()
            curr_node=curr_node.children[item_index]
        curr_node.endOfWord=True

    def search_key(self,key):
        curr_node=self.root
        for item in key:
            curr_index=self.char2Index(item)
            if not curr_node.children[curr_index]:
                return False
            curr_node=curr_node.children[curr_index]
        return curr_node!=None and curr_node.endOfWord

    def getWords(self,curr_node,word,string_list):
        if(curr_node.endOfWord==True):
            string_list.append(word)
        for i in range(0,26):
            # print(i)
            if curr_node.children[i]:
                print(word+chr(ord('a')+i))
                self.getWords(curr_node.children[i],word+chr(ord('a')+i),string_list)
        return string_list


    def get_prefix_strings(self,prefix_key):
        curr_node=self.root
        check_flag=True
        prefix_strings=[]
        for item in prefix_key:
            curr_index=self.char2Index(item)
            if curr_node.children[curr_index]:
                curr_node=curr_node.children[curr_index]
            else:
                check_flag=False
                break;
        if not check_flag:
            return []
        else:
            return self.getWords(curr_node,prefix_key,[])

if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any",
            "by", "their","anyone","man","mancheseter"]
    trie_wrapper=Trie()
    for item in keys:
        trie_wrapper.insert_word(item)

    search_keys=["anyone","answer"]
    for item in search_keys:
        search_flag=trie_wrapper.search_key(item)
        if(search_flag):
            print("The key:{value1}, is present in the trie").format(value1=item)
        else:
            print("The key:{value1}, is not present in the trie").format(value1=item)

    prefix_strings=trie_wrapper.get_prefix_strings('')
    print(prefix_strings)

