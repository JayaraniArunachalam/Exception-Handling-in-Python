try:
    with open("Read the numbers","r") as f:
        lines = f.readlines()
        if not lines:
            print("The file is empty.")
        else:
            print("File Contents")
            for line in lines:
                print (line)
        print("The numbers in the file are:")
        for line in lines:
            words = line.strip().split()
            for word in words:
                try:
                    number = float(word)  # can handle both int and float
                    print(number)
                except ValueError:
                    continue
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Unexpected error:", e)
