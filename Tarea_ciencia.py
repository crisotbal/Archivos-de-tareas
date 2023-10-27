#!/usr/bin/env python
# coding: utf-8

# ## Rango intercualtil

# In[2]:


def IQR(d):
    n = len(d)
    d.sort()
    if n%4 == 0:
        es = n/4
        q1 = (d[es+1]+d[es])/2
        ter = es*3
        q3 = (d[ter+1]+d[ter])/2
        dq = q3-q1
    else:
        f = n//4
        a = f+1
        q1 = d[a]
        ra = a*3
        q3 = d[ra]
        dq = q3-q1
    return dq


# ## Varianza

# In[3]:


def Varianza(o):
    x = Promedio(o)
    n = len(o)
    suma = 0
    for k in o:
        r = (k-x)**2
        suma = suma + r
    var = suma/n
    return var


# ## Desviaciòn estandar

# In[ ]:


def Desviaciòn_est(u):
    desv = (Varianza(u))**(1/2)
    return desv


# ## Promedio

# In[4]:


def Promedio(x):
    n = len(x)
    suma = 0
    for h in x:
        suma = suma + h
    prom = (suma/n)
    return prom


# ## Mediana

# In[ ]:


def mediana(m):
    
    m.sort()
    if len(m)%2 == 0:
        c = int(len(m)/2)-1
        j = m[c]
        h = m[c+1]
        med = (h-j)/2
        if med == 0:
            med = j
        
    else:
        n = (len(m)-1)/2
        f = n+1
        med = m[int(f-1)]
        if med == 0:
            med = n
            
    return med


# ## Moda

# In[ ]:


def moda(mm):
    if len(mm) == 0:
        return None  # Devuelve None si la lista está vacía.

    cuenta = {}  # Diccionario para almacenar las frecuencias de los elementos.
    
    # Contar las frecuencias de los elementos en la lista.
    for n in mm:
        if n in cuenta:
            cuenta[n] += 1
        else:
            cuenta[n] = 1

    # Encontrar el elemento con la frecuencia máxima.
    moda = None
    max_cuenta = 0
    for n, frec in cuenta.items():
        if frec > max_cuenta:
            moda = n
            max_cuenta = frec
        elif frec == max_cuenta and n != moda:
            # En caso de empate, si hay múltiples modas, devuelve una lista de las modas.
            if not isinstance(moda, list):
                moda = [moda]
            moda.append(n)
    
    if max_cuenta == 1:
        return None  # Si todas las frecuencias son 1, no hay moda.
    elif isinstance(moda, list):
        return moda
    else:
        return moda


# ## Rango

# In[ ]:


def rango(x):

    x.sort()
    ran = abs(x[-1]-x[0])
    return ran


# ## Desviaciòn mediana absoluta

# In[ ]:


def MAD(r):
    r.sort()
    for w in r:
        u = []
        a = abs(w-(Promedio(r)))
        u.append(a)
    loco = mediana(u)
    return loco

