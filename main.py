from math import sqrt
stl_file = open("simple_block_ascii.stl", "r")
lines = stl_file.readlines()

buffer = []

'''The structure of buffer [] will be as follows
[facet data] comprises of [[normal data][vertices data]] ......] '''


for i in range(len(lines)):
    if "facet normal" in lines[i]:
        facet_data = []
        normal_data = []
        normal_data_str = lines[i].strip().split(" ")
        normal_data.append(float(normal_data_str[2].split("\n")[0]));
        normal_data.append(float(normal_data_str[3].split("\n")[0]));
        normal_data.append(float(normal_data_str[4].split("\n")[0]));
        facet_data.append(normal_data)

        vertex_data = []
        #two lines from current line i.e facet normal , we will have vertex data information.
        vertex_data_str_array = lines[i+2:i+5]
        for j in range(0,3):
            vertex_data_str = vertex_data_str_array[j].strip().split(" ")
            vertex_data.append(float(vertex_data_str[1].split("\n")[0]))
            vertex_data.append(float(vertex_data_str[2].split("\n")[0]))
            vertex_data.append(float(vertex_data_str[3].split("\n")[0]))

        facet_data.append(vertex_data)
        buffer.append(facet_data)

print("Number of facets = ", len(buffer))
area = 0.0
volume = 0.0

#computation of area begins.
#traverse each facet data present in buffer that contains normal data and vertex data.
for i in range(len(buffer)):
    vect1 = []
    vect2 = []
    vect1 = [buffer[i][1][0] - buffer[i][1][3] , buffer[i][1][1]-buffer[i][1][4], buffer[i][1][2]-buffer[i][1][5]]
    vect2 = [buffer[i][1][0] - buffer[i][1][6] , buffer[i][1][1]-buffer[i][1][7], buffer[i][1][2]-buffer[i][1][8]]

    cx = (vect1[1] * vect2[2]) - (vect1[2] * vect2[1])
    cy = (vect1[2] * vect2[0]) - (vect1[0] * vect2[2])
    cz = (vect1[0] * vect2[1]) - (vect1[1] * vect2[0])

    area += sqrt((pow(cx,2))+ (pow(cy,2)) + (pow(cz,2))) * 0.5
    #from cross product magnitude we get the area of parlellogram formed by two be vectors
    #to compute the area of triangle, we scale it to 0.5


print(f"Area of the stl file is :{area}")

#computation of area ends...

#computation of volume begins
#traverse each facet data present in buffer that contains normal data and vertex data.
#use gauss divergence theorem and compute the volume of tesselated file assuming it as closed volume.
#volume = summation(tess1stpt.(normal * Area))/3.0
for i in range(len(buffer)):
    vect1 = []
    vect2 = []

    vect1 = [buffer[i][1][0] - buffer[i][1][3] , buffer[i][1][1]-buffer[i][1][4], buffer[i][1][2]-buffer[i][1][5]]
    vect2 = [buffer[i][1][0] - buffer[i][1][6] , buffer[i][1][1]-buffer[i][1][7], buffer[i][1][2]-buffer[i][1][8]]

    cx = (vect1[1] * vect2[2]) - (vect1[2] * vect2[1])
    cy = (vect1[2] * vect2[0]) - (vect1[0] * vect2[2])
    cz = (vect1[0] * vect2[1]) - (vect1[1] * vect2[0])


    area_of_tess = sqrt((pow(cx,2))+ (pow(cy,2)) + (pow(cz,2))) * 0.5
    
    scaled_normal = [area_of_tess*buffer[i][0][j] for j in range(len(buffer[i][0]))]

    for j in range(len(scaled_normal)):
        volume += buffer[i][1][j] * scaled_normal[j]

volume = volume*(1.0/3.0)
print(f"Volume of the stl file is:{volume}")
