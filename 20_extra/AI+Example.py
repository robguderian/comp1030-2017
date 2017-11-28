
# coding: utf-8

# # Decision Tree example

# In[30]:


myFile = open('class.csv')

features = []
labels = []
skipFirst = True
for line in myFile.readlines():
    if not skipFirst:
        cleanline = line.strip()
        theseFeatures = cleanline.split(",")
        print(theseFeatures)
        featuresToAdd = [float(theseFeatures[1]),
                        float(theseFeatures[2]),
                        float(theseFeatures[3]),
                        float(theseFeatures[4]),
                        float(theseFeatures[5]),
                        float(theseFeatures[6]),
                        float(theseFeatures[7]),
                        float(theseFeatures[8])]
        labels.append(theseFeatures[10])
        features.append(featuresToAdd)
    skipFirst = False


# In[31]:


labels


# In[32]:


features


# In[33]:


from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)


# In[35]:


testData = [ 86, 90, 64, 76, 72, 68, 65, 89]
clf.predict([testData])


# In[36]:


import random


# In[52]:


# python dark magic
# google list comprehension
testData = [random.randint(60, 65) for _ in range(0, 8)] 
print(testData)
clf.predict([testData])


# In[55]:


myFile = open('class.csv')

features = []
labels = []
skipFirst = True
for line in myFile.readlines():
    if not skipFirst:
        cleanline = line.strip()
        theseFeatures = cleanline.split(",")
        print(theseFeatures)
        featuresToAdd = [float(theseFeatures[1]),
                        float(theseFeatures[2]),
                        float(theseFeatures[3]),
                        float(theseFeatures[4]),
                        float(theseFeatures[5]),
                        float(theseFeatures[6]),
                        float(theseFeatures[7]),
                        float(theseFeatures[8])]
        labels.append(theseFeatures[9])
        features.append(featuresToAdd)
    skipFirst = False


# In[56]:


from sklearn import tree
clf = tree.DecisionTreeRegressor()
clf = clf.fit(features, labels)


# In[57]:


# python dark magic
# google list comprehension
testData = [random.randint(60, 65) for _ in range(0, 8)] 
print(testData)
clf.predict([testData])


# In[60]:




