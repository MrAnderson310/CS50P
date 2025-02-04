#Take in a file and depending on what file type print out the media type of the file
def main():
    #Gets user input
    x = input("File Name: ")
    x = x.lower()
    #Checks which file extension the input ends in
    if x.endswith(".gif"):
        print("image/gif")
    elif x.endswith(".jpg") or x.endswith(".jpeg"):
        print("image/jpeg")
    elif x.endswith(".png"):
        print("image/png")
    elif x.endswith(".pdf"):
        print("application/pdf")
    elif x.endswith(".txt"):
        print("text/plain")
    elif x.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()