------
La [[Criptografía]] se basa en su mayoría en cifrar mensajes susando funciones de un solo sentido, es decir, funciones que sean fáciles de computar pero difíciles de invertir, un ejemplo de estas funciones es la multiplicación.


![[Pasted image 20230106055653.png]]


![[Pasted image 20230106060120.png]]

-----------------------

1.  In this video, we're going to discuss encryption and quantum computing, and the intersections between the two.
2.  We currently live in a data-driven world and I say that because we have so many internet users out there transmitting a lot of data. 
3.  In 2020, we saw approximately 4.5 billion internet users and each of them are transmitting an enormous amount of data in the form of communications, such as emails and texts and social network interactions, and then transactions for commerce or online banking.
4.  So all these communications are holding very sensitive data so we want to make sure that these communications are kept secure and encryption helps us do that.
5.  So how does encryption work? On a high level, we have a message that, here in this example, we see a message to our friend. And we combine that with a secret key in order to generate ciphertext.
6.  Once we have ciphertext, it almost makes the message seem completely random and unusable so the contents of that message are kept safe.
7.  So how is encryption secure? Encryption is based on one-way cryptographic functions.  
8.  A one-way function is a function that's easy to compute but difficult to invert. Multiplication can be thought of as an example and that's because it's easy to multiply but a little bit more difficult to factor.
9.  That actually becomes the basis of key generation for a lot of encryption schemes because we take prime numbers and then we multiply them in order to create a key.
10.  Knowledge of the keys or the key factors allows for data decryption, so we want to make sure that we keep those secret and away from anyone who might want to try to read the data.
11.  So we think about generating a key. We can think about it, uh, in like how we think of mixing paint. It's easy to mix paint but it's really difficult to unmix paint once it's combined.
12.  So we have here two prime numbers that we multiply together but once we have them multiplied together it's difficult to pull them back out into their factors.
13.  So how does quantum computing disrupt modern encryption? Modern encryption uses large keys and because it's hard to, it's really challenging to factor a large number, our data stays relatively secure just because it's a pretty intractable problem to try to come up with the factors for that key.
14.  So for example, if we have a key that is 1024 bits in length that is equivalent to 309 decimal digits and even the best quantum or even the best classical computers will have a difficult time factoring that value.
15.  So what if factoring was more efficient? Encryption would essentially be broken.
16.  And we have Shor's algorithm, which is a quantum algorithm that factors numbers exponentially faster than the best classical algorithm.
17.  So, if we have a quantum computer that can implement Shor's algorithm, in theory all encrypted messages--past and present--would be vulnerable to decryption.
18.  So with that in mind, how concerned should we be?  
19.  Well, quantum computers are currently not large enough to run Shor's algorithm. And decades are needed to make our computers a little bit more robust, in the sense that we need to refine and scale our devices.
20.  And additionally, security has adapted in the past, as technology improves, so in post-quantum cryptography we'll be able to assist in our transition to a quantum future.


