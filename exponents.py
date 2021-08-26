def exponent(value):
    # converts an integer number to superscript string
    value_str = str(value)
    superscripts = {
        u"0": u"\u2070",
        u"1": u"\u00b9",
        u"2": u"\u00b2",
        u"3": u"\u00b3",
        u"4": u"\u2074",
        u"5": u"\u2075",
        u"6": u"\u2076",
        u"7": u"\u2077",
        u"8": u"\u2078",
        u"9": u"\u2079",
        u"+": u"\u207A",
        u"-": u"\u207B",
    }

    if isinstance(value, int) is True:
        return "".join(
            [superscripts[loop_counter] for loop_counter in value_str]
        )
    else:
        print("Oops!!  That was no valid integer.")
