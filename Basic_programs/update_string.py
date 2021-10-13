###
# Update the string
###


def update_script(str1):
    print("Original script:  -", str1)
    print("Updated script: -", str1[:6] + 'John')




if __name__ == "__main__":
    str1 = "Hello Python"
    update_script(str1)