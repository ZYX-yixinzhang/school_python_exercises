# 16321 programming1 Coursework1 Spell checker

# part1--main menu & deal with inputs

# calculate the total time taken
import time
start = time.time()

# start the program
# deal with inputs
while True:
    Main_Menu = ['quit', 'spell check a sentence', 'spell check a file']
    print("╔═══════ ╳ Main Menu╳ ═══════╗")
    for idx, val in enumerate(Main_Menu):
        print("║\000" + str(idx) + "." + val + "\000║".rjust(26-len(val)))
    print("╚════════════════════════════╝")
    choice_start = input(" please choose: ")

    # correct input
    # 0--quit the program
    if choice_start == str(0):
        print("thanks for using, goodbye!")
        break

    # spell check
    elif choice_start == str(1) or choice_start == str(2):
        # 1--sentence
        while True:
            if choice_start == str(1):
                sentence = input("please enter a sentence: ")

                # remove punctuation and split sentences
                sentence = sentence.lower()
                import re
                sentence = re.sub(r"[^A-Za-z ]", "", sentence)
                words_object = sentence.split()
                break

            # 2--file spelling check
            if choice_start == str(2):

                while True:
                    filename = input("please enter a file name: ")

                    # valid--split into words
                    try:
                        with open(filename, "r") as file_object:
                            input_lines = file_object.readlines()

                            # remove punctuations
                            words_list = []
                            for line in input_lines:
                                import re
                                line = re.sub(r"[^A-Za-z ]", "", line)
                                line = line.lower()
                                words_list.append(line)

                            # change to string & split string
                            words_file = (" ".join(str(i) for i in words_list))
                            words_object = words_file.split()

                    # file name not valid - try again
                    except FileNotFoundError:
                        print(f"Sorry, the file ' {filename} ' does not exits.")
                        continue
                    else:
                        break
                break

        # part2--spell checking

        with open("EnglishWords.txt", "r+") as file_source:
            content = file_source.read()
            words_source = content.split()

        wordcount = 0
        correct_count = 0
        error_count = 0
        added_count = 0
        changed_count = 0

        # check if the input includes English words--my idea
        if not words_object:
            print("The input you entered do not include any English words, please try again.")
            continue
        # check if correct
        else:
            for word in words_object:
                wordcount += 1

                if word in words_source:
                    print("Correct spelling: " + word)
                    correct_count += 1

            # if not correct --menu two
                else:
                    print(f"There is a spelling error on word '{word}',")
                    correcting_menu = ["ignore", "mark", "add to dictionary", "present a suggestion"]
                    while True:
                        print("╔══════ ╳ Correcting Menu╳ ══════╗")
                        for idx, val in enumerate(correcting_menu, start=1):
                            print("║\000" + str(idx) + "." + val + "║".rjust(29-len(val)))
                        print("╚════════════════════════════════╝")
                        choice_correct = input("Please choose: ")

                        # 1--ignore  count as correct spelling
                        if choice_correct == str(1):
                            correct_count = correct_count+1
                            break

                        # 2--mark  count as incorrect spelling
                        elif choice_correct == str(2):
                            error_count += 1
                            words_object[wordcount-1] = f"?{word}?"
                            print(word)
                            break

                        # 3--add to txt   count as correct
                        elif choice_correct == str(3):
                            correct_count += 1
                            added_count += 1
                            with open("EnglishWords.txt", "a") as file_source:
                                file_source.write("\n" + word )
                            break

                        # 4--give a suggestion
                        elif choice_correct == str(4):

                            # calculate similarity
                            similarity = []
                            for word_s in words_source:
                                from difflib import SequenceMatcher
                                score = SequenceMatcher(None, word, word_s) .ratio()
                                similarity.append(score)

                            # give the suggestion - most similar
                            print(f"Do you mean {words_source[similarity.index(max(similarity))]} ?")
                            while True:
                                print("╔══ ╳choice suggestion╳ ══╗")
                                print("║0. reject the suggestion ║")
                                print("║1. accept the suggestion ║")
                                print("╚═════════════════════════╝")
                                choice_suggestion = input("Please choose:")

                                # 0--reject
                                if choice_suggestion == str(0):
                                    error_count += 1
                                    break
                                # if 1--accept
                                elif choice_suggestion == str(1):
                                    correct_count += 1
                                    changed_count += 1
                                    words_object[wordcount - 1] = f"{words_source[similarity.index(max(similarity))]}"
                                    break
                                else:
                                    print(f"Sorry, {choice_suggestion} is not a valid input, please try again.")
                                    continue
                            break
                        else:
                            print(f"Sorry, {choice_correct} is not a valid input.")
                            continue
        # creating summary
        print("Generating a new file,please wait...")
        wordcount_output = "Total word count: " + str(wordcount)
        correct_output = "Correct spelling count: " + str(correct_count)
        error_output = "Error spelling count: " + str(error_count)
        add_output = "Adding to list: " + str(added_count)
        change_output = "changed by suggestion: " + str(changed_count)

        localtime = "Localtime: " + time.asctime(time.localtime(time.time()))
        end = time.time()
        time_output = "Total time taken: " + str(end-start) + " s"

        new_file = input("Please input the name of new file: ")
        count = wordcount_output + "\n" + correct_output + "\n" + error_output + "\n" +\
            add_output + "\n" + change_output
        time_ = localtime + "\n" + time_output
        new_content = " ".join(words_object)
        full_text = count + "\n" + time_ + "\n\n" + new_content

        # create a new file
        def txt(name, text):
            file = open(name + ".txt", "w")
            file.write(text)

        txt(new_file, full_text)

        print("The spell checking has been finished. You can quit or back to main menu.")
        while True:
            print("╔═════ ╳final menu╳ ═════╗")
            print("║0. quit                 ║")
            print("║1. back to the main menu║")
            print("╚════════════════════════╝")
            choice_final = input("Please choose: ")

        # final choice-- quit or go back to the main menu

            if choice_final == str(0):
                print("Thanks for using, good bye!")
                exit()

            # 1-- go back to the main menu.
            elif choice_final == str(1):
                break

            else:
                print(f"Sorry, ' {choice_final} '  is not a valid input.")
                continue

    # wrong input
    else:
        print(f"Sorry, ' {choice_start} ' is not a valid input, please try again.")
        continue
