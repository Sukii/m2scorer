import difflib

# define original text
original = ["The birds in this forest is singing beautifuly","Another sentence with error in punctiation"]

# define modified text
edited = ["The birds in this forest are singing beautifully","Another sentence, with an error in punctuation"]

# initiate the Differ object
d = difflib.Differ()

for i in range(0,len(original)):
    print(original[i])
    # calculate the difference between the two texts
    diff = list(d.compare(original[i].split(), edited[i].split()))
    type = "unknown"
    i = 0
    for word in diff:
        if word[:1] == "+":
            print("A", i,i+1, "|||" + type + "|||" + word[1:] + "|||REQUIRED|||-NONE-|||0")
        if word[:1] == " " or word[:1] == "+" :
            i=i+1
    print("")
