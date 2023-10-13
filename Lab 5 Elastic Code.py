#### All code is an edited version of code from https://github.com/Dana-physicsLabs/PH1110-1111/tree/master/PythonCode. 
#### Some code is edited to fit my experiment.

### 1: velocity
v_Ai = 0.2410 #initial velocity (from statistics analysis of velocity graph)
dv_Ai = 0.0006224 #uncertainty of "

v_Bi = -0.2206 #cart B at rest at beginning
dv_Bi = 0.004427

v_Af = -0.1427   #final velocity (from statistics analysis of velocity graph)
dv_Af = 0.004414 #uncertainty of "

v_Bf = 0.1815 
dv_Bf = 0.003027 

### 2: mass
mA = 0.5008 #measured mass of the cart in kg
dmA = 0.001 #uncertainty in "

mB = 0.4989
dmB = 0.001

### 3: Kinetic Energy for Elastic
ke_Ai = .5*(mA * v_Ai * v_Ai) #initial kinetic energy of cart A
ke_Bi = .5*(mB * v_Bi * v_Bi) #initial kinetic energy of cart B

dke_Ai = ke_Ai * ((dmA/mA)+(2*((dv_Ai)/abs(v_Ai)))) #uncertainty in ke_Ai
dke_Bi = ke_Bi * ((dmB/mB)+(2*((dv_Bi)/abs(v_Bi)))) #uncertainty in ke_Bi
#Some notes on the above equation

#^^if only 1 cart (cart 1) is moving



#Don't need to do absolute value of m because it's already positive
# dm/m here is essentially dx/abs(x) as written in eq. 4 in Lab 1R
# that means (dv_A0+dv_B0)/abs(v_A0+v_B0))) corresponds to dy/abs(y) " 
# p_0 corresponds to abs(A) in eq. 4 in Lab 1R. 

#This is for Elastic KE calculation 

ke_Af = .5*((mA) * v_Af * v_Af) #final kinetic energy of cart A
ke_Bf = .5*((mB) * v_Bf * v_Bf) #final kinetic energy of cart B

dke_Af = ke_Af * ((dmA/mA)+((dv_Af)/abs(v_Af))) #uncertainty in final kinetic energy of cart A
dke_Bf = ke_Bf * ((dmB/mB)+((dv_Bf)/abs(v_Bf)))

print("Intial Elastic Kinetic Energy of Cart A:",ke_Ai,"±",dke_Ai," Joules") #print the intial 
#kinetic energy and its uncertainty
print("Intial Elastic Kinetic Energy of Cart B:",ke_Bi,"±",dke_Bi," Joules") #print the intial 
#kinetic energy and its uncertainty

print("Final Elasitc Kinetic Energy of Cart A:",ke_Af,"±",dke_Af," Joules") #print the final
#kinetic energy and its uncertainty
print("Final Elasitc Kinetic Energy of Cart B:",ke_Bf,"±",dke_Bf," Joules") #print the final
#kinetic energy and its uncertainty

### 4: Momentum
p_Ai = (mA * v_Ai) #initial momentum of the cart A
dp_Ai = p_Ai * ((dmA/mA)+((dv_Ai)/abs(v_Ai))) #uncertainty in "
#Some notes on the above equation
p_Bi = (mB * v_Bi) #initial momentum of the cart B
dp_Bi = p_Bi * ((dmB/mB)+((dv_Bi)/abs(v_Bi))) #uncertainty in "

#Don't need to do absolute value of m because it's already positive
# dm/m here is essentially dx/abs(x) as written in eq. 4 in Lab 1R
# that means (dv_A0+dv_B0)/abs(v_A0+v_B0))) corresponds to dy/abs(y) " 
# p_0 corresponds to abs(A) in eq. 4 in Lab 1R. 

p_Af = (mA * v_Af) #final momentum of the cart A
dp_Af = p_Af * ((dmA/mA)+((dv_Af)/abs(v_Af))) #uncertainty in "
p_Bf = (mB * v_Bf) #final momentum of the cart B
dp_Bf = p_Bf * ((dmB/mB)+((dv_Bf)/abs(v_Bf))) #uncertainty in "

print("\ninitial momentum of A:", p_Ai,"±",dp_Ai," kg * m/s") #print the momentum
print("initial momentum of B:", p_Bi,"±",dp_Bi," kg * m/s") #print the momentum

print("final momentum of A:", p_Af,"±",dp_Af," kg * m/s") #print the momentum
print("final momentum of B:", p_Bf,"±",dp_Bf," kg * m/s") #print the momentum