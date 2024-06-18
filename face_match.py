#!/usr/bin/env python
# coding: utf-8

# In[8]:


import face_recognition


# In[35]:


image_of_biden = face_recognition.load_image_file('biden.jpeg')
known_face_encoding = face_recognition.face_encodings(image_of_biden)[0]


# In[33]:


unknown_image = face_recognition.load_image_file('biden_speach.JPG')
unknown_face_locations = face_recognition.face_locations(unknown_image)
unknown_face_encodings = face_recognition.face_encodings(unknown_image, unknown_face_locations)


# In[34]:


print("I found {} face(s) in this photograph.".format(len(face_locations)))


# In[38]:


for unknown_face_encoding in unknown_face_encodings:
    results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)
    
    if results[0]:
        print("Found the known face in the unknown image!")
    else:
        pass

