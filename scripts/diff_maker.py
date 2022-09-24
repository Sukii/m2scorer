import sys
import difflib


# read original sentences into array
original_file = open(sys.argv[1], "r")
original = original_file.readlines()
original_file.close()

# read modified sentences into array
modified_file = open(sys.argv[2], "r")
edited = modified_file.readlines()
modified_file.close()

# original sentences
#original = ["The birds in this forest is singing beautifuly","Another sentence with error in punctiation"]

# corrected sentences
#edited = ["The birds in this forest are singing beautifully","Another sentence, with an error in punctuation"]

# initiate the Differ object
d = difflib.Differ()

for i in range(0,len(original)):
    print(original[i].rstrip())
    # calculate the difference between the two sentences
    diff = list(d.compare(original[i].rstrip().split(), edited[i].rstrip().split()))
    type = "unknown"
    i = 0
    for word in diff:
        if word[:1] == "+":
            print("A", i,i+1, "|||" + type + "|||" + word[1:] + "|||REQUIRED|||-NONE-|||0")
        if word[:1] == " " or word[:1] == "+" :
            i=i+1
    print("")
