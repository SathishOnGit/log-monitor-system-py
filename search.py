def search_logs(file_path, keyword):

    with open(file_path, "r") as file:

        for line in file:

            if keyword.lower() in line.lower():
                print(line.strip())