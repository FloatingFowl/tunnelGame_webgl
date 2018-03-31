colours = ["cyan","magenta","lime","pink","teal","lavender"]
for i in range(len(colours)):
    print "textureCollection." + colours[i] + " = gl.createTexture();"
    print "textureCollection." + colours[i] + ".image = new Image();"
    print "textureCollection." + colours[i] + ".image.onload = function () {"
    print "    handleLoadedTexture(textureCollection." + colours[i] + ") }"
    print "textureCollection." + colours[i] + " = 'color_" + str(i+1) + ".jpg'\n"
