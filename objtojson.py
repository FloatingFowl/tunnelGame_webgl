for iter in range(1,13):
    fname = "tunlay" + str(iter) + ".obj"
    content = []

    with open(fname) as f:
        content = f.readlines()
        content = [x.strip() for x in content] 

    vnum = 0
    fnum = 0
    nnum = 0
    vertices = []
    normals = []
    faces = []

    for i in range(len(content)):
        if content[i][0:2] == "v ":
            vnum += 1
            vln = content[i].split(' ')
            vertices.append([vln[1], vln[2], vln[3]])
        elif content[i][0:2] == "vn":
            nnum += 1
            vln = content[i].split(' ')
            normals.append([vln[1], vln[2], vln[3]])
        elif content[i][0:2] == "f ":
            fnum += 1
            vln = content[i].split(' ')
            faces.append([int((vln[1].split('//'))[0]) - 1, int((vln[2].split('//'))[0])-1, int((vln[3].split('//'))[0])-1])

    vpStr = '['
    vnStr = '['
    for i in range(vnum):
        vpStr += vertices[i][0] + ','
        vpStr += vertices[i][1] + ','
        vpStr += vertices[i][2] + ','

# for _ in range(2):
    for i in range(vnum):
        j = i % nnum
        vnStr += normals[j][0] + ','
        vnStr += normals[j][1] + ','
        vnStr += normals[j][2] + ','

    fnum /= 2
    vtStr = '['
    inStr = '['

    for i in range(fnum):
        seto = set()
        inStr += str(faces[i][0]) + ', ' + str(faces[i][2]) + ', ' + str(faces[i][1]) + ', '
        inStr += str(faces[i + fnum][2]) + ', ' + str(faces[i + fnum][1]) + ', ' + str(faces[i + fnum][0]) + ','

        seto.add(faces[i][0])
        seto.add(faces[i][1])
        seto.add(faces[i][2])
        seto.add(faces[i + fnum][0])
        seto.add(faces[i + fnum][1])
        seto.add(faces[i + fnum][2])

        # for j in seto:
            # vpStr += vertices[j][0] + ', '
            # vpStr += vertices[j][1] + ', '
            # vpStr += vertices[j][2] + ', '
        # for j in range(4):
            # vnStr += normals[i][0] + ', '
            # vnStr += normals[i][1] + ', '
            # vnStr += normals[i][2] + ', '
        vtStr += '0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0,'

    vpStr = vpStr[:-1] + ']'
    vnStr = vnStr[:-1] + ']'
    vtStr = vtStr[:-1] + ']'
    inStr = inStr[:-1] + ']'

    with open('tube' + str(iter) + '.json', 'a') as f:
        f.write('{');
        f.write('"vertexPositions" : ' + vpStr + ',')
        f.write('"vertexNormals" : ' + vnStr + ',')
        f.write('"vertexTextureCoords" : ' + vtStr + ',')
        f.write('"indices" : ' + inStr + '')
        f.write('}');
