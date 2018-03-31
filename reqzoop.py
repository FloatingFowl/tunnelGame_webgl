for i in range(7,13):
    print "var req" + str(i) + " = new XMLHttpRequest();"
    print "req" + str(i) + ".open('GET', 'tube" + str(i) + ".json');"
    print "req" + str(i) + ".onreadystatechange = function () {"
    print "    if (req" + str(i) + ".readyState == 4) {"
    print "        handleLoadedTeapot(JSON.parse(req" + str(i) + ".responseText));"
    print "}}"
    print "req" + str(i) + ".send();"
