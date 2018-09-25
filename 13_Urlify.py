#replace spaces with %20

def spacer(s1):
    if " " not in s1:
        return s1;
    s2 = s1.replace(" ", "%20");
    return s2;

print(spacer('glen'));
print(spacer(' gl e n'))

