
filename = input("Enter the name of the file to open: ")
    
try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File Content: {content}")
            print(content)
            
except FileNotFoundError:
        # 1.1) Handle case where file does not exist
        print("Error: The file was not found. Please check the path.")
        
except PermissionError:
        # 2.2) Handle case where permissions are lacking
        print("Error: Permission denied. You do not have access.")
        
except Exception as e:
        # Catch-all for any other unexpected errors
        print("An unexpected error occurred")

