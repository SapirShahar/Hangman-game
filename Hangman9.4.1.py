def choose_word(file_path, index):
    input_file = open(file_path, "r")
    words_lst= input_file.read()
    #print (words_lst)
    words_lst= words_lst.split(' ')
    #print(words_lst)
    uniqe_word=[]
    a_len_lst=len(words_lst)
    if index > a_len_lst:
        index=index-a_len_lst
    for i in words_lst:
        if i not in uniqe_word:
            uniqe_word.append(i)
    u_len_lst= len(uniqe_word)
    #print (uniqe_word)
    #print (len_lst)
    specific_word= words_lst[index-1]
    #print (specific_word)
    tuple1= u_len_lst,specific_word
    print (tuple1)


def main():
   user_index=int(input("enter a number:"))
   choose_word(r"C:\Users\sapirb\Desktop\אישי\python\files ex\words.txt",user_index)

if __name__ == "__main__":
       main()