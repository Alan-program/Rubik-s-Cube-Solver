#located：新k
def color_detect(b,g,r): 
    if (b>=0 and b<=63) and (g>=0 and g<=43) and (r>=120 and r<=168):
        return 'red'
    if (b>=0 and b<=44) and (g>=43 and g<=72) and (r>=173 and r<=223):
         return 'orange'
    if (b>=0 and b<=59) and (g>=111 and g<=195) and (r>=125 and r<=190):
        return 'yellow'   
    if (b>=16 and b<=64) and (g>=118 and g<=182) and (r>=0 and r<=59):
        return 'green'
    if (b>=21 and b<=104) and (g>=0 and g<=59) and (r>=0 and r<=39):
        return 'blue'
    if (b>=25 and b<=137) and (g>=129 and g<=162) and (r>=140 and r<=172):
        return 'white'
    
    return 'white'

# located：空間資訊教室
# def color_detect(b,g,r): 
#     if (b>=24 and b<=80) and (g>=26 and g<=64) and (r>=67 and r<=255):
#         return 'red'
#     if (b>=26 and b<=109) and (g>=66 and g<=105) and (r>=119 and r<=255):
#          return 'orange'
#     if (b>=0 and b<=49) and (g>=101 and g<=225) and (r>=154 and r<=210):
#         return 'yellow'   
#     if (b>=8 and b<=166) and (g>=98 and g<=255) and (r>=0 and r<=67):
#         return 'green'
#     if (b>=96 and b<=255) and (g>=0 and g<=120) and (r>=0 and r<=69):
#         return 'blue'
#     if (b>=158 and b<=206) and (g>=159 and g<=226) and (r>=152 and r<=210):
#         return 'white'
    
#     return 'white'

