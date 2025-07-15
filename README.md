# Bachelor-project
## My bachelor project (SMS spam detection)
A simple implementation of AI to an Android app, the app in question was created only as a demonstration to show how it could be used.

## How it works?

1. The Android app runs in the background and listens for incoming SMS notifications.
2. Upon receiving an SMS, it sends the message text to the Flask server.
3. The server pre-processes the text (Text cleaning, tokenization,, removing stop words, stemming, ).
4. The processed text is passed to the trained Naive Bayes model.
5. The model predicts whether the SMS is spam or not spam.
6. The result is sent back to the Android app, which results in a notification to be shown on the phone.

   

## **The limitations (drawbacks):**

The app and the server must be on the same network. If the SMS is sent to the wrong IP, the classification fails.
The Android app currently has no GUI, it functions as a background service only.
The model is trained only on English spam messages.

## The potential (Future possible improvements.)

1. Embedding the model directly inside the Android app, to remove the need for a network or server.
2. Adding support for multiple languages in the dataset and model.
3. Building a proper GUI for the app turning it into a full messaging client with spam filtering.
4. Add a feature to collect 'wild' data:
5. an opt‑in feature in the GUI where users can choose which SMS messages to upload back to the server to use that feedback  to continuously expand and retrain the model on real‑world spam samples.
6. adding encryption safety measures for user data protection (have an application for RSA encryption/decryption, maybe will do something with that too.)
7. Maybe not limit it to SMS spam but also include a E-mail spam message detection too.
8. Enchancing the text processing (with: Contraction handling, Spell-checking and emotion and emoji detection.)


## How it looks like

1. <img width="540" height="800" alt="image" src="https://github.com/user-attachments/assets/77b79e1e-765d-4731-a038-a671af497f40" />




2. <img width="540" height="800" alt="image" src="https://github.com/user-attachments/assets/535ff390-d460-4a12-baf0-4eb71dad775b" />

 

**The project, is just a proof-of-concept of AI integration into Mobile apps, It isn’t a production‑ready messaging solution. And it also was my first time building android app, using android studio.** 

