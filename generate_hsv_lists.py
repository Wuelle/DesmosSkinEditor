from PIL import Image
import math
import sys

if len(sys.argv) < 2:
    print("Please specify the skin file to use, like this:")
    print(f"> python3 {sys.argv[0]} path/to/your/skin.png")
    exit(1)

img = Image.open(sys.argv[1])
img_hsv=img.convert('hsv')
width, height = img.size

H=[0]*4096
S=[0]*4096
V=[0]*4096
j=0
for x in range(0, width):
        for y in range(0, height):
                h, s, v = img_hsv.getpixel((x, y))
                H[j] = h
                S[j] = s
                V[j] = v
                j=j+1

K_HF=[519+i-8*math.floor((i-1)/8)+64*math.floor((i-1)/8) for i in range(1, 65)]
K_HL=[7+i-8*math.floor((i-1)/8)+64*math.floor((i-1)/8) for i in range(1, 65)]
K_HR=[1031+i-8*math.floor((i-1)/8)+64*math.floor((i-1)/8) for i in range(1, 65)]
K_HT=[511+i-8*math.floor((i-1)/8)+64*math.floor((i-1)/8) for i in range(1, 65)]
K_HB=[1023+i-8*math.floor((i-1)/8)+64*math.floor((i-1)/8) for i in range(1, 65)]
K_HBa=[1543+i-8*math.floor((i-1)/8)+64*math.floor((i-1)/8) for i in range(1, 65)]

K_TF=[1299+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 97)]
K_TL=[1043+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_TR=[1811+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_TT=[1295+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 33)]
K_TB=[1807+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 33)]
K_TBa=[2067+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 97)]

