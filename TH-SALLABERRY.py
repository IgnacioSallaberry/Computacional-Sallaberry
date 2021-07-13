# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:18:45 2021

@author: Ignacio Sallaberry
"""
import matplotlib.pyplot as plt
import numpy as np
import random
import re
from scipy import stats
#%%
#==================================================================================================
#                            Obtengo las palabras de los libros en español y en alemán
#==================================================================================================

def palabras_del_libro(name):
    with open(name) as fobj:
        libro = fobj.read()
    lineas = re.split('\n', libro)

    palabra=[]    
    for linea in lineas:
        i=0
        linea = re.sub(r'[^\w\s]','',linea) #esto saca todos los signos de puntuación. Si no los saco, el largo de la palabra va a cambiar.
        while i<len(linea.split()):
            palabra.append(linea.split()[i])
            i+=1
    return palabra

path = r'C:\Users\ETCasa\Desktop\MEFE\Computacionales\Computacional' #carpeta con los txt de los libros.

palabras_ES = palabras_del_libro(path + r'\text_es.txt')
palabras_AL = palabras_del_libro(path + r'\text_al.txt')

#%%
#==================================================================================================
#      Comparación entre tomar todas las palabras, o elegirlas al azar. (considerando igual numero de entradas)
#==================================================================================================

t_1_ES = []#numero de letras en cada palabra
for p in palabras_ES:
    t_1_ES.append(len(p))


t_1_ES_azar=[]
i=0
while i<len(palabras_ES):
    t_1_ES_azar.append(len(random.choice(palabras_ES)))
    i+=1


figure, ax = plt.subplots(figsize=(7,6), dpi=300)

bins = np.arange(0,20,1)
h,b = np.histogram(t_1_ES,bins,density=True)
error1 = np.sqrt(h/len(t_1_ES))
ax.bar(b[:-1],height=h,width =1,color='pink',edgecolor='deeppink', ecolor='crimson',yerr=error1,capsize=4, label='NO azar')


h1,b1 = np.histogram(t_1_ES_azar,bins,density=True)
error2 = np.sqrt(h1/len(t_1_ES_azar))
ax.bar(b1[:-1],height=h1 ,width =0.5,color='yellow',edgecolor='gold', ecolor='goldenrod', yerr=error2,capsize=4, alpha=0.5, label='azar')

ax.set_title('Distribución del estadístico $t_{1-ES}$')
ax.legend()
ax.set_xlabel('Longitud')
ax.set_ylabel('Probabilidad')
ax.set_xticks(bins)

figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
figManager.window.showMaximized()           ####   esto y la linea de arriba me maximiza la ventana de la figura
plt.show()



#%%

#==============================================================================
#                            PUNTO 1
#==============================================================================
####
#               Distribución t1
###
t_1_ES = []#numero de letras en cada palabra
for p in palabras_ES:
    t_1_ES.append(len(p))

    #Valor medio de t_1_ES
mean_ES = np.mean(t_1_ES)
#Mediana de t_ES
median_ES = np.median(t_1_ES)
#Moda de t_1_ES
mode_ES = stats.mode(t_1_ES)


t_1_AL = []#numero de letras en cada palabra
for p in palabras_AL:
    t_1_AL.append(len(p))
#Valor medio de t_1_AL
mean_AL = np.mean(t_1_AL)
#Mediana de t_AL
median_AL = np.median(t_1_AL)
#Moda de t_1_AL
mode_AL = stats.mode(t_1_AL)


figure, ax = plt.subplots(2,figsize=(3.3,3.3), dpi=200, sharey=True)

bins = np.arange(0,20,1)
h,b = np.histogram(t_1_ES,bins,density=True)
error1 = np.sqrt(h/len(t_1_ES))
ax[0].bar(b[:-1],height=h,width =1,color='pink',edgecolor='deeppink', ecolor='crimson',yerr=error1,capsize=4, label=r'$t_{1-ES}$')

ax[0].axvline(mean_ES,color='r', label='$media$ = {:.3f}'.format(mean_ES))
# ax[0].text(mean_ES+mean_ES*.03,0.1,s='$media$ = {:.3f}'.format(mean_ES), color='r',rotation=90)

ax[0].axvline(median_ES,color='r',linestyle='--', label='$mediana$ = {:.3f}'.format(median_ES))
# ax[0].text(median_ES-median_ES*.03,0.1,s='$mediana$ = {:.3f}'.format(mean_ES), color='r',rotation=90)

ax[0].axvline(mode_ES[0],color='r',linestyle='-.', label='$moda$ = {:.3f}'.format(mode_ES[0][0]))
# ax[0].text(mode_ES[0]+mode_ES[0]*.03,0.1,s='$moda$ = {:.3f}'.format(mode_ES[0]), color='r',rotation=90)


ax[0].set_title('Distribución del estadístico $t_{1-ES}$')
ax[0].set_xlabel('Longitud')
ax[0].set_ylabel('Probabilidad')
ax[0].set_xticks(bins)
ax[0].tick_params(which='minor', length=1.75, width=1)
ax[0].tick_params(which='major', length=3, width=1.25)
ax[0].legend()

h,b = np.histogram(t_1_AL,bins,density=True)
error1 = np.sqrt(h/len(t_1_AL))
ax[1].bar(b[:-1],height=h,width =1,color='skyblue',edgecolor='steelblue', ecolor='blue',yerr=error1,capsize=4, label=r'$t_{1-AL}$')
ax[1].axvline(mean_AL,color='r', label='$media$ = {:.3f}'.format(mean_AL))
ax[1].axvline(median_AL,color='r',linestyle='--', label='$mediana$ = {:.3f}'.format(median_AL))
ax[1].axvline(mode_AL[0],color='r',linestyle='-.', label='$moda$ = {:.3f}'.format(mode_AL[0][0]))

ax[1].set_title('Distribución del estadístico $t_{1-AL}$')
ax[1].set_xlabel('Longitud')
ax[1].set_ylabel('Probabilidad')
ax[1].set_xticks(bins)
ax[1].legend()
ax[1].tick_params(which='minor', length=1.75, width=1)
ax[1].tick_params(which='major', length=3, width=1.25)

figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
figManager.window.showMaximized()           ####   esto y la linea de arriba me maximiza la ventana de la figura
plt.show()


#%%

#==============================================================================
#                            PUNTO 2
#==============================================================================
#==============================================================================
#                            CALCULO LAS DISTRIBUCIONES DE t_20
#==============================================================================
t_20_ES = []
i=0
while i<len(t_1_ES):
    t_20_ES.append(max(random.sample(t_1_ES,20)))
    i+=1    

t_20_AL = []
i=0
while i<len(t_1_AL):
    t_20_AL.append(max(random.sample(t_1_AL,20)))
    i+=1    


figure, ax = plt.subplots(2,figsize=(3.3,3.3), dpi=200, sharey=True)

bins = np.arange(0,30,1)
h0,b0 = np.histogram(t_20_ES,bins,density=True)
error0 = np.sqrt(h0/len(t_20_ES))
ax[0].bar(b0[:-1],height=h0 ,width =1,color='navajowhite',edgecolor='peru', ecolor='sandybrown',yerr=error0,capsize=4, label=r'$t_{20-ES}$')

ax[0].set_title('Distribución del estadístico $t_{20-ES}$')
ax[0].set_xlabel('Longitud')
ax[0].set_ylabel('Probabilidad')
ax[0].set_xticks(bins)
ax[0].tick_params(which='minor', length=1.75, width=1)
ax[0].tick_params(which='major', length=3, width=1.25)
ax[0].legend()



h1,b1 = np.histogram(t_20_AL,bins,density=True)
error1 = np.sqrt(h1/len(t_20_AL))
ax[1].bar(b1[:-1],height=h1 ,width =1,color='paleturquoise',edgecolor='seagreen', ecolor='darkcyan',yerr=error1,capsize=4, label=r'$t_{20-AL}$')

ax[1].set_title('Distribución del estadístico $t_{20-AL}$')
ax[1].set_xlabel('Longitud')
ax[1].set_ylabel('Probabilidad')
ax[1].set_xticks(bins)
ax[1].legend()
ax[1].tick_params(which='minor', length=1.75, width=1)
ax[1].tick_params(which='major', length=3, width=1.25)

figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
figManager.window.showMaximized()           ####   esto y la linea de arriba me maximiza la ventana de la figura
plt.show()

#%%
#==============================================================================
#                            PUNTO 3
#==============================================================================
#==============================================================================
#                            Calculo el t_20_ES_ critico y lo pongo en el gráfico
#==============================================================================
i=0
p=0
while i<0.95:
    i+=h0[p]
    p+=1

significancia = 1-i
t_20_ES_C = p


figure, ax = plt.subplots(2,figsize=(3.3,3.3), dpi=200, sharey=True)

bins = np.arange(0,30,1)
h0,b0 = np.histogram(t_20_ES,bins,density=True)
error0 = np.sqrt(h0/len(t_20_ES))
ax[0].bar(b0[:-1],height=h0 ,width =1,color='navajowhite',edgecolor='peru', ecolor='sandybrown',yerr=error0,capsize=4, label=r'$t_{20-ES}$')

# ax[0].bar(b0[t_20_ES_C:-1],height=h0 ,width =1,color='navajowhite',edgecolor='peru', ecolor='sandybrown',yerr=error0,capsize=4, label=r'$t_{20-ES}$',  hatch="//")

ax[0].axvline(p,h0[p],color='r',linestyle='--', label='$t_{20-ES}^c = $'+'{:.1f}'.format(p))
ax[0].text(t_20_ES_C*1.01,h0[p]*5,s='$t_{20-ES}^c$', color='r',rotation=90)

ax[0].set_title('Distribución del estadístico $t_{20-ES}$')
ax[0].set_xlabel('Longitud')
ax[0].set_ylabel('Probabilidad')
ax[0].set_xticks(bins)
ax[0].tick_params(which='minor', length=1.75, width=1)
ax[0].tick_params(which='major', length=3, width=1.25)
ax[0].legend()



h1,b1 = np.histogram(t_20_AL,bins,density=True)
error1 = np.sqrt(h1/len(t_20_AL))
ax[1].bar(b1[:-1],height=h1 ,width =1,color='paleturquoise',edgecolor='seagreen', ecolor='darkcyan',yerr=error1,capsize=4, label=r'$t_{20-AL}$')

ax[1].axvline(p,h0[p],color='r',linestyle='--', label='$t_{20-ES}^c = $'+'{:.1f}'.format(p))
ax[1].text(t_20_ES_C*1.01,h0[p]*5,s='$t_{20-ES}^c$', color='r',rotation=90)


ax[1].set_title('Distribución del estadístico $t_{20-AL}$')
ax[1].set_xlabel('Longitud')
ax[1].set_ylabel('Probabilidad')
ax[1].set_xticks(bins)
ax[1].legend()
ax[1].tick_params(which='minor', length=1.75, width=1)
ax[1].tick_params(which='major', length=3, width=1.25)

figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
figManager.window.showMaximized()           ####   esto y la linea de arriba me maximiza la ventana de la figura
plt.show()


#%%
#==============================================================================
#                            PUNTO 4 - A
#==============================================================================
#==============================================================================
#                            Calculo la potencia del test considerando H1 
#==============================================================================

i=0
p=0
while p<t_20_ES_C:
    i+=h1[p]
    p+=1

potencia_t20 = 1-i


print(t_20_ES_C, potencia_t20)


#%%
#==============================================================================
#                            PUNTO 4 - B - Potencia de t_1
#==============================================================================
h,b = np.histogram(t_1_ES,bins,density=True)
i=0
p=0
while i<0.95:
    i+=h[p]
    p+=1
# i=i-h[p]
# print(1-i,p)
t_1_ES_C = p

h,b = np.histogram(t_1_AL,bins,density=True)
i=0
p=0
while p<t_1_ES_C:
    i+=h1[p]
    p+=1
# i=i-h[p]
# print(1-i,p)
potencia_t1 = 1-i

print(t_1_ES_C, potencia_t1)

#%%
#==============================================================================
#                            PUNTO 4 - C - Potencia de t_100
#==============================================================================
t_100_ES = []
i=0
while i<len(t_1_ES):
    t_100_ES.append(max(random.sample(t_1_ES,100)))
    i+=1    

t_100_AL = []
i=0
while i<len(t_1_AL):
    t_100_AL.append(max(random.sample(t_1_AL,100)))
    i+=1    



h,b = np.histogram(t_100_ES,bins,density=True)
i=0
p=0
while i<0.95:
    i+=h[p]
    p+=1
# i=i-h[p]
# print(1-i,p)
t_100_ES_C = p

h,b = np.histogram(t_100_AL,bins,density=True)
i=0
p=0
while p<t_100_ES_C:
    i+=h1[p]
    p+=1
potencia_t100 = 1-i

print(t_100_ES_C, potencia_t100)


#%%
#==============================================================================
#                            PUNTO 5 - Test de Runs
#==============================================================================
#==============================================================================
#                            Distribuciones de "rachas"
#==============================================================================

def estadistico_rachas(t):
    rachas = [] 
    p=0
    mediana = np.median(t)
    while p<5000:
        r1=random.choices(t, k=30)
        i=0
        r=0
        while i<len(r1)-1:
            if r1[i]<mediana<r1[i+1] or r1[i]>mediana>r1[i+1]: #Cumpleaños en febrero, entonces si es igual rechazo el valor. 
                r+=1
                i+=1
            else:
                i+=1
        rachas.append(r)
        p+=1
    
    return rachas

r_ES = estadistico_rachas(t_1_ES)
r_AL = estadistico_rachas(t_1_AL)


#%%

figure, ax = plt.subplots(2,figsize=(3.3,3.3), dpi=200, sharey=True)

bins = np.arange(0,30,1)
h0,b0 = np.histogram(r_AL,bins,density=True)
error0 = np.sqrt(h0/len(r_AL))
ax[0].bar(b0[:-1],height=h0 ,width =1,color='peru',edgecolor='navajowhite', ecolor='orange',yerr=error0,capsize=4, label=r'$r_{AL}$')

ax[0].set_title('Distribución del estadístico $r_{AL}$')
ax[0].set_xlabel('$r_{AL}$')
ax[0].set_ylabel('Probabilidad')
ax[0].set_xticks(bins)
ax[0].tick_params(which='minor', length=1.75, width=1)
ax[0].tick_params(which='major', length=3, width=1.25)
ax[0].legend()



h1,b1 = np.histogram(r_ES,bins,density=True)
error1 = np.sqrt(h1/len(r_ES))
ax[1].bar(b1[:-1],height=h1 ,width =1,color='cadetblue',edgecolor='deepskyblue', ecolor='b',yerr=error1,capsize=4, label=r'$r_{ES}$')

ax[1].set_title('Distribución del estadístico $r_{ES}$')
ax[1].set_xlabel('$r_{ES}$')
ax[1].set_ylabel('Probabilidad')
ax[1].set_xticks(bins)
ax[1].legend()
ax[1].tick_params(which='minor', length=1.75, width=1)
ax[1].tick_params(which='major', length=3, width=1.25)

figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
figManager.window.showMaximized()           ####   esto y la linea de arriba me maximiza la ventana de la figura
plt.show()




#%%
# Calculo el r_c para el idioma ALEMAN. Pidiendo una significancia de A LO SUMO 5%
i=0
p=0
while i<0.95:
    i+=h0[p]
    p+=1

r_AL_C = p

print(r_AL_C)
#==============================================================================
#                            Calculo la potencia del test considerando H1 
#==============================================================================

i=0
p=0
while p<r_AL_C:
    i+=h1[p]
    p+=1
# i=i-h[p]
potencia = 1-i


print(r_AL_C, potencia)


#%%

#==============================================================================
#                            PUNTO 6 - Me quedo en casa
#==============================================================================
#==============================================================================
#                            Rachas observadas en el libro
#==============================================================================
palabras_libro = ['Si', 'En', 'primer', 'reino', 'conocimiento', 'en', 'el', 'madre', 'que', 'Sus', 'mar', 'oro', 'que', 'echar', 'Y', 'y', 'siguieron', 'salvado', 'nueva', 'en', 'dentro', 'quién', 'los', 'roca', 'gran', 'cardaban', 'rey', 'y', 'buenos', 'mil']

#calculo el largo de las palabras elegidas.
t_libro = []
for p in palabras_libro:
    t_libro.append(len(p))

#calculo la cantidad de rachas en las palabras del libro. Las llamo r_OBS
r_OBS = 0

i=0
mediana = np.median(r_AL)

while i<len(t_libro)-1:
    if t_libro[i]<mediana<t_libro[i+1] or t_libro[i]>mediana>t_libro[i+1]: #Cumpleaños en febrero, entonces si es igual rechazo el valor.
        r_OBS +=1
        i+=1
    else:
        i+=1

i=r_OBS
p_valor=0
while i<len(h0):
    p_valor+=h0[i]
    i+=1


print(r_OBS, p_valor)

i=r_OBS
error_II = 0
while i<len(h0):
    error_II+=h1[i]
    i+=1

print(r_OBS, error_II)


#%%

figure, ax = plt.subplots(2,figsize=(3.3,3.3), dpi=200, sharey=True)

bins = np.arange(0,30,1)
h0,b0 = np.histogram(r_AL,bins,density=True)
error0 = np.sqrt(h0/len(r_AL))
ax[0].bar(b0[:-1],height=h0 ,width =1,color='peru',edgecolor='navajowhite', ecolor='orange',yerr=error0,capsize=4, label=r'$r_{AL}$')

ax[0].axvline(r_AL_C,h0[r_AL_C],color='r',linestyle='--')
ax[0].text(r_AL_C*1.01,h0[r_AL_C]*3.5,s='$r_{AL}^c$', color='r',rotation=90)

ax[0].axvline(r_OBS,0,color='green',linestyle='-')
ax[0].text(r_OBS,h0[r_AL_C]*3.5,s='$r_{OBS}$', color='green', fontweight='bold',rotation=90)


ax[0].set_title('Distribución del estadístico $r_{AL}$')
ax[0].set_xlabel('$r_{AL}$')
ax[0].set_ylabel('Probabilidad')
ax[0].set_xticks(bins)
ax[0].tick_params(which='minor', length=1.75, width=1)
ax[0].tick_params(which='major', length=3, width=1.25)
ax[0].legend()



h1,b1 = np.histogram(r_ES,bins,density=True)
error1 = np.sqrt(h1/len(r_ES))
ax[1].bar(b1[:-1],height=h1 ,width =1,color='cadetblue',edgecolor='deepskyblue', ecolor='b',yerr=error1,capsize=4, label=r'$r_{AL}$')

ax[1].axvline(r_AL_C,h0[r_AL_C],color='r',linestyle='--')
ax[1].text(r_AL_C*1.01,h0[r_AL_C]*3.5,s='$r_{AL}^c$', color='r',rotation=90)

ax[1].set_title('Distribución del estadístico $r_{ES}$')
ax[1].set_xlabel('$r_{ES}$')
ax[1].set_ylabel('Probabilidad')
ax[1].set_xticks(bins)
ax[1].legend()
ax[1].tick_params(which='minor', length=1.75, width=1)
ax[1].tick_params(which='major', length=3, width=1.25)

figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
figManager.window.showMaximized()           ####   esto y la linea de arriba me maximiza la ventana de la figura
plt.show()


#%%
#==============================================================================
#                            ANEXO - Dos colas
#==============================================================================
# Calculo el r_c para el idioma ALEMAN. Pidiendo una significancia de A LO SUMO 5%
i=0
p=0
while i<0.925:
    i+=h0[p]
    p+=1

r_AL_C_upper = p

i=0
p=0
while i<0.025:
    i+=h0[p]
    p+=1

r_AL_C_lower = p

print(r_AL_C_lower, r_AL_C_upper)

figure, ax = plt.subplots(1,figsize=(3.3,3.3), dpi=200, sharey=True)

bins = np.arange(0,30,1)
h0,b0 = np.histogram(r_AL,bins,density=True)
error0 = np.sqrt(h0/len(r_AL))
ax.bar(b0[:-1],height=h0 ,width =1,color='peru',edgecolor='navajowhite', ecolor='orange',yerr=error0,capsize=4, label=r'$r_{AL}$')

ax.axvline(r_AL_C_lower,h0[r_AL_C],color='r',linestyle='--')
ax.text(r_AL_C_lower*0.85,h0[r_AL_C]*4,s='$r_{L}^C$', color='r',rotation=90)

ax.axvline(r_AL_C_upper,h0[r_AL_C],color='r',linestyle='--')
ax.text(r_AL_C_upper*1.025,h0[r_AL_C]*4,s='$r_{U}^C$', color='r',rotation=90)

ax.axvline(r_OBS,0,color='green',linestyle='-')
ax.text(r_OBS,h0[r_AL_C]*3.5,s='$r_{OBS}$', color='green', fontweight='bold',rotation=90)

ax.set_title('Distribución del estadístico $r_{AL}$')
ax.set_xlabel('$r_{AL}$')
ax.set_ylabel('Probabilidad')
ax.set_xticks(bins)
ax.tick_params(which='minor', length=1.75, width=1)
ax.tick_params(which='major', length=3, width=1.25)
ax.legend()
figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
figManager.window.showMaximized()           ####   esto y la linea de arriba me maximiza la ventana de la figura
plt.show()

