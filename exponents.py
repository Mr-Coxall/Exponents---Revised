def exponent(value):
    # converts an integer number to superscript string

    if isinstance(value, int) is True:
        SUPER_SCRIPT = str.maketrans(
            "0123456789+-",
            "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u207A\u207B",
        )

        return str(value).translate(SUPER_SCRIPT)
    else:
        print("Oops!!  That was no valid integer.")