K_LAF=[2835+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_LAL=[2579+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_LAR=[3091+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_LABa=[3347+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_LAT=[2831+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 17)]
K_LAB=[3087+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 17)]

K_RAF=[2355+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_RAL=[2099+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_RAR=[2611+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_RABa=[2867+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_RAT=[2351+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 17)]
K_RAB=[2607+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 17)]

K_LLF=[275+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_LLL=[19+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_LLR=[531+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_LLBa=[787+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_LLT=[271+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 17)]
K_LLB=[527+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 17)]

K_RLF=[1331+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_RLL=[1075+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_RLR=[1587+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_RLBa=[1843+i-12*math.floor((i-1)/12)+64*math.floor((i-1)/12) for i in range(1, 49)]
K_RLT=[1327+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 17)]
K_RLB=[1583+i-4*math.floor((i-1)/4)+64*math.floor((i-1)/4) for i in range(1, 17)]


H_HF = [H[K_HF[j]] for j in range(0, 64)]
S_HF = [S[K_HF[j]] for j in range(0, 64)]
V_HF = [V[K_HF[j]] for j in range(0, 64)]

H_HL = [H[K_HL[j]] for j in range(0, 64)]
S_HL = [S[K_HL[j]] for j in range(0, 64)]
V_HL = [V[K_HL[j]] for j in range(0, 64)]

H_HR = [H[K_HR[j]] for j in range(0, 64)]
S_HR = [S[K_HR[j]] for j in range(0, 64)]
V_HR = [V[K_HR[j]] for j in range(0, 64)]

H_HT = [H[K_HT[j]] for j in range(0, 64)]
S_HT = [S[K_HT[j]] for j in range(0, 64)]
V_HT = [V[K_HT[j]] for j in range(0, 64)]

H_HB = [H[K_HB[j]] for j in range(0, 64)]
S_HB = [S[K_HB[j]] for j in range(0, 64)]
V_HB = [V[K_HB[j]] for j in range(0, 64)]

H_HBa = [H[K_HBa[j]] for j in range(0, 64)]
S_HBa = [S[K_HBa[j]] for j in range(0, 64)]
V_HBa = [V[K_HBa[j]] for j in range(0, 64)]

H_TF = [H[K_TF[j]] for j in range(0, 96)]
S_TF = [S[K_TF[j]] for j in range(0, 96)]
V_TF = [V[K_TF[j]] for j in range(0, 96)]

H_TL = [H[K_TL[j]] for j in range(0, 48)]
S_TL = [S[K_TL[j]] for j in range(0, 48)]
V_TL = [V[K_TL[j]] for j in range(0, 48)]

H_TR = [H[K_TR[j]] for j in range(0, 48)]
S_TR = [S[K_TR[j]] for j in range(0, 48)]
V_TR = [V[K_TR[j]] for j in range(0, 48)]

H_TT = [H[K_TT[j]] for j in range(0, 32)]
S_TT = [S[K_TT[j]] for j in range(0, 32)]
V_TT = [V[K_TT[j]] for j in range(0, 32)]

H_TB = [H[K_TB[j]] for j in range(0, 32)]
S_TB = [S[K_TB[j]] for j in range(0, 32)]
V_TB = [V[K_TB[j]] for j in range(0, 32)]

H_TBa = [H[K_TBa[j]] for j in range(0, 96)]
S_TBa = [S[K_TBa[j]] for j in range(0, 96)]
V_TBa = [V[K_TBa[j]] for j in range(0, 96)]

H_LAF = [H[K_LAF[j]] for j in range(0, 48)]
S_LAF = [S[K_LAF[j]] for j in range(0, 48)]
V_LAF = [V[K_LAF[j]] for j in range(0, 48)]

H_LAL = [H[K_LAL[j]] for j in range(0, 48)]
S_LAL = [S[K_LAL[j]] for j in range(0, 48)]
V_LAL = [V[K_LAL[j]] for j in range(0, 48)]

H_LAR = [H[K_LAR[j]] for j in range(0, 48)]
S_LAR = [S[K_LAR[j]] for j in range(0, 48)]
V_LAR = [V[K_LAR[j]] for j in range(0, 48)]

H_LABa = [H[K_LABa[j]] for j in range(0, 48)]
S_LABa = [S[K_LABa[j]] for j in range(0, 48)]
V_LABa = [V[K_LABa[j]] for j in range(0, 48)]

H_LAT = [H[K_LAT[j]] for j in range(0, 16)]
S_LAT = [S[K_LAT[j]] for j in range(0, 16)]
V_LAT = [V[K_LAT[j]] for j in range(0, 16)]

H_LAB = [H[K_LAB[j]] for j in range(0, 16)]
S_LAB = [S[K_LAB[j]] for j in range(0, 16)]
V_LAB = [V[K_LAB[j]] for j in range(0, 16)]

H_RAF = [H[K_RAF[j]] for j in range(0, 48)]
S_RAF = [S[K_RAF[j]] for j in range(0, 48)]
V_RAF = [V[K_RAF[j]] for j in range(0, 48)]

H_RAL = [H[K_RAL[j]] for j in range(0, 48)]
S_RAL = [S[K_RAL[j]] for j in range(0, 48)]
V_RAL = [V[K_RAL[j]] for j in range(0, 48)]

H_RAR = [H[K_RAR[j]] for j in range(0, 48)]
S_RAR = [S[K_RAR[j]] for j in range(0, 48)]
V_RAR = [V[K_RAR[j]] for j in range(0, 48)]

H_RABa = [H[K_RABa[j]] for j in range(0, 48)]
S_RABa = [S[K_RABa[j]] for j in range(0, 48)]
V_RABa = [V[K_RABa[j]] for j in range(0, 48)]

H_RAT = [H[K_RAT[j]] for j in range(0, 16)]
S_RAT = [S[K_RAT[j]] for j in range(0, 16)]
V_RAT = [V[K_RAT[j]] for j in range(0, 16)]

H_RAB = [H[K_RAB[j]] for j in range(0, 16)]
S_RAB = [S[K_RAB[j]] for j in range(0, 16)]
V_RAB = [V[K_RAB[j]] for j in range(0, 16)]

H_LLF = [H[K_LLF[j]] for j in range(0, 48)]
S_LLF = [S[K_LLF[j]] for j in range(0, 48)]
V_LLF = [V[K_LLF[j]] for j in range(0, 48)]

H_LLL = [H[K_LLL[j]] for j in range(0, 48)]
S_LLL = [S[K_LLL[j]] for j in range(0, 48)]
V_LLL = [V[K_LLL[j]] for j in range(0, 48)]

H_LLR = [H[K_LLR[j]] for j in range(0, 48)]
S_LLR = [S[K_LLR[j]] for j in range(0, 48)]
V_LLR = [V[K_LLR[j]] for j in range(0, 48)]

H_LLBa = [H[K_LLBa[j]] for j in range(0, 48)]
S_LLBa = [S[K_LLBa[j]] for j in range(0, 48)]
V_LLBa = [V[K_LLBa[j]] for j in range(0, 48)]

H_LLT = [H[K_LLT[j]] for j in range(0, 16)]
S_LLT = [S[K_LLT[j]] for j in range(0, 16)]
V_LLT = [V[K_LLT[j]] for j in range(0, 16)]

H_LLB = [H[K_LLB[j]] for j in range(0, 16)]
S_LLB = [S[K_LLB[j]] for j in range(0, 16)]
V_LLB = [V[K_LLB[j]] for j in range(0, 16)]

H_RLF = [H[K_RLF[j]] for j in range(0, 48)]
S_RLF = [S[K_RLF[j]] for j in range(0, 48)]
V_RLF = [V[K_RLF[j]] for j in range(0, 48)]

H_RLL = [H[K_RLL[j]] for j in range(0, 48)]
S_RLL = [S[K_RLL[j]] for j in range(0, 48)]
V_RLL = [V[K_RLL[j]] for j in range(0, 48)]

H_RLR = [H[K_RLR[j]] for j in range(0, 48)]
S_RLR = [S[K_RLR[j]] for j in range(0, 48)]
V_RLR = [V[K_RLR[j]] for j in range(0, 48)]

H_RLBa = [H[K_RLBa[j]] for j in range(0, 48)]
S_RLBa = [S[K_RLBa[j]] for j in range(0, 48)]
V_RLBa = [V[K_RLBa[j]] for j in range(0, 48)]

H_RLT = [H[K_RLT[j]] for j in range(0, 16)]
S_RLT = [S[K_RLT[j]] for j in range(0, 16)]
V_RLT = [V[K_RLT[j]] for j in range(0, 16)]

H_RLB = [H[K_RLB[j]] for j in range(0, 16)]
S_RLB = [S[K_RLB[j]] for j in range(0, 16)]
V_RLB = [V[K_RLB[j]] for j in range(0, 16)]

H_0=H_HF+H_HL+H_HR+H_HT+H_HB+H_HBa+H_TF+H_TBa+H_TL+H_TR+H_TT+H_TB+H_LAF+H_LAL+H_LAR+H_LABa+H_LAT+H_LAB+H_RAF+H_RAL+H_RAR+H_RABa+H_RAT+H_RAB+H_LLF+H_LLL+H_LLR+H_LLBa+H_LLT+H_LLB+H_RLF+H_RLL+H_RLR+H_RLBa+H_RLT+H_RLB
S_0=S_HF+S_HL+S_HR+S_HT+S_HB+S_HBa+S_TF+S_TBa+S_TL+S_TR+S_TT+S_TB+S_LAF+S_LAL+S_LAR+S_LABa+S_LAT+S_LAB+S_RAF+S_RAL+S_RAR+S_RABa+S_RAT+S_RAB+S_LLF+S_LLL+S_LLR+S_LLBa+S_LLT+S_LLB+S_RLF+S_RLL+S_RLR+S_RLBa+S_RLT+S_RLB
V_0=V_HF+V_HL+V_HR+V_HT+V_HB+V_HBa+V_TF+V_TBa+V_TL+V_TR+V_TT+V_TB+V_LAF+V_LAL+V_LAR+V_LABa+V_LAT+V_LAB+V_RAF+V_RAL+V_RAR+V_RABa+V_RAT+V_RAB+V_LLF+V_LLL+V_LLR+V_LLBa+V_LLT+V_LLB+V_RLF+V_RLL+V_RLR+V_RLBa+V_RLT+V_RLB

print(H_0)
print(S_0)
print(V_0)
