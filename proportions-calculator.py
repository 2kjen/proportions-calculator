def main():
    print(''' 
    Proportions Calculator by Jennifer B.
    
    You have an image you need to resize & you want to keep the image's proportions.
    When you change either the width or the height of an object,
    the proportions calculator will tell you what the length of the other dimension
    should be if you want to maintain the current proportion.  
    This calculator only works with integers.
    
    ''')

    while True:  # Main program loop
        print("""What is the width of the image you would like to resize?"
        Input an integer without a unit of measurement.""")
        try:
            old_width = int(input("> "))
        except (ValueError, TypeError):
            print("Please enter integers (a.k.a. whole numbers) only!")
            old_width = int(input("> "))

        print("""What is the length of the image you would like to resize? 
        Input an integer without a unit of measurement.""")
        try:
            old_length = int(input("> "))
        except (ValueError, TypeError):
            print("Please enter integers (a.k.a. whole numbers) only!")
            old_length = int(input("> "))

        ratio = old_width / old_length

        print("""What dimension would you like to change?
        
        For width, type 'w' or 'width'. For length, type 'l' or 'length'.
        Don't include the quotation marks!""")
        changed_dimension = input("> ")
        while changed_dimension not in ('w', 'width', 'l', 'length'):
            print("""Please enter 'w' or 'width' for width (without the quotation marks),
            or enter 'l' or 'length' for length (again, without quotation marks).""")
            changed_dimension = input("> ")

        if changed_dimension in ('w', 'width'):
            print("What would you like to change the width to?")
            try:
                new_width = int(input("> "))
            except (ValueError, TypeError):
                print("Please enter integers (a.k.a. whole numbers) only!")
                new_width = int(input("> "))
            new_length = int(new_width / ratio)
            print("Your new length should be: %i" % new_length)

        elif changed_dimension in ('l', 'length'):
            print("What would you like to change the length to?")
            try:
                new_length = int(input("> "))
            except (ValueError, TypeError):
                print("Please enter integers (a.k.a. whole numbers) only!")
                new_length = int(input("> "))
            new_width = int(new_length * ratio)
            print("Your new width should be: %i" % new_width)

        else:
            print(""" O-oh! It looks like there's been an error somewhere!
            If you want to change the width: type 'w' or 'width' without the quotation marks.
            If you want to change the length: type 'l' or 'length' without the quotation marks.""")

        print("Would you like to reuse the Proportions Calculator?")
        if not input("> ").startswith('y'):
            print("Thanks for using the Proportions Calculator!")
            break


if __name__ == '__main__':
    main()
